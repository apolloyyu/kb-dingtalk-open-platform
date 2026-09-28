---
title: "使用循环渲染容器渲染列表"
source_url: "https://open.dingtalk.com/document/development/render-list-using-loop-rendering-containers"
namespace: "development"
slug: "render-list-using-loop-rendering-containers"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "搭建平台 > 使用教程 > 使用循环渲染容器渲染列表"
doc_id: "qzZHPlF1a4"
updated_at: "2026-05-19 17:05:15"
---

> Source: https://open.dingtalk.com/document/development/render-list-using-loop-rendering-containers
> Path: 互动卡片 / 模板搭建卡片 / 搭建平台 > 使用教程 > 使用循环渲染容器渲染列表
> Updated: 2026-05-19 17:05:15

# 使用循环渲染容器渲染列表

本文基于一个会议邀请卡片，详细讲解卡片模板搭建过程中的一些方法与技巧，特别是如何使用循环渲染容器渲染一个数量不确定的列表元素。

## **步骤一：分析卡片结构**

这是一个会议邀请卡片的需求，需要在卡片上展示会议的基本信息以及一个“确认参加”按钮，参会者点击该按钮后，按钮文案需要变成“已确认”，且按钮需要变成不可点击状态。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8261286271/p837088.png)![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8261286271/p837101.png)

卡片内容由“卡片头部”、卡片主标题、会议议程与操作按钮组成。其中，比较复杂的部分是会议议程，会议议程是一个列表，而且列表条目不固定，所以需要使用“循环渲染容器”来实现。每一个列表条目项都由两个左右布局的容器组成，左侧容器渲染序号，右侧容器中的文案最多显示两行，超出的部分需要省略。

## 步骤二：搭建卡片头部与卡片标题

我们使用“卡片头部”组件，由于头部文案是固定的，我们将文案写死在模板中即可。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8261286271/p837089.png)

接下来，我们使用文本组件作为卡片的主标题，同时调整一下文本元素的样式和其四周的外边距。这里需要注意的是，不同的组件有不同的默认外边距，在搭建卡片模板时，为了保证模板的美观性，我们建议在卡片的四周保留12个单位的空白，卡片纵向排列的内容之间，可以根据实际情况保留8到12个单位的间隔。

由于卡片的主标题会随着不同的会议有所区别，所以我们需要为卡片主标题的文案绑定变量，同时设置mock数据用于调试。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8261286271/p837090.png)

## 步骤三：搭建单个会议议程条目

首先，使用文本元素来搭建“会议议程”的小标题。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8261286271/p837091.png)

接下来，我们开始搭建最复杂的列表部分，我们先不考虑列表的循环问题，先单独搭建一个列表条目。

列表条目需要使用一个独立的“容器”来包裹，容器内部又分为左右排布的两个子容器。

我们先搭建左侧的容器部分，它的宽度与高度是固定的，且内部有一个文本元素。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8261286271/p837095.png)

接下来，我们搭建右侧的内容容器，需要注意的是右侧的容器需要根据卡片宽度进行自适应，因此我们需要开启容器的“占据内容”选项。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8261286271/p837096.png)

## 步骤四：使用循环渲染容器渲染列表

循环渲染容器需要配合“对象数组”变量使用，因此，我们需要先定义一个“对象数组”变量，变量中包含具体的议程列表内容。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8261286271/p837097.png)

然后我们添加一个“循环渲染容器”组件，绑定之前定义的变量，然后把我们刚刚搭建的“列表条目”拖入循环渲染容器中。

这里有个小提示，当页面中元素过多，难以选中时，可以在“大纲树”面板中进行拖拽操作。

此时点击“预览模式”，会发现我们之前搭建的“列表条目”元素被渲染了三个，与我们mock数据中配置的条目数量一致。不过现在有两个问题，一个是列表条目之间没有间隔，不太美观，另一个问题是每个列表条目的内容都是一样的。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8261286271/p837098.png)

针对第一个问题，我们可以通过修改循环渲染容器的“子元素间距”属性来解决。

针对第二个问题，需要我们为列表条目中的内容绑定变量来实现。我们选择列表的文本内容，在绑定变量时会发现选项中多出了“循环变量”的属性。这个属性来自于“循环渲染容器”所绑定的对象数组变量中对象的属性值。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8261286271/p837099.png)

目前，列表的渲染已经基本符合预期了，不过前面的序号还没有处理。当然，我们可以选择在我们的对象数组中新增一个与content并列的index的属性，然后手动写入序号，不过我们有更简单的方式来实现。

我们可以选择新建一个“表达式变量”，命名为index，然后写入表达式“subdata Index”，该表达式的功能是在循环渲染容器中，获取当前项目的索引值。因为索引值是从0开始的，所以作为序号，我们需要加1。

最后，我们为序号所对应的文本元素绑定index变量，即可完成整体的列表渲染。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8261286271/p837100.png)

## **视频演示**

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20240920/hfoder/%E4%BD%BF%E7%94%A8%E5%BE%AA%E7%8E%AF%E6%B8%B2%E6%9F%93%E5%AE%B9%E5%99%A8%E6%B8%B2%E6%9F%93%E5%88%97%E8%A1%A8.mp4)
