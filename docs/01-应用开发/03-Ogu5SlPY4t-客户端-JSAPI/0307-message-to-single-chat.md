---
title: "用户身份发送卡片消息到单聊"
source_url: "https://open.dingtalk.com/document/development/message-to-single-chat"
namespace: "development"
slug: "message-to-single-chat"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 用户身份发送卡片消息到单聊"
doc_id: "5BqfMOFhG6"
updated_at: "2026-09-01 09:15:50"
---

> Source: https://open.dingtalk.com/document/development/message-to-single-chat
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 用户身份发送卡片消息到单聊
> Updated: 2026-09-01 09:15:50

# 用户身份发送卡片消息到单聊

该文档向开发者提供以当前用户的身份将卡片消息发送到指定单聊的能力，可以通过调用sendMessageToSingleChat的JSAPI会唤起发送消息到单聊的确定弹窗，用户点击确定后就可以将卡片消息到指定单聊。

> **[!IMPORTANT]**
>
> Android端、iOS端、PC端不同系统展示结果可能会出现差别，请以最终的展示效果为准。

## 效果示例

### 发送消息

![单聊发送消息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0535228871/p578403.png)

### 发送成功

![单聊发送成功](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0535228871/p578404.png)

## 准备工作

1. 用户身份发送卡片消息到单聊的JSAPI需依赖[dingtalk-jsapi](https://www.npmjs.com/package/dingtalk-jsapi)，请先升级到最新版本的[dingtalk-jsapi](https://www.npmjs.com/package/dingtalk-jsapi)版本。

```
npm i dingtalk-jsapi@2.15.0 -S
```

## API使用说明

> **[!IMPORTANT]**
>
> 钉钉版本≥6.3.35 支持此功能，请注意钉钉版本。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持 |

```
import 'dingtalk-jsapi/entry/union';
import { sendMessageToSingleChat } from 'dingtalk-jsapi/plugin/coolAppSdk';

sendMessageToSingleChat({
  context: {
    clientId: 'dingmpixxxxxxx',
    corpId: 'ding16xxxxxxxxxx', // 根据对应场景获取 corpId
  },
  userIdList: ["manxxxxxx75"],
  sendCardRequest: {
    cardData: {
      cardParamMap: {
        title: "xxxxx",
        approval: "测试",
        type: "测试",
        amount: "1000元",
        reason: "北京出差",
        agree: "同意",
        disagree: "拒绝"
      }
    },
    cardTemplateId: "44ed1b33-xxxx-xxxx-xxxx-a552d42f0104",
    outTrackId: "xxxxxxxxxx"
  }
}).then(m => {
  console.log('测试' + JSON.stringify(m))
  if (res.errorCode === '0') {
    console.log('获取成功：' + JSON.stringify(res.detail))
  }
}).catch(e => {
  console.log('失败' + JSON.stringify(e))
});
```

## 参数说明

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| context | Object | 是 | 应用相关身份标识。 |
| context.clientId | String | 是 | 应用标识。   - 企业内部应用，传clientId。  **[!NOTE]**  如何获取Appkey，请参见[Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。 - 第三方企业应用，传SuiteKey。  **[!NOTE]**  如何获取Appkey，请参见[基础概念-SuiteKey](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。 |
| context.corpId | String | 是 | 企业CorpId。  **[!NOTE]**   - 小程序可通过[dd.corpId](0476-dd-corpid.md)获取。 - 微应用可通过[获取企业CorpId](0715-obtain-enterprise-corpid.md)获取。 |
| userIdList | String[] | 是 | 需要发送消息的单聊人员userId列表。 |
| sendCardRequest | Object | 是 | 动态卡片的相关数据。 |
| sendCardRequest.cardTemplateId | String | 是 | 互动卡片的消息模板ID。可通过[卡片平台](https://open-dev.dingtalk.com/fe/card)获取模板ID。image |
| sendCardRequest.outTrackId | String | 是 | 唯一标示卡片的外部编码。  **[!NOTE]**  发送不同的卡片内容，需要使用不同的outTrackId。 |
| sendCardRequest.cardData | Object | 是 | 卡片数据。详情参见[发送钉钉互动卡片（高级版）](../02-4a8AMF6u2A-服务端-API/1478-send-interactive-dynamic-cards-1.md)cardData字段。 |

## 返回结果

### 成功

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errorCode | String | 响应码：   - **0**： 表示安装成功 - **500**：表示获取应用信息失败 - **1000**：表示部分群发送失败 - **1001**：表示数据量过大导致传输错误 |
| errorMessage | String | 异常说明。  **[!NOTE]**  安装成功时，该字段返回空字符串。 |
| detail | Object | 安装成功的相关信息。 |
| detail.success | Boolean | 是否全部发送成功。 |
| detail.result | Array | 发送结果。 |
| detail.result[].openConversationId | String | 需要发送消息的单聊人员userId列表。 |
| detail.result[].success | Boolean | 该单聊卡片消息是否发送成功。 |

### 失败

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| errorCode | - String - Number（IOS由于实现问题，会返回数字类型） | 错误码：   - 22：表示页面被用户手动关闭。 - 7：表示当前钉钉版本较低，不支持该API，需要升级至最新版本的钉钉。   **[!IMPORTANT]**  由于实现问题，部分  旧版本  客户端不支持该API会返回"1"、"404"等状态码，需要去升级钉钉客户端。 |
| errorMessage | String | 错误说明：   - Close：表示被用户手动关闭。 - API not exists：表示当前钉钉版本较低，不支持该API，需要升级至最新版本的钉钉。 |

## 错误码

> **[!NOTE]**
>
> 当调用失败时，IOS由于实现问题，会返回数字类型。其他情况返回String类型。

| 参数 | 说明 |
| --- | --- |
| 22 | 表示页面被用户手动关闭。 |
| 7 | 表示当前钉钉版本较低，不支持该API，需要升级至最新版本的钉钉。 |
