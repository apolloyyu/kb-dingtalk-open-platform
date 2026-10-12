---
title: "实现置顶卡片纯拉模式"
source_url: "https://open.dingtalk.com/document/development/pure-pull-mode-process-guide"
namespace: "development"
slug: "pure-pull-mode-process-guide"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 使用教程 > 实现置顶卡片纯拉模式"
doc_id: "NWW2WdGxK7"
updated_at: "2026-08-07 14:50:56"
---

> Source: https://open.dingtalk.com/document/development/pure-pull-mode-process-guide
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 使用教程 > 实现置顶卡片纯拉模式
> Updated: 2026-08-07 14:50:56

# 实现置顶卡片纯拉模式

本文介绍了互动卡片纯拉模式的概念与接入流程。

## 预期效果

- 置顶卡片纯拉模式

  每次打开会话时，都会回调开发者设置的callbackUrl地址去获取私有数据，并更新到卡片上。![p520631](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9071678661/p521595.png)
- 消息卡片纯拉模式

  每次打开会话拉取消息时，都会回调开发者设置的callbackUrl地址去获取私有数据，并更新到卡片上。![11111](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0882678661/p521687.png)

## 接入流程简介

本文档以开启纯拉模式的置顶卡片为例，展示了互动卡片纯拉模式的接入流程。

步骤一：创建互动卡片模板。

步骤二：注册互动卡片回调地址。

步骤三：创建并开启互动卡片置顶。

步骤四：更新卡片内容。

## 步骤一：创建互动卡片模板

登录[钉钉管理后台](https://oa.dingtalk.com/#/welcome)，[创建互动卡片消息模板](https://open-dev.dingtalk.com/fe/card?hash=%23%2F#/)获取**cardTemplateId**。

### 创建吊顶卡片类型模板

> **[!NOTE]**
>
> 设置卡片模板的内容，详情请参考文档[创建消息模板](../01-XOnnmGCTbn-开发指南/0095-create-a-message-template.md)。

![11111](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0724118561/p466977.png)

### 设置互动卡片私有变量

> **[!NOTE]**
>
> - 使用互动卡片实现用户与卡片的交互，详情请参考文档[开发互动卡片](../01-XOnnmGCTbn-开发指南/0048-develop-group-chat-coolapp-interactive-card.md)。
> - 纯拉模式只能拉取互动卡片消息模板中的私有变量对应的数据。

在卡片模板编辑器上，可以设置私有变量。![iShot2022-07-15_14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0724118561/p467139.png)![222](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0724118561/p467140.png)

### 保存或发布互动卡片

在卡片模板编辑器上，您可以通过不同的组件组合来实现您的业务需求。当卡片搭建完成之后，单击**保存**或**发布**后即可使用该卡片。![iShot2022-07-15_14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1724118561/p467137.png)

## 步骤二：注册互动卡片回调地址

卡片纯拉模式需调用接口[注册卡片回调地址](0786-register-card-callback-address.md)，获取参数**callbackRouteKey**。

## 步骤三：创建并开启互动卡片置顶

调用[创建并开启互动卡片吊顶](0761-send-group-helper-message.md)接口，实现开启卡片置顶。

> **[!NOTE]**
>
> 将参数**pullStrategy**设置为**true**，开启卡片纯拉模式。

## 步骤四：更新卡片内容

[响应互动卡片消息](../01-XOnnmGCTbn-开发指南/0098-responding-to-interactive-messages.md)，返回卡片私有数据，实现更新卡片内容。

> **[!NOTE]**
>
> 用户每次打开会话，都会回调开发者设置的callbackUrl地址去获取私有变量对应的数据；非私有变量对应的数据无法通过纯拉模式获取。

### 拉取私有数据

用户打开会话的行为，会通过HTTP post method 请求的形式回调给开发者注册的HTTP地址，来拉取私有数据。请求内容会以 contentType="application/json" 形式将如下参数传递给开发者。

> **[!NOTE]**
>
> 其中 content 字段包含了卡片中非私有数据的内容。

```
{
    "corpId": "dingXXXXXX",
    "outTrackId": "XXXXXX",
    "userId": "XXXXXX",
    "content": "{\"cardData\":{\"cardParamMap\":{\"xxx\":\"xxx\"}}}",
    ...
}
```

### 同步更新卡片私有数据

在纯拉模式下，您需要同步更新卡片的私有数据内容，那么您可以在接收到回调请求后，在该请求里面返回最新的卡片私有数据回去，这样就能实现用户每次看到卡片时，都能够获取到最新的私有数据。返回的具体卡片数据格式如下。

> **[!NOTE]**
>
> 不需要返回非私有变量对应的数据，即使返回，也不会更新卡片上非私有变量对应的数据。

```
{
 "outTrackId": "XXXXXX(用于更新卡片的唯一ID)",
 "cardOptions": {
  "updatePrivateDataByKey": true/false,
 },
 "userPrivateData": {
  "cardParamMap": {
   "key1": "value1",
   "key2": "value2",
   "变量N": "变量值N"
  },
  "cardMediaIdParamMap": {
   "image1": "mediaIdXXXXX1",
   "image2": "mediaIdXXXXX2"
  }
 }
}
```

### 置顶卡片纯拉模式实现效果

每次打开会话时，卡片效果如下图所示。![p520631](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9071678661/p521595.png)
