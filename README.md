<article align="center" style="margin-bottom: 20px;">
    <h1 
        align="center"
        itemprop="title"
        style="font-size: 30px; font-weight: bold; margin-bottom: 20px;"
    >
    PTTA: <br/>Purifying Malicious Samples for Test-Time Model Adaptation
    </h1>
</article>

<div
    align="center"
    style="font-size: 18px; margin-bottom: 20px;"
>
    <a href="https://jimm0011.github.io/" target='_blank'>Jing Ma</a><sup>1</sup>&emsp;
    <a href="https://vain222.github.io/" target='_blank'>Hanlin Li</a><sup>1</sup>&emsp;
    <a href="https://eglxiang.github.io/" target='_blank'>Xiang Xiang</a><sup>1,2</sup>
</div>

<div 
    align="center"
    style="font-size: 16px; margin-bottom: 20px;"
>
<sup>1</sup>Huazhong University of Science and Technology (HUST)&emsp;

<sup>2</sup>Peng Cheng National Lab&emsp;
</div>


## Introduction

[![Website](https://img.shields.io/badge/Website-Online-27AE60.svg)](https://jimm0011.github.io/PTTA-proj/)
[![Arxiv](https://img.shields.io/badge/Arxiv-Preprint-A42C24.svg)]()

This repository contains the online website of [PTTA: Purifying Malicious Samples for Test-Time Model Adaptation]() published in [ICML 2025](https://icml.cc/Conferences/2025).
Please check the [paper]() for more details.

#### TL;DR (Too Long; Didn’t Read) :

> Rather than selecting and discarding malicious samples for test-time model adaptation, why not purify them into benign ones?



<details>
<summary>
    <b>Abstract :</b>
</summary>

Test-Time Adaptation (TTA) enables deep neural networks to adapt to arbitrary distributions during inference. Existing TTA algorithms generally tend to select benign samples that help achieve robust online prediction and stable self-training. Although malicious samples that would undermine the model's optimization should be filtered out, it also leads to a waste of test data. To alleviate this issue, we focus on how to make full use of the malicious test samples for TTA by transforming them into benign ones, and propose a plug-and-play method, PTTA. The core of our solution lies in the purification strategy, which retrieves benign samples having opposite effects on the objective function to perform Mixup with malicious samples, based on a saliency indicator for encoding benign and malicious data. This strategy results in effective utilization of the information in malicious samples and an improvement of the models' online test accuracy. In this way, we can directly apply the purification loss to existing TTA algorithms without the need to carefully adjust the sample selection threshold. Extensive experiments on four types of TTA tasks as well as classification, segmentation, and adversarial defense demonstrate the effectiveness of our method.

![Pipeline](./public/pipeline.jpg)

</details>



<details>
<summary>
    <b>Lay Summary :</b>
</summary>

How can deep neural networks evolve through self-supervision without human intervention? This is a recent research trend, but difficult to solve well due to real-world complexity.

Our paper identifies the "malicious sample hazards" as an obstacle to model self-evolution. Prior solutions typically select and filter out malicious samples that negatively impact model optimization, which also reduces utilization of already limited data. Rather than discarding them, why not purify malicious samples into benign ones? Surprisingly, we found that superimpose benign samples—which exert the most opposite influence on the objective function—onto malicious samples effectively mitigates these hazards. 

Our findings reveal a new direction: using purification strategies to boost sample utilization during autonomous machine learning. This enables stable and efficient self-supervised evolution of deep neural networks.

</details>



<details>
<summary>
    <b>BibTeX :</b>
</summary>

```
@inproceedings{ma2025ptta,
  title={PTTA: Purifying Malicious Samples for Test-Time Model Adaptation},
  author={Ma, Jing and Li, Hanlin and Xiang, Xiang},
  booktitle={Forty-second International Conference on Machine Learning},
  year={2025},
}
```

</details>



## News

- **May 2025**:
🎉 Our paper (PTTA) has been accepted by [ICML 2025](https://icml.cc/).

