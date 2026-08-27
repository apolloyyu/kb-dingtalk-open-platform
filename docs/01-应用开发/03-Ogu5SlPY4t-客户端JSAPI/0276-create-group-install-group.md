---
title: "创建群聊并安装酷应用入群"
source_url: "https://open.dingtalk.com/document/development/create-group-install-group"
namespace: "development"
slug: "create-group-install-group"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "酷应用 > 群聊酷应用 > 创建群聊并安装酷应用入群"
doc_id: "EQAyQpOkfD"
updated_at: "2025-08-27 18:09:14"
---

> Source: https://open.dingtalk.com/document/development/create-group-install-group
> Path: 应用开发 / 客户端JSAPI / 酷应用 > 群聊酷应用 > 创建群聊并安装酷应用入群
> Updated: 2025-08-27 18:09:14

# 创建群聊并安装酷应用入群

本文档介绍了提供将酷应用安装至群聊会话的能力。调用createGroupJSAPI的JSAPI会唤起创建群会话弹窗，您可以指定人员创建群会话并将酷应用安装至群会话。

> **[!IMPORTANT]**
>
> Android端、iOS端、PC端不同系统展示结果可能会出现差别，请以最终的展示效果为准。

## 效果示例

![创建群会话并安装酷应用入群](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5922804561/p445901.png)

## 准备工作

1. 完成酷应用开发，详情参见[群聊酷应用](https://open.dingtalk.com/document/orgapp/group-chat-cool-app-overview#cfb54a7056ygl)。
2. 酷应用入群JSAPI需依赖[dingtalk-jsapi](https://www.npmjs.com/package/dingtalk-jsapi)，请先升级到最新版本的[dingtalk-jsapi](https://www.npmjs.com/package/dingtalk-jsapi)版本。

```
npm i dingtalk-jsapi@2.13.100-alpha.11 -S
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
import { createGroup } from 'dingtalk-jsapi/plugin/coolAppSdk';

createGroup({
 context: {
   coolAppCode: 'xxx',
   clientId: 'yyy',
   corpId: 'zzz', // 根据对应场景获取 corpId
  },
  title: '测试',
  memberUserIds: ['userId1', 'userId2'],
  managementOptions: {
   validationType: 1,
    mentionAllAuthority: 1
  },
})
.then(res => {
  if (res.errorCode === '0') {
    // 建群成功
  }
}).catch(e => {
  // 用户主动退出安装
});
```

## 参数说明

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| context | Object | 是 | 酷应用相关身份标识。 |
| context.coolAppCode | String | 是 | 需要安装的酷应用的编码。通过以下方式获取：酷应用入群-获取酷应用编码 |
| context.clientId | String | 是 | 应用标识。   - 企业内部应用，传Appkey。   **[!NOTE]**  如何获取Appkey，请参见[基础概念-AppKey](https://open.dingtalk.com/document/orgapp/basic-concepts)。   - 第三方企业应用，传SuiteKey。   **[!NOTE]**  如何获取Appkey，请参见[基础概念-SuiteKey](https://open.dingtalk.com/document/orgapp/basic-concepts)。 |
| context.corpId | String | 是 | 企业CorpId，用于校验群所属企业，只能安装到该企业的内部群。  **[!NOTE]**  如何获取CorpId，请参见[基础概念-CorpId](https://open.dingtalk.com/document/orgapp/basic-concepts)。 |
| title | String | 是 | 群名称。 |
| memberUserIds | Array of String | 是 | 群成员的userId列表。 |
| managementOptions | Object | 否 | 群管理相关配置。 |
| managementOptions.validationType | Number | 否 | 入群需验证：   - 0：不入群验证（默认） - 1：入群验证 |
| managementOptions.mentionAllAuthority | Number | 否 | 仅群主和管理员可@全员：   - 0：默认所有人 - 1：仅群主可@全员 |

## 返回结果

### 成功

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errorCode | String | 响应码：   - 0：表示安装成功。 - 500：表示获取酷应用信息失败。 - 1000：表示创建群聊失败，常见场景为群成员开启了高管模式，具体信息可见detail字段。 |
| errorMessage | String | 异常说明。  **[!NOTE]**  安装成功时，该字段返回空字符串。 |
| detail | Object | 安装成功的相关信息。 |
| detail.openConversationId | String | 创建的群id。 |
| detail.success | Boolean | 是否创建成功 |
| detail.errorCode | String | 业务错误码。 |
| detail.errorMsg | String | 业务错误原因。 |

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

## 相关链接

酷应用接入流程更多详情请参考文档[群聊酷应用](https://open.dingtalk.com/document/orgapp/group-chat-cool-app-overview#cfb54a7056ygl)。
