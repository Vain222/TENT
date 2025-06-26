<script lang="ts">

import { defineComponent } from 'vue'
import { VueLatex } from 'vatex'

export default defineComponent({
    components: {
        VueLatex
    },
    data() {
        return {
            isDetailSec1: false,
            isDetailSec2: true,
        }
    },
    methods: {
        toggleDetailSec1() {
            this.isDetailSec1 = !this.isDetailSec1;
            if (this.isDetailSec1) {
                const container = document.getElementById('malicious-sec1');
                if (container) {
                    container.style.marginBottom = '0px';
                }
            } else {
                const container = document.getElementById('malicious-sec1');
                if (container) {
                    container.style.marginBottom = '9px';
                }
            }
        },
        toggleDetailSec2() {
            this.isDetailSec2 = !this.isDetailSec2;
            if (this.isDetailSec2) {
                const container = document.getElementById('malicious-sec2');
                if (container) {
                    container.style.marginBottom = '0px';
                }
            } else {
                const container = document.getElementById('malicious-sec2');
                if (container) {
                    container.style.marginBottom = '9px';
                }
            }
        },
    },
})

</script>

<template>
  <div>
    <el-divider />

    <el-row justify="center">
        <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="markdown-title">
            Introduction
        </el-col>
    </el-row>

    <el-row justify="center">
        <el-col
            :xs="24" :sm="20" :md="16" :lg="12" :xl="12"
            id="malicious-sec1"
            @click="toggleDetailSec1"
        >
            <div v-if="!isDetailSec1" class="triangle-right"></div>
            <div v-if="isDetailSec1" class="triangle-down"></div>
            <h3 style="margin: 0 0 0 15px; ">
                1. Test-Time Model Adaptation (TTA)
            </h3>
        </el-col>
    </el-row>

    <transition name="fade">
    <el-row justify="center" v-if="isDetailSec1">
        <el-col :xs="24" :sm="20" :md="16" :lg="12" :xl="12">
            <p>
                Imagine a scenario where we need to make online predictions for test samples in an environment. 
                We generally select a suitable model and pre-trained weights from open-source model libraries. 
                Self-supervised model adaptation using test samples is beneficial for improving prediction accuracy.
            </p>
        </el-col>
    </el-row>
    </transition>

    <transition name="fade">
    <el-row justify="center" v-if="isDetailSec1">
        <el-col 
            :xs="24" :sm="20" :md="16" :lg="12" :xl="12"
            class="intro-img-container"
        >
            <img
                :src="'./malicious/tta.png'"
                alt="test-time model adaptation"
                class="img-intro-tta"
            >
        </el-col>
    </el-row>
    </transition>

    <el-row justify="center">
        <el-col
            :xs="24" :sm="20" :md="16" :lg="12" :xl="12"
            id="malicious-sec2"
            @click="toggleDetailSec2"
        >
            <div v-if="!isDetailSec2" class="triangle-right"></div>
            <div v-if="isDetailSec2" class="triangle-down"></div>
            <h3 style="margin: 0 0 0 15px; ">
                2. Malicious Sample Hazards
            </h3>
        </el-col>
    </el-row>

    <transition name="fade">
    <el-row justify="center" v-if="isDetailSec2">
        <el-col :xs="24" :sm="20" :md="16" :lg="12" :xl="12">
            <p>
                Not all test samples help with model adaptation. 
                Due to data distribution shifts,
                selecting benign samples and discarding malicious ones 
                often leads to smoother model optimization and more stable updates. 
                Yet, this strategy doesn't always work.
            </p>
            
            <p>
                Our observations show that high-entropy malicious samples 
                are harder to predict correctly than low-entropy ones. 
                Learning from high-entropy samples undermines optimization stability. 
            </p>
        </el-col>
    </el-row>
    </transition>

    <transition name="fade">
    <el-row justify="center" v-if="isDetailSec2">
        <el-col 
            :xs="24" :sm="20" :md="16" :lg="12" :xl="12"
            class="intro-img-container"
        >
            <img
                :src="'./malicious/avg_ent.png'"
                alt="Accuracy vs. Entropy"
                class="img-intro-malicious"
            >
        </el-col>
    </el-row>
    </transition>

    <transition name="fade">
    <el-row justify="center" v-if="isDetailSec2">
        <el-col :xs="24" :sm="20" :md="16" :lg="12" :xl="12">
            <p>
                More importantly, perfectly filtering out malicious samples is challenging. 
                This results in sharp performance fluctuations for TTA 
                with even slight adjustments to the sample selection threshold.
            </p>
        </el-col>
    </el-row>
    </transition>

    <transition name="fade">
    <el-row justify="center" v-if="isDetailSec2">
        <el-col 
            :xs="24" :sm="20" :md="16" :lg="12" :xl="12"
            style="display: flex; flex-direction: row; align-items: center; justify-content: center;"
        >
            <div class="intro-malicious-img-title-1">
                ResNet50
            </div>
            <div class="intro-malicious-img-title-2">
                ViT-B/16
            </div>
        </el-col>
    </el-row>
    </transition>

    <transition name="fade">
    <el-row justify="center" v-if="isDetailSec2">
        <el-col 
            :xs="24" :sm="20" :md="16" :lg="12" :xl="12"
            class="intro-img-container"
        >
            <img
                :src="'./malicious/resnet50.png'"
                alt="ResNet50"
                class="img-intro-malicious-curve"
            >
            <img
                :src="'./malicious/vitb16.png'"
                alt="Fig. 2 (right) ViT-B/16"
                class="img-intro-malicious-curve"
            >
        </el-col>
    </el-row>
    </transition>

  </div>
</template>

<style scoped>

.intro-malicious-img-title-1, .intro-malicious-img-title-2 {
    width: 49%; 
    text-align: center; 
    font-size: 20px;
    box-sizing: border-box;
    padding-left: 10%;
}

.intro-malicious-img-title-2 {
    padding-left: 5%;
}

.intro-img-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
}

.img-intro-malicious-curve {
    width: 45%;
    margin: 3px;
}

.img-intro-malicious {
    width: 80%;
    margin: 3px;
}

.img-intro-tta {
    width: 100%;
    margin: 3px;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

#malicious-sec1, #malicious-sec2 {
    cursor: pointer; 
    display: flex; 
    flex-direction: row; 
    align-items: center; 
    justify-content: flex-start;
    margin-top: 18px; 
    margin-bottom: 9px;
}

#malicious-sec2 {
    margin-bottom: 0px;
}

.triangle-right {
    width: 0;
    height: 0;
    border-top: 7px solid transparent;
    border-left: 14px solid black;
    border-bottom: 7px solid transparent;
    box-sizing: border-box;
    margin-top: 1px;
}

.triangle-down {
    width: 0;
    height: 0;
    border-left: 7px solid transparent;
    border-right: 7px solid transparent;
    border-top: 14px solid black;
    box-sizing: border-box;
    margin-top: 1px;
}

.img-pic-2 {
    width: 40%;
}

.img-pic-3 {
    width: 100%;
}

.img-pic {
    width: 65%;
    margin-bottom: 2px;
    margin-top: 2px;
}

@media (max-width: 1500px) {
    .img-pic {
        width: 80%;
        margin-bottom: 5px;
        margin-top: 5px;
    }
    .img-pic-2 {
        width: 60%;
    }
}

@media (max-width: 992px) {
    .img-pic {
        width: 70%;
        margin-bottom: 5px;
        margin-top: 5px;
    }
    .img-pic-2 {
        width: 30%;
    }
}

@media (max-width: 576px) {
    .img-pic {
        width: 90%;
        margin-bottom: 5px;
        margin-top: 5px;
    }
    .img-pic-2 {
        width: 45%;
    }
}

.img-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    /* box-shadow: var(--el-box-shadow-light); */
}

.markdown-title {
    font-family: "MyFont", Verdana, sans-serif;
    letter-spacing: 2px;
    font-size: 28px;
    font-weight: bold;
    text-align: center;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    unicode-bidi: isolate;
}

</style>
