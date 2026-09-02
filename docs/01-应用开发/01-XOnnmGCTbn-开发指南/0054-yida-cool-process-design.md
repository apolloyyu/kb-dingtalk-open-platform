---
title: "酷流程设计"
source_url: "https://open.dingtalk.com/document/dingstart/yida-cool-process-design"
namespace: "dingstart"
slug: "yida-cool-process-design"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发群聊酷应用 > 宜搭群聊酷应用（ISV应用） > 酷流程设计"
doc_id: "7OvoRGIGiB"
updated_at: "2026-07-22 16:55:20"
---

> Source: https://open.dingtalk.com/document/dingstart/yida-cool-process-design
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发群聊酷应用 > 宜搭群聊酷应用（ISV应用） > 酷流程设计
> Updated: 2026-07-22 16:55:20

# 酷流程设计

介绍如何将卡片与业务流程进行绑定关联。

## **酷流程介绍**

卡片的发送及更新，是由**集成&自动化**执行的。接下来围绕“团建意见收集”业务场景，来描述如何使用“集成&自动化”来实现该场景的。

## **业务场景**

有一个“团建意见收集”的表单，员工提交表单后，将表单填写的内容以卡片形式发送到群里。

其他员工在群中看到此卡片，可以点赞或者也提报团建意见。

**表单示例：**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482125.png)

**群中卡片示例：**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5521872871/p1084357.png)

## **操作步骤**

### **步骤一：集成&自动化**

1. **集成&自动化介绍**

   - **集成&自动化**：由**事件**触发执行的**业务编排/业务流程**。
   - **事件**：包括 “表单事件触发”、“卡片手动触发”、“定时触发” 等。
   - **业务编排/业务流程**：提供了编排业务逻辑的能力，如表单的增删改查、卡片的发送&更新、连接器等节点。

     如：提交“团建意见”表单后，发送卡片到群中 —— 这个场景中，提交表单是“事件”，发送卡片到群中是“业务流程”。

     关于集成&自动化，更多详情参见[集成自动化](https://www.yuque.com/yida/support/zevvr1)，本文档重点讲如何在集成&自动化中发送&更新卡片。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4737231661/p480484.png)
2. **集成&自动化入口**

   单击**集成&自动化，**再单击**新建集成&自动化**或者查看已创建的集成自动化。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482136.png)
3. **发送卡片的业务流程**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5521872871/p480490.png)

### **步骤二：表单事件触发**

**功能：**表单提交、表单更新、表单删除时，触发一段业务流程。

示例业务场景：有一个“团建意见收集”的表单，员工提交表单后，将表单填写的内容以卡片形式发送到群里。

1. 创建“表单事件触发”的集成自动化：单击**新建集成&自动化** > 填写**名称** > 选择表单**团建意见提报**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482186.png)
2. 进入业务流程的设计器，选择**表单事件触发 > 选择触发事件 >**单击**保存**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482188.png)
3. 增加**发送卡片**节点。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482189.png)
4. 配置**发送卡片**节点信息，包括**选择卡片 > 配置卡片内容 > 属性配置**这 3 个步骤。

   ![iShot2022-08-29_09](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482196.png)

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482201.png)

### **步骤三：卡片手动触发**

**功能：**卡片上的按钮被点击后，触发的一段业务流程。

示例业务场景：员工在群中看到团建意见卡片，点击“点赞”按钮进行点赞+1。

1. 创建**卡片手动触发**的集成自动化：单击**新建 > 填写名称 > 选择表单“团建意见提报”**。

   选择表单的原则：卡片是由**表单事件触发**的业务编排发出来的，那么**卡片手动触发**选择的表单要与**表单事件触发**时的选择**表单保持一致**，即保持同样的卡片上下文。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3737231661/p480502.png)

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482208.png)
2. 进入业务流程的设计器，增加**获取单条数据**节点，筛选出接下来要更新点赞量的团建意见数据。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482219.png)
3. 增加**更新数据**节点，更新上一步中**获取单条数据**节点中筛选出来的团建意见的点赞量。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482222.png)
4. 增加**更新卡片**，将群中对应的卡片上的点赞量更新为最新值。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482224.png)

### **步骤四：发送卡片节点配置**

本节点重点描述卡片节点的配置，注意是配置而不是设计，设计请参考[酷卡片设计](0053-yida-cool-card-design.md)文档。

卡片的三要素：**样式**、**数据**、**按钮/链接**，所以卡片节点的配置也围绕着这三要素进行。

配置流程：

1. **选择要发送/更新的卡片**

   可以选择官方提供的卡片模板，也可以选择自定义卡片模板。 选择后点击“打开卡片预览”可以预览卡片样式。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482226.png)
2. **将数据绑定到卡片上**

   将业务流程中各个节点获取到的数据，绑定到卡片上对应的数据变量上。（卡片三要素：样式、数据变量、按钮/链接）。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482228.png)
3. **配置卡片按钮/链接的动作行为**

   卡片的按钮可以绑定业务流程，也可以绑定链接。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482230.png)

   在设计卡片时，按钮的点击可以对应不同的事件类型，一般选择**自定义动作**或者**链接跳转**。

   **自定义动作：**可以绑定**卡片手动触发**的业务流程，点击时会执行对应的业务流程。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482234.png)

   **链接跳转：**点击时打开对应的链接，链接的值可以是固定值（在设计卡片时填写），也可以是变量（在集成&自动化的卡片节点中配置）。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482236.png)
4. **确定发送范围及规则**

   - 卡片发送范围：可以发送到人或者发送群

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3737231661/p480522.png)

     其中群可以配置为“当前群”。
   - “当前群”：群中安装酷应用后，通过群中的表单链接提交表单数据，配置“当前群”，即可以发送到表单被提交时所在的群中。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482239.png)
   - 卡片发送规则：

     场景1：每提交一条表单数据发送一张卡片，则选择“表单实例ID”字段即可。

     场景2：每天提交的表单数据，都只发一张卡片，那么可以选择代表当天日期的字段。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193471661/p482240.png)

### **步骤五：更新卡片节点配置**

卡片有一个特性：卡片内容可以被更新，这是与普通的消息的区别，可以避免群中被刷屏。

更新卡片配置流程：

1. 选择要更新的卡片。
2. 确定卡片更新规则。
3. 配置要更新的数据。

关键点：

1. 卡片被更新前要先被发送。
2. “**卡片更新规则**”中配置的字段，要与**卡片发送节点**中配置的“**卡片发送规则**”字段一致，才可正确更新到对应卡片。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4737231661/p480529.png)

## **搭建教程**

[](https://cloud.video.taobao.com/play/u/null/p/1/e/6/t/1/d/ud/374788831146.mp4)
