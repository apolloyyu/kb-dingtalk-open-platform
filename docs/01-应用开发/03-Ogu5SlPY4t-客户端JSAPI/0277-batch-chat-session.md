---
title: "批量安装酷应用到单聊会话"
source_url: "https://open.dingtalk.com/document/development/batch-chat-session"
namespace: "development"
slug: "batch-chat-session"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "酷应用 > 单聊酷应用 > 批量安装酷应用到单聊会话"
doc_id: "T0F5syOrBE"
updated_at: "2025-08-27 18:09:16"
---

> Source: https://open.dingtalk.com/document/development/batch-chat-session
> Path: 应用开发 / 客户端JSAPI / 酷应用 > 单聊酷应用 > 批量安装酷应用到单聊会话
> Updated: 2025-08-27 18:09:16

# 批量安装酷应用到单聊会话

本文档介绍了提供将酷应用安装至单聊会话的能力。调用batchInstallCoolApp的JSAPI会唤起将酷应用安装至单聊会话的弹窗，您可以指定需安装的酷应用，将酷应用安装至指定单聊会话。

> **[!IMPORTANT]**
>
> Android端、iOS端、PC端不同系统展示结果可能会出现差别，请以最终的展示效果为准。

## 效果示例

![安装酷应用到单聊](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4653838561/p468337.png)

## 准备工作

1. 批量安装酷应用到单聊会话的JSAPI需依赖[dingtalk-jsapi](https://www.npmjs.com/package/dingtalk-jsapi)，请先升级到最新版本的[dingtalk-jsapi](https://www.npmjs.com/package/dingtalk-jsapi)版本。

```
npm i dingtalk-jsapi@2.15.0 -S
```

## API使用说明

> **[!IMPORTANT]**
>
> - 钉钉版本≥6.3.35 支持此功能，请注意钉钉版本。
> - 单聊酷应用不支持安装到自己的单聊会话。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持 |

```
import 'dingtalk-jsapi/entry/union';
import { batchInstallCoolApp } from 'dingtalk-jsapi/plugin/coolAppSdk';

batchInstallCoolApp({
  coolAppCode: 'xxx',
  clientId: 'yyy',
  corpId: 'zzz', // 根据对应场景获取 corpId
  isSingleChat: true,
}).then(res => {
  if (res.errorCode === '0') {
    // 安装成功
  }
}).catch(e => {
  // 用户主动退出安装
});
```

## 参数说明

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| coolAppCode | String | 是 | 需要安装的酷应用的编码。通过以下方式获取：第三方企业应用coolAppCode |
| clientId | String | 是 | 应用标识。   - 企业内部应用，传Appkey。   **[!NOTE]**  如何获取Appkey，请参见[基础概念-AppKey](https://open.dingtalk.com/document/orgapp/basic-concepts)。   - 第三方企业应用，传SuiteKey。   **[!NOTE]**  如何获取Appkey，请参见[基础概念-SuiteKey](https://open.dingtalk.com/document/orgapp/basic-concepts)。 |
| corpId | String | 是 | 企业CorpId，用于校验人员所属主企业。 |
| isSingleChat | Boolean | 是 | 指定安装到群聊还是单聊：   - **true**：单聊 - **false**：群聊 |

## 返回结果

### 成功

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errorCode | String | 响应码：   - 0：表示安装成功。 - 22：表示页面被用户点击取消关闭弹窗。 |
| errorMessage | String | 异常说明。  **[!NOTE]**  安装成功时，该字段返回空字符串。 |
| detail | Object | 安装成功的相关信息。 |
| detail.success | Boolean | 是否全部安装成功。 |
| detail.coolAppBatchInstallDetailList | Array | 酷应用安装结果。 |
| detail.coolAppBatchInstallDetailList[].openConversationId | String | 安装酷应用单聊会话的Id。 |
| detail.coolAppBatchInstallDetailList[].success | Boolean | 是否安装成功。 |

### 失败

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| errorCode | - String - Number（IOS由于实现问题，会返回数字类型） | 错误码：   - 22：表示页面被用户手动关闭。 - 7：表示当前钉钉版本较低，不支持该API，需要升级至最新版本的钉钉。 |
| errorMessage | String | 错误说明：   - Close：表示被用户手动关闭。 - API not exists：表示当前钉钉版本较低，不支持该API，需要升级至最新版本的钉钉。 |

## 错误码

> **[!NOTE]**
>
> 当调用失败时，IOS由于实现问题，会返回数字类型。其他情况返回String类型。

| 参数 | 说明 |
| --- | --- |
| 22 | 表示页面被用户手动关闭。 |
| 7 | 表示当前钉钉版本较低，不支持该API，需要升级至最新版本的钉钉。 |
