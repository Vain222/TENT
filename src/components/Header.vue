<script lang="ts" setup>
import { ElIcon } from 'element-plus'
import { SuccessFilled } from '@element-plus/icons-vue'

// 项目主页
const logo = {
    name: "PTTA",
    link: "#",
}
</script>

<template>
    <!-- 移除页首悬浮和水平导航目录相关代码 -->
    <div>
        <!-- 仅保留项目主页 -->
        <el-menu-item index="1">
            <el-icon :size="20"><SuccessFilled /></el-icon>
            <a :href=logo.link>{{ logo.name }} </a>
        </el-menu-item>
    </div>
</template>

<style>
/* 移除与导航相关的样式 */
/* 仅保留通用样式 */
/* 链接装饰，取消下划线和链接颜色 */
a {
	text-decoration: None;
	color: inherit;
}

/* 取消鼠标焦点悬浮在链接上的颜色装饰 */
a:hover {
  color: inherit;
  border-bottom: none;
}
</style>

<style scoped>
/* 移除与导航相关的样式 */
</style>