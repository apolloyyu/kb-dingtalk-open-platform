---
title: "使用容器搭建复杂布局卡片"
source_url: "https://open.dingtalk.com/document/development/use-containers-to-build-complex-layout-cards"
namespace: "development"
slug: "use-containers-to-build-complex-layout-cards"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "搭建平台 > 使用教程 > 使用容器搭建复杂布局卡片"
doc_id: "04t961i5lG"
updated_at: "2026-05-19 17:05:12"
---

> Source: https://open.dingtalk.com/document/development/use-containers-to-build-complex-layout-cards
> Path: 互动卡片 / 模板搭建卡片 / 搭建平台 > 使用教程 > 使用容器搭建复杂布局卡片
> Updated: 2026-05-19 17:05:12

# 使用容器搭建复杂布局卡片

本教程基于一个审批场景的卡片，讲解了如何利用容器组件的排列，搭建复杂布局的卡片模板。

## **步骤一：分析卡片的布局**

我们需要搭建如下的一张审批卡片模板。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9911286271/p835540.png)

可以看出，这张卡片由卡片头部、卡片主内容区域和卡片操作按钮三个部分组成。其中卡片主内容区域由一个左右布局的列表和一个覆盖在内容上面的图片组成。

## **步骤二：搭建卡片框架**

我们先搭建三个元素，一个“卡片头部”元素、一个“单个容器”元素和一个“单个按钮”元素，然后调整它们的样式和间距，完成卡片整体框架搭建。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9911286271/p835541.png)

## **步骤三：搭建**“审批通过”**的图标样式**

接下来，我们搭建主内容区域中，右侧的“审批通过”印章样式，印章需要覆盖在列表内容的上方。

我们需要在主内容区域容器中搭建左右排列的两个“单个容器”组件，并在右侧的容器中添加一个“印章”样式的图片。我们让左侧的容器组件撑满整个父容器的宽度，给右侧的容器设置固定值为70的宽度和高度，同时再给右侧的容器设置一个值为-70的左边距，即可实现让右侧容器覆盖在左侧容器上方的“印章”样式。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9911286271/p835542.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9911286271/p835543.png)

## **步骤四：搭建报销内容列表**

每一个列表条目都是由左右两个容器组成，左侧容器宽度是固定的，右侧容器宽度需要根据卡片剩余宽度自适应。

首先要搭建两个左右布局的容器，为左侧容器设置一个固定的容器宽度，同时给右侧的容器开启“占据内容”选项。开启了”占据内容“选项的容器会根据其父容器的横向剩余空间，按比例自适应宽度。

然后在左侧容器内部添加一个“标签组件”，在右侧容器内部添加一个“基础文本”组件，调整它们的样式，即可完成单个列表条目的搭建。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9911286271/p835544.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9911286271/p835545.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9911286271/p835549.png)

我们把搭建好了的列表条目复制两个，调整其中元素的文本和样式，即可完成整个卡片模板的搭建。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9911286271/p835546.png)

## **视频演示**

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20240816/jrbnjp/%E4%BD%BF%E7%94%A8%E5%AE%B9%E5%99%A8%E6%90%AD%E5%BB%BA%E5%A4%8D%E6%9D%82%E5%B8%83%E5%B1%80%E5%8D%A1%E7%89%87.mov)
