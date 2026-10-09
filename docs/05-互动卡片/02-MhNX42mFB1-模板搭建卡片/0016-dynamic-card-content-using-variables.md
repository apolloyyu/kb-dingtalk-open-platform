---
title: "使用变量实现卡片内容的动态化"
source_url: "https://open.dingtalk.com/document/development/dynamic-card-content-using-variables"
namespace: "development"
slug: "dynamic-card-content-using-variables"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "搭建平台 > 使用教程 > 使用变量实现卡片内容的动态化"
doc_id: "ap6d1HCAZV"
updated_at: "2026-05-19 17:05:14"
---

> Source: https://open.dingtalk.com/document/development/dynamic-card-content-using-variables
> Path: 互动卡片 / 模板搭建卡片 / 搭建平台 > 使用教程 > 使用变量实现卡片内容的动态化
> Updated: 2026-05-19 17:05:14

# 使用变量实现卡片内容的动态化

本文基于一个数据看板卡片，讲解如何使用卡片变量来实现卡片内容的动态化。

## **步骤一：分析卡片中的动态内容**

我们的目的是实现一个数据看板，用户可以看到整个团队的数据概况，同时不同的用户可以在卡片上看到自己的数据，以及自己的数据在团队中的占比。

![20240818223204.jpg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9951286271/p837071.jpg)

可以看出，这张卡片中有三类动态数据，“团队完成任务总数”是所有用户共享的数据，用户昵称和“你完成的任务数”对于不同用户有所差异，“在团队中的占比”是由两个现有数据计算而来，我们在搭建中可以采用“普通变量”和“表达式变量”来实现类似诉求。

## **步骤二：创建卡片变量**

基于之前的分析，我们定义了“name”、“totalCount”、“selfCount”三个变量来分别对应“昵称”、“团队数据”和“个人数据”，同时对于非共享数据，我们开启了“私有”属性。

“私有变量”也是普通变量，其区别在于投放卡片时，可以面向不同的用户指定不同的数据，该数据仅对应的用户自己可见。私有变量的优先级高于公有变量，在卡片渲染时，如果在私有数据中获取不到变量对应的值时，会尝试去公有数据中获取。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9951286271/p837074.png)

“在团队中的占比”数据可以通过现有数据计算得出，在这里我们定义一个表达式变量来实现。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9951286271/p837075.png)

我们预置了一系列丰富的表达式运算能力，具体有哪些可用的表达式，可以通过点击“使用文档”来查看。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9951286271/p837076.png)

## **步骤三：绑定卡片变量**

我们在Mock数据面板为这些变量设置Mock数据。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9951286271/p837077.png)

接下来，我们为卡片中所有的动态内容绑定对应的变量，即可在搭建器中实时看到卡片的渲染结果。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9951286271/p837078.png)

保存成功后，即可通过调用开放接口进行卡片的创建与投放。需要特别注意的一点是，在卡片模板调试完成并准备上线前，我们强烈建议点击“发布”按钮对模板进行锁定，避免协作开发者意外修改卡片模板，从而引起线上故障。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9951286271/p837079.png)

## **步骤四：投放卡片**

我们需要调用开放接口实现“创建并投放卡片”与“更新卡片”功能，具体接口的使用方法可以参考开放平台接口文档，文档路径目前位于“服务端API / 互动卡片”目录下。你也可以直接点击卡片搭建器中的文档入口，快速跳转到对应文档。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9951286271/p837080.png)

这里，我们的卡片投放演示采用群机器人为载体，利用机器人消息的能力来触发卡片的投放与更新。群机器人的相关操作我们的演示中不做涉及，如果希望了解更多信息，可以查阅具体的文档。

我们在机器人的消息监听函数中，监听send信息。当机器人收到“send”信息时，我们根据之前模板内定义的变量，分别配置公有数据与私有数据。私有数据中的两个ID是我们测试群中两个用户的 UserID，我们为他们分别指定了两个不同的私有数据。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9951286271/p837082.png)

接下来，我们来看一下卡片的实际投放效果。我们在测试组织中添加两个不同的用户。然后通过发送send消息给机器人，触发机器人的卡片推送。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9951286271/p837085.png)

我们可以看到，机器人在群内推送了我们刚才搭建的那张卡片。如我们预期，两位用户分别看到了专属于自己的数据卡片。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9951286271/p837086.png)

## 步骤五：更新卡片

我们在机器人的消息监听函数中，监听update信息。当机器人收到“update”消息时，我们给第二位用户更新了他的私有数据，同时更新了公有数据中的数据总量。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9951286271/p837084.png)

接下来，我们通过发送update消息给机器人，触发机器人的卡片更新操作。如我们预期，卡片数据同步发生了变化。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9951286271/p837087.png)

## **视频演示**

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20240920/ftuzym/%E4%BD%BF%E7%94%A8%E5%8F%98%E9%87%8F%E5%AE%9E%E7%8E%B0%E5%8D%A1%E7%89%87%E5%86%85%E5%AE%B9%E7%9A%84%E5%8A%A8%E6%80%81%E5%8C%96.mp4)
