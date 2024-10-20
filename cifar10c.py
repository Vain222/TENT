import logging

import torch
import torch.optim as optim
import numpy as np

from robustbench.data import load_cifar10c, load_cifar10
from robustbench.model_zoo.enums import ThreatModel
from robustbench.utils import load_model
from robustbench.utils import clean_accuracy as accuracy

import tent
import norm

from conf import cfg, load_cfg_fom_args


logger = logging.getLogger(__name__)


def evaluate(description):
    load_cfg_fom_args(description)
    # configure model
    print("loading model")
    base_model = load_model(cfg.MODEL.ARCH, cfg.CKPT_DIR,
                       cfg.CORRUPTION.DATASET, ThreatModel.corruptions).cuda()
    # base_model.load_state_dict(torch.load("ckpt/cifar10/corruptions/my_train.pth"))
    print("model loaded")
    if cfg.MODEL.ADAPTATION == "source":
        logger.info("test-time adaptation: NONE")
        model = setup_source(base_model)
    if cfg.MODEL.ADAPTATION == "norm":
        logger.info("test-time adaptation: NORM")
        model = setup_norm(base_model)
    if cfg.MODEL.ADAPTATION == "tent":
        logger.info("test-time adaptation: TENT")
        model = setup_tent(base_model)
    if cfg.MODEL.ADAPTATION == "eata":
        logger.info("test-time adaptation: EATA")
        model = setup_eata(base_model)
    # evaluate on each severity and type of corruption in turn
    for severity in cfg.CORRUPTION.SEVERITY:
        for corruption_type in cfg.CORRUPTION.TYPE:
            # reset adaptation for each combination of corruption x severity
            # note: for evaluation protocol, but not necessarily needed
            try:
                model.reset()
                logger.info("resetting model")
            except:
                logger.warning("not resetting model")
            x_test, y_test = load_cifar10c(cfg.CORRUPTION.NUM_EX,
                                           severity, cfg.DATA_DIR, False,
                                           [corruption_type])
            # x_test, y_test = load_cifar10()

            # mean = np.array([0.4914, 0.4822, 0.4465])
            # # mean = np.array([0.5, 0.5, 0.5])
            # std = np.array([0.2470, 0.2435, 0.2616])
            # # std = np.array([0.5, 0.5, 0.5])
            # mean = torch.tensor(mean, dtype=torch.float32).view(1, 3, 1, 1).to(x_test.device)
            # std = torch.tensor(std, dtype=torch.float32).view(1, 3, 1, 1).to(x_test.device)
            # x_test = (x_test - mean) / std
            # x_test = torch.clamp(x_test, 0, 1)
            
            x_test, y_test = x_test.cuda(), y_test.cuda()
            acc = accuracy(model, x_test, y_test, cfg.TEST.BATCH_SIZE)
            err = 1. - acc
            logger.info(f"error % [{corruption_type}{severity}]: {err:.2%}")


def setup_source(model):
    """Set up the baseline source model without adaptation."""
    model.eval()
    logger.info(f"model for evaluation: %s", model)
    return model


def setup_norm(model):
    """Set up test-time normalization adaptation.

    Adapt by normalizing features with test batch statistics.
    The statistics are measured independently for each batch;
    no running average or other cross-batch estimation is used.
    """
    norm_model = norm.Norm(model)
    logger.info(f"model for adaptation: %s", model)
    stats, stat_names = norm.collect_stats(model)
    logger.info(f"stats for adaptation: %s", stat_names)
    return norm_model


def setup_tent(model):
    """Set up tent adaptation.

    Configure the model for training + feature modulation by batch statistics,
    collect the parameters for feature modulation by gradient optimization,
    set up the optimizer, and then tent the model.
    """
    model = tent.configure_model(model)
    params, param_names = tent.collect_params(model)
    optimizer = setup_optimizer(params)
    print(cfg.OPTIM.STEPS)
    print(cfg.MODEL.EPISODIC)
    tent_model = tent.Tent(model, optimizer,
                           steps=cfg.OPTIM.STEPS,
                           episodic=cfg.MODEL.EPISODIC)
    logger.info(f"model for adaptation: %s", model)
    logger.info(f"params for adaptation: %s", param_names)
    logger.info(f"optimizer for adaptation: %s", optimizer)
    return tent_model

def setup_eata(model):
    import eata
    import math
    from selectedRotateImageFolder import prepare_test_data
    model = eata.configure_model(model)
    params, param_names = eata.collect_params(model)
    # optimizer = torch.optim.SGD(params, 0.005, momentum=0.9)
    optimizer = setup_optimizer(params)
    # adapt_model = eata.EATA(model, optimizer, None, e_margin=math.log(1000)*0.40, d_margin=0.05) 
    adapt_model = eata.EATA(model, optimizer, e_margin=10, d_margin=0.1) 
    logger.info(f"model for adaptation: %s", model)
    logger.info(f"params for adaptation: %s", param_names)
    logger.info(f"optimizer for adaptation: %s", optimizer)
    # compute fisher informatrix
    # args.corruption = 'original'
    # argss = eata.get_args()
    # argss.corruption = 'original'
    # fisher_dataset, fisher_loader = prepare_test_data(argss)
    # fisher_dataset.set_dataset_size(argss.fisher_size)
    # fisher_dataset.switch_mode(True, False)

    # model = eata.configure_model(model)
    # params, param_names = eata.collect_params(model)
    # ewc_optimizer = torch.optim.SGD(params, 0.001)
    # fishers = {}
    # train_loss_fn = torch.nn.CrossEntropyLoss().cuda()
    # for iter_, (images, targets) in enumerate(fisher_loader, start=1):      
    #     if argss.gpu is not None:
    #         images = images.cuda(argss.gpu, non_blocking=True)
    #     if torch.cuda.is_available():
    #         targets = targets.cuda(argss.gpu, non_blocking=True)
    #     outputs = model(images)
    #     _, targets = outputs.max(1)
    #     loss = train_loss_fn(outputs, targets)
    #     loss.backward()
    #     for name, param in model.named_parameters():
    #         if param.grad is not None:
    #             if iter_ > 1:
    #                 fisher = param.grad.data.clone().detach() ** 2 + fishers[name][0]
    #             else:
    #                 fisher = param.grad.data.clone().detach() ** 2
    #             if iter_ == len(fisher_loader):
    #                 fisher = fisher / iter_
    #             fishers.update({name: [fisher, param.data.clone().detach()]})
    #     ewc_optimizer.zero_grad()
    # logger.info("compute fisher matrices finished")
    # del ewc_optimizer

    # optimizer = torch.optim.SGD(params, 0.00025, momentum=0.9)
    # adapt_model = eata.EATA(model, optimizer, fishers, argss.fisher_alpha, e_margin=argss.e_margin, d_margin=argss.d_margin)
    return adapt_model

def setup_optimizer(params):
    """Set up optimizer for tent adaptation.

    Tent needs an optimizer for test-time entropy minimization.
    In principle, tent could make use of any gradient optimizer.
    In practice, we advise choosing Adam or SGD+momentum.
    For optimization settings, we advise to use the settings from the end of
    trainig, if known, or start with a low learning rate (like 0.001) if not.

    For best results, try tuning the learning rate and batch size.
    """
    if cfg.OPTIM.METHOD == 'Adam':
        return optim.Adam(params,
                    lr=cfg.OPTIM.LR,
                    betas=(cfg.OPTIM.BETA, 0.999),
                    weight_decay=cfg.OPTIM.WD)
    elif cfg.OPTIM.METHOD == 'SGD':
        return optim.SGD(params,
                   lr=cfg.OPTIM.LR,
                   momentum=cfg.OPTIM.MOMENTUM,
                   dampening=cfg.OPTIM.DAMPENING,
                   weight_decay=cfg.OPTIM.WD,
                   nesterov=cfg.OPTIM.NESTEROV)
    else:
        raise NotImplementedError


if __name__ == '__main__':
    evaluate('"CIFAR-10-C evaluation.')
