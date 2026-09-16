---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/overview-card"
namespace: "development"
slug: "overview-card"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 互动卡片 > 概述"
doc_id: "6KgBcc70C0"
updated_at: "2026-07-14 09:09:12"
---

> Source: https://open.dingtalk.com/document/development/overview-card
> Path: 应用开发 / 服务端 API / 即时通信 > 互动卡片 > 概述
> Updated: 2026-07-14 09:09:12

# 概述

本文介绍钉钉互动卡片是什么，以及它所具备的特点和所适用的场景。

## **什么是互动卡片**

钉钉互动卡片是一种即时交互、多人协同、数据驱动的轻量卡片，它能够将原本复杂的应用解构成一个个轻量级的卡片在钉钉的各个场域（场域的解释请参考下文名词解释部分）上运行。用户可以在卡片上完成互动协同，提高用户的沟通效率，同时帮助业务更好地触达用户。

### **卡片特性**

- **数据驱动**

  钉钉的互动卡片由模板和数据组成，数据决定了卡片的内容。在正常情况下，开发者只需要搭建一次卡片模板，后续只需要通过数据来驱动不同的卡片样式和内容即可。

  ![互动卡片介绍](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2531993871/p548957.png)

  卡片的数据还具备另外一个特点，即卡片数据具备动态性。普通的文本消息一旦发送出去，内容就无法变更，而互动卡片凭借灵活的数据驱动能力，能够让开发者自由地更新卡片上的数据，让卡片内容“动”起来。

  ![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3536989661/p520572.gif)
- **即时交互、多人协同**

  传统的消息都是静态的，更多的是作为内容的载体。而互动卡片除了可以展示丰富的内容之外，还支持让用户在卡片上进行轻量级的交互，交互的结果实时在卡片上同步显示。这意味着卡片不仅作为内容的载体，还是一个可操作可互动的轻量级应用，用户从此不再需要打开额外的页面去完成操作，直接在钉钉聊天窗口即可完成所有操作。

  ![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3536989661/p521274.gif)

  同时互动卡片还具备多人协同的能力，同一个卡片状态变更会实时同步，如下方的审批卡片，当审批员在互动卡片上完成审批的操作之后，发起审批的用户在卡片上即可看到最新的审批通过状态。

  ![ezgif-2-ce0aac35aa](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3536989661/p522208.gif)
- **多场域运行**

  钉钉互动卡片最常见于聊天窗口中，通常以卡片消息的方式与大家见面。但其实互动卡片不仅仅可以在聊天中运行，它还可以运行在其他场景。

  如下图，消息互动卡片和群吊顶互动卡片均是由同一个互动卡片模板所创建的。吊顶上的互动卡片拥有消息互动卡片消息的所有能力，但吊顶上的互动卡片尺寸是固定的。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2531993871/p522406.png)

### **应用场景**

钉钉互动卡片由于其丰富的样式能力以及交互能力，能够实现非常强大的功能。以下是部分典型的应用场景：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2531993871/p522340.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2531993871/p522341.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2531993871/p522342.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2531993871/p522343.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2531993871/p522344.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2531993871/p522345.png)

### **卡片类型**

钉钉互动卡片的类型包括：消息卡片、标准卡片、吊顶卡片、通讯录卡片以及工作台卡片等，是在创建卡片模板时所确定的，不同的类型的卡片适用于不同的业务场景，卡片的能力和样式也有所差异。

- **消息卡片**

  消息卡片是钉钉互动卡片最常见的类型，其以聊天消息的形式出现在群聊或者单聊中，提供多端一致的信息展示与协同交互能力，拥有最丰富的组件和能力。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5382992761/p526933.png)
- **标准卡片**

  标准卡片是钉钉通用的卡片类型，会针对不同的投放场景进行能力与样式的自适应，确保同一个卡片模板在聊天消息、群聊吊顶、协作、工作台等场景中拥有一致的使用体验，但是相对消息卡片来说组件较少、样式较少。如果开发者有跨场景同时投放互动卡片需求，则需要使用标准卡片模板进行卡片搭建。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5382992761/p526931.png)
- **吊顶卡片**

  吊顶卡片以置顶消息的形式出现在群聊中，它拥有互动卡片的所有能力，但尺寸是固定的，可以用于承载数据看板、公告通知类的信息。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5382992761/p526934.png)
- **通讯录卡片**

  通讯录卡片可以由组织管理员配置，作为插件的形式插入到企业员工个人的 Profile 中，为员工提供便捷的数据展示或访问入口。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2531993871/p536208.png)
- **工作台卡片**

  工作台卡片是一种特殊的卡片类型，专用于工作台插件的开发，开发者可以使用工作台卡片快速搭建并发布工作台插件。更多内容请参考[自建工作台卡片的创建和使用](../../08-工作台/02-Qzb8Lpee2t-使用教程/0006-add-self-built-interactive-cards-to-the-workbench.md)。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5382992761/p526935.png)

## **开放概览**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建卡片](0780-interface-for-creating-a-card-instance.md) | 调用本接口创建卡片实例，可以设置卡片的基本数据、设置动态数据源、卡片所在场域等内容。 | 新版 |
| [投放卡片](0781-delivery-card-interface.md) | 调用本接口实现多个指定场域的卡片投放。 | 新版 |
| [更新卡片](0782-interactive-card-update-interface.md) | 调用本接口实现更新卡片。 | 新版 |
| [创建并投放卡片](0783-create-and-deliver-cards.md) | 调用本接口，可以创建卡片实例，并将卡片投放至多个指定场域。 | 新版 |
| [关闭吊顶卡片](0784-api-closetopcard.md) | 调用本接口可关闭通过卡片投放接口投放的吊顶卡片。 | 新版 |
| [AI卡片流式更新](0785-api-streamingupdate.md) | 通过本接口持续更新的内容，在客户端会呈现一种打字机效果。 | 新版 |
| [注册卡片回调地址](0786-register-card-callback-address.md) | 调用本接口注册卡片回调地址。 | 新版 |
| [新增或者更新卡片的场域信息](0787-add-field-interface.md) | 调用本接口新增或者更新卡片实例的场域信息。 | 新版 |
| [卡片平台模板复制](0788-api-copytemplate.md) | 调用本接口，根据模板ID复制模板。 | 新版 |

## **使用教程**

我们以视频的形式，系统性地讲解了互动卡片的基本使用方法，包含如何创建卡片模板、如何使用卡片变量，如何投放与更新卡片。同时，我们基于一个实际的业务诉求，介绍了卡片模板的一些实用搭建技巧，以及如何通过绑定卡片事件来实现卡片的互动。

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20240724/nbbavo/%E3%80%90%E5%8D%A1%E7%89%87%E5%9F%BA%E7%A1%80%E8%83%BD%E5%8A%9B%E6%95%99%E7%A8%8B%E3%80%91%EF%BC%88%E5%85%A8%EF%BC%89.mov)

## **名词解释**

| **名词** | **说明** | **相关链接** |
| --- | --- | --- |
| 互动卡片 | 一种即时交互、多人协同，数据驱动的轻量卡片 | 无 |
| 搭建平台 | 卡片提供的低代码搭建平台，通过该平台可进行卡片的模板搭建、管理，卡片实例创建以及投放操作 | [卡片搭建平台](https://open-dev.dingtalk.com/fe/card) |
| 卡片模板 | 通过搭建平台创建的卡片模板样式，一个模板包含了一组卡片的布局、组件、变量的集合 | [普通卡片模板](../../05-互动卡片/01-N4KJ5HbqnQ-开发指南/0001-card-template-building-and-publishing.md) |
| 卡片实例化 | 通过模板和模板中每个变量对应的数据做映射绑定，生成的产物即为卡片实例，基于卡片实例可以做后续的行为，例如绑定动态数据源，卡片投放，卡片数据更新，多端多人互动交互，事件回调等操作 | - [卡片平台创建卡片实例](../../05-互动卡片/01-N4KJ5HbqnQ-开发指南/0003-create-a-card-instance-from-the-card-platform.md) - [开放接口创建卡片实例](../../05-互动卡片/01-N4KJ5HbqnQ-开发指南/0004-open-the-interface-to-create-a-card-instance.md) - [创建卡片](0780-interface-for-creating-a-card-instance.md) |
| 卡片投放 | 通过搭建平台或者卡片提供的开放接口将卡片实例面向钉钉的开放场域进行投递发送行为，例如在钉钉群聊场域中发送一个卡片消息，面向协作场域中投递一个待办的卡片 | - [卡片平台投放卡片实例](../../05-互动卡片/01-N4KJ5HbqnQ-开发指南/0005-card-delivery-instance-for-card-platform.md) - [开放接口投放卡片实例](../../05-互动卡片/01-N4KJ5HbqnQ-开发指南/0006-open-interface-card-delivery-instance.md) - [投放卡片](0781-delivery-card-interface.md) |
| 卡片更新 | 通过卡片提供的开放接口更新已经投放的卡片上的数据。 | [更新卡片](0782-interactive-card-update-interface.md) |
| 事件回调 | 通过卡片提供的开放接口注册回调地址，当卡片发生互动行为或者需要回源到业务拉取数据时，通过注册的回调地址请求到业务服务，进行相应的动作 | [事件回调](../../05-互动卡片/01-N4KJ5HbqnQ-开发指南/0007-event-callback-card.md) |
| 动态数据源 | 卡片提供的一种渲染时业务数据同步策略，当业务卡片在用户端上上屏时，通过卡片绑定的动态数据源配置，实时发起动态数据请求到业务侧做数据拉取，将业务返回的数据同步渲染到卡片对应的动态数据源字段，增强业务数据到卡片渲染的及时性，实现千人千面的卡片数据展示效果 | [动态数据源](../../05-互动卡片/01-N4KJ5HbqnQ-开发指南/0008-dynamic-data-source.md) |
| 卡片鉴权 | 基于酷应用创建的卡片支持酷应用鉴权，当卡片实例化过程中开启鉴权，在用户端侧卡片数据获取渲染之前可以做酷应用的可用性有效性的鉴权，如果卡片对应的酷应用已下架或已退订，卡片的实例将无法获取以及后续操作 | image |
| 场域 | 基于钉钉产品功能的人和事的协同场，例如个人 Profile、群聊、单聊等 | 无 |
