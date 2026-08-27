---
title: "添加群成员"
source_url: "https://open.dingtalk.com/document/development/add-group-members"
namespace: "development"
slug: "add-group-members"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "酷应用 > 群聊酷应用 > 添加群成员"
doc_id: "kioe4B39x1"
updated_at: "2025-10-09 18:07:46"
---

> Source: https://open.dingtalk.com/document/development/add-group-members
> Path: 应用开发 / 客户端JSAPI / 酷应用 > 群聊酷应用 > 添加群成员
> Updated: 2025-10-09 18:07:46

# 添加群成员

本文档向开发者提供将在群聊内添加群成员的能力，当酷应用被安装到群聊会话后，酷应用开发者可以通过调用addMember的JSAPI添加群成员入群，用户点击确定后就可以将群成员添加到指定群。

> **[!IMPORTANT]**
>
> Android端、iOS端、PC端不同系统展示结果可能会出现差别，请以最终的展示效果为准。

## 效果示例

![添加群成员](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9739615561/p449084.png)

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
import { addMembers } from 'dingtalk-jsapi/plugin/coolAppSdk';

addMembers({
      context: {
        coolAppCode: 'COOLAPP-1-10xxxxxxxxxxxD99000R',
        clientId: 'dingmpixxxxxxx',
        corpId: 'ding16xxxxxxxxxx', // 根据对应场景获取 corpId
      },
      openConversationList: ["cideJmxxxxxVK9yXLIEg=="],
      userIds: ['08521816421284272']
    })
    .then(res => {
      if (res.errorCode === '0') {
        console.log("添加成功"+ JSON.stringify(res))
      }
    }).catch(e => {
      console.log("添加失败"+ JSON.stringify(e))
});
```

## 参数说明

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| context | Object | 是 | 酷应用相关身份标识。 |
| context.coolAppCode | String | 是 | 需要安装的酷应用的编码。通过以下方式获取：酷应用入群-获取酷应用编码 |
| context.clientId | String | 是 | 应用标识。   - 企业内部应用，传Appkey。   **[!NOTE]**  如何获取Appkey，请参见[基础概念-AppKey](https://open.dingtalk.com/document/orgapp/basic-concepts)。   - 第三方企业应用，传SuiteKey。   **[!NOTE]**  如何获取Appkey，请参见[基础概念-SuiteKey](https://open.dingtalk.com/document/orgapp/basic-concepts)。 |
| context.corpId | String | 是 | 企业CorpId，用于校验群所属企业，只能安装到该企业的内部群。  **[!NOTE]**  如何获取CorpId，请参见[基础概念-CorpId](https://open.dingtalk.com/document/orgapp/basic-concepts)。 |
| openConversationList | Array of String | 是 | 要添加成员的的群ID。 |
| userIds | Array of String | 是 | 需要入群的成员userId。 |

## 返回结果

### 成功

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errorCode | String | 响应码：   - 0：表示安装成功。 - 失败原因有多种，具体见下方错误场景和对应的错误码 |
| errorMessage | String | 异常说明。  **[!NOTE]**  安装成功时，该字段返回空字符串。 |
| detail | Object | 入群的相关信息。 |
| detail[].success | String | 群添加成员的结果。 |
| detail[].errorCode | Boolean | 群添加成员失败的错误码。 |
| detail[].errorMsg | String | 群添加成员失败的错误信息。 |
| detail[].openConversationId | String | 群ID。 |
| detail[].failedUserIds | Array of String | 未成功入群的用户userId。  **[!NOTE]**  不包含不存在或已离职的用户userId。 |
| detail[].notExistUserIds | Array of String | 不存在或已离职的用户userId。 |

**错误场景**：

| 错误原因 | 错误码 | 错误信息 |
| --- | --- | --- |
| 系统异常 | -1 | 系统繁忙，请稍后再试。 |
| 多种原因导致部分成员添加失败 | 1000 | 部分成员添加失败。 |
| 未知错误 | 100001 | 系统繁忙，请稍后再试。 |
| 请求参数为空 | 200001 | 请求参数为空。 |
| 入参群数量超过上限 | 500048 | 群数量超过限制。 |
| 入参人数超过上限 | 500105 | 批量添加群成员数量超出限制。 |
| 校验群应用权限失败 | 500074 | 酷应用未授权给当前应用。 |
| 所有员工都不存在 | 500026 | 员工不存在。 |
| 群不存在 | 500053 | 群不存在。 |
| 群已解散 | 500097 | 群已解散。 |
| 群内未安装酷应用 | 500072 | 群内未安装酷应用。 |
| 群所属企业id一致校验失败 | 500089 | 群不属于当前企业。 |
| 群成员数量超过限制 | 500047 | 群成员数量超过限制。 |
| 群聊加人鉴权失败 | 500104 | 没有权限加人入群。 |
| 群内开启了入群许可，需要群主或管理员同意入群申请 | 500106 | 群开启了入群许可，成员邀请已发送。 |
| 用户开启高管模式且群内开启了入群许可，不允许加用户入群 | 4012059 | 处于勿扰模式，拒绝加入群聊，请先与TA建立好友关系。 |

### 失败

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| errorCode | - String - Number（IOS由于实现问题，会返回数字类型） | 错误码：   - 22：表示页面被用户手动关闭。 - 7：表示当前钉钉版本较低，不支持该API，需要升级至最新版本的钉钉。   **[!IMPORTANT]**  由于实现问题，部分旧版客户端不支持该API，会返回"1"、"404"等状态码，需要升级至最新版本的钉钉。 |
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
