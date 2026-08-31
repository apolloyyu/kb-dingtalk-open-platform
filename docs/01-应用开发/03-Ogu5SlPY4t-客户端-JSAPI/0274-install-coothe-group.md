---
title: "安装酷应用入群"
source_url: "https://open.dingtalk.com/document/development/install-coothe-group"
namespace: "development"
slug: "install-coothe-group"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 群聊酷应用 > 安装酷应用入群"
doc_id: "FDyuY2grYp"
updated_at: "2026-08-28 10:26:18"
---

> Source: https://open.dingtalk.com/document/development/install-coothe-group
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 群聊酷应用 > 安装酷应用入群
> Updated: 2026-08-28 10:26:18

# 安装酷应用入群

本文档介绍了提供将酷应用安装至群聊会话的能力。调用installCoolAppToGroup的JSAPI会唤起将酷应用安装入群的弹窗，您可以指定需安装的酷应用，将酷应用安装至指定群聊。

> **[!IMPORTANT]**
>
> Android端、iOS端、PC端不同系统展示结果可能会出现差别，请以最终的展示效果为准。

## 效果示例

![添加群应用步骤](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2764501561/p434267.png)

## 准备工作

酷应用入群JSAPI需依赖[dingtalk-jsapi](https://www.npmjs.com/package/dingtalk-jsapi)，请先升级到最新版本的[dingtalk-jsapi](https://www.npmjs.com/package/dingtalk-jsapi)版本。

```
npm i dingtalk-jsapi@2.13.100-alpha.6 -S
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
import { installCoolAppToGroup } from 'dingtalk-jsapi/plugin/coolAppSdk';

installCoolAppToGroup({
  coolAppCode: 'xxx',
  clientId: 'yyy',
  corpId: 'zzz', // 根据对应场景获取 corpId
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
| coolAppCode | String | 是 | 需要安装的酷应用的编码。通过以下方式获取：三方群扩展 |
| clientId | String | 是 | 应用标识。   - 企业内部应用，传clientId。  **[!NOTE]**  如何获取Appkey，请参见[Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。 - 第三方企业应用，传SuiteKey。  **[!NOTE]**  如何获取Appkey，请参见[基础概念-SuiteKey](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。 |
| corpId | String | 是 | 企业CorpId，用于校验群所属企业，只能安装到该企业的内部群。  **[!NOTE]**   - 小程序通过[dd.corpId](0505-dd-corpid.md)获取。 - 微应用通过[获取企业CorpId](0747-obtain-enterprise-corpid.md)获取。 |

## 返回结果

### 成功

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errorCode | String | 响应码：   - **0**：表示安装成功。 - **22**：表示页面被用户点击取消关闭弹窗。 |
| errorMessage | String | 异常说明。  **[!NOTE]**  安装成功时，该字段返回空字符串。 |
| detail | Object | 安装成功的相关信息。 |
| detail.coolAppCode | String | 安装成功的酷应用编码。 |
| detail.openConversationId | String | 安装酷应用的群Id。 |
| detail.corpId | String | 企业标识，与入参指定的CorpId一致。 |

### 失败

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| errorCode | - String - Number（IOS由于实现问题，会返回数字类型） | 错误码：   - **22**：表示页面被用户手动关闭。 - **7**：表示当前钉钉版本较低，不支持该API，需要升级至最新版本的钉钉。 |
| errorMessage | String | 错误说明：   - **Close**：表示被用户手动关闭。 - **API not exists**：表示当前钉钉版本较低，不支持该API，需要升级至最新版本的钉钉。 |

## 错误码

> **[!NOTE]**
>
> 当调用失败时，IOS由于实现问题，会返回数字类型。其他情况返回String类型。

| 参数 | 说明 |
| --- | --- |
| 22 | 表示页面被用户手动关闭。 |
| 7 | 表示当前钉钉版本较低，不支持该API，需要升级至最新版本的钉钉。 |

## 相关链接

酷应用接入流程更多详情请参考文档[酷应用介绍](../01-XOnnmGCTbn-开发指南/0042-coolapp-overview.md)。

## **常见问题**

- **iOS下调用api无反应**

  如果调用通讯录选人组件后立刻调用此API，可能会不响应，需要在调用选人组件后加个延迟，等选人组件页面完全关闭后，再调用此API。
- **酷应用权限校验不通过**

  原因是酷应用跟clientId不匹配， 需要传入酷应用归属的主应用的clientId。

  - 企业内部应用，传clientId。

    > **[!NOTE]**
    >
    > 如何获取Appkey，请参见[Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。
  - 第三方企业应用，传SuiteKey。

    > **[!NOTE]**
    >
    > 如何获取Appkey，请参见[基础概念-SuiteKey](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。
