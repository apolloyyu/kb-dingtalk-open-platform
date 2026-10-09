---
title: "使用容器搭建数据看板卡片"
source_url: "https://open.dingtalk.com/document/development/use-containers-to-build-a-data-board-card"
namespace: "development"
slug: "use-containers-to-build-a-data-board-card"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "搭建平台 > 使用教程 > 使用容器搭建数据看板卡片"
doc_id: "d4slzJFVDy"
updated_at: "2026-05-19 17:05:13"
---

> Source: https://open.dingtalk.com/document/development/use-containers-to-build-a-data-board-card
> Path: 互动卡片 / 模板搭建卡片 / 搭建平台 > 使用教程 > 使用容器搭建数据看板卡片
> Updated: 2026-05-19 17:05:13

# 使用容器搭建数据看板卡片

本教程讲解了如何利用容器组件的排列，搭建一个数据看板卡片模板。

## **步骤一：分析卡片的布局**

我们需要搭建如下的一张数据看板卡片模板。

![20240815205538](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4851286271/p835596.jpg)

可以看出，这张卡片由卡片头部、数据看板区域和查看详情按钮三个部分组成。其中数据看板区域由三个灰色背景色的容器组成，它们分两行展示，第一行有一个单独的容器，第二行有两个横向排列的等宽容器。

## **步骤二：搭建卡片框架**

我们先搭建三个元素，一个“卡片头部”元素、一个“单个容器”元素和一个“单个按钮”元素，然后调整它们的样式和间距，完成卡片整体框架搭建。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4851286271/p835618.png)

## **步骤三：搭建一个数据看板模块**

接下来，我们搭建一个数据看板模块。首先搭建一个“单个容器”元素，并为其设置背景色、圆角、padding等属性。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4851286271/p835617.png)

容器内部的内容由两行组成，一行是一个文本元素，另一行是一个容器，容器内有两个横向排列的文本元素。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4851286271/p835616.png)

我们搭建完成基本元素后，调整各元素的样式与间距，完成数据看板模块的搭建。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4851286271/p835615.png)

## **步骤四：搭建整体数据看板**

数据看板由三个数据看板模块组成，看板整体分两行，我们用两个“单个容器”元素来搭建数据看板的布局，这里需要把它们的子元素设置成“横向排列”。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4851286271/p835614.png)

我们把之前搭建的数据看板模块复制两个，分别拖入刚刚搭建的数据看板布局元素内，并调整它们的间距。这里我们需要为第二行的两个数据看板模块元素分别设置“占据内容”为1，让它们实现等比例自适应。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4851286271/p835612.png)

最后，我们修改数据看板模块中的文本内容，即可完成整个卡片的搭建。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4851286271/p835611.png)

## **视频演示**

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20240920/bxmkmf/%E4%BD%BF%E7%94%A8%E5%AE%B9%E5%99%A8%E6%90%AD%E5%BB%BA%E6%95%B0%E6%8D%AE%E7%9C%8B%E6%9D%BF%E5%8D%A1%E7%89%87.mp4)
