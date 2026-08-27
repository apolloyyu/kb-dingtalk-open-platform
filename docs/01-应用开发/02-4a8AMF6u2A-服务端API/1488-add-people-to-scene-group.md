---
title: "新增群成员"
source_url: "https://open.dingtalk.com/document/development/add-people-to-scene-group"
namespace: "development"
slug: "add-people-to-scene-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 会话管理 > 场景群 > 新增群成员"
doc_id: "CNYIgjCmoD"
updated_at: "2026-08-25 09:37:17"
---

> Source: https://open.dingtalk.com/document/development/add-people-to-scene-group
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 即时通信 > 会话管理 > 场景群 > 新增群成员
> Updated: 2026-08-25 09:37:17

# 新增群成员

调用本接口，向群内新增群成员（群成员人数上限1000），适用于企业需要批量添加成员到群聊的场景，如项目组扩充人员、活动组织新增参与者等。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[添加场景群成员](0749-api-addscenegroupmember.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/im/chat/scenegroup/member/add`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1b\*\*\*\*\* | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| open\_conversation\_id | String | 是 | cid9FTRQSLo+sK\*\*\*\*\* | 群ID，调用[创建群](1486-create-a-scene-group-v2.md)接口获取`open_conversation_id`参数值。 |
| user\_ids | String | 是 | manager35\*\*\*\*\*,013\*\*\*\*\* | 批量增加的成员userid。  **[!NOTE]**  多个userid之间使用英文逗号分隔，最多传100个。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 847jlh2xqf6x | 请求ID，标识唯一的一次请求。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/im/chat/scenegroup/member/add?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "user_ids":"manager35*****,013*****",
        "open_conversation_id":"cid9FTRQSLo+sK*****"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scenegroup/member/add");
OapiImChatScenegroupMemberAddRequest req = new OapiImChatScenegroupMemberAddRequest();
req.setOpenConversationId("cid9FTRQSLo+sK*****");
req.setUserIds("manager35*****,013*****");
OapiImChatScenegroupMemberAddResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "success":true,
        "errmsg":"ok",
        "request_id": "847jlh2xqf6x"
}
```

## 错误码

| 错误码（errorcode） | 错误信息描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40035 | 不合法的参数 | 请确认群ID填写是否正确，user\_ids为非空 |
| 400020 | 没有访问权限 | 请在调用[创建群](https://open.dingtalk.com/document/orgapp/create-a-scene-group-v2)接口后，延迟几秒再调用本接口 |
| 400020 | 没有访问权限 | 请确认access\_token所属企业与群所属企业是否一致 |
| 400001 | 系统错误 | 请稍后重试 |
| 660041 | 员工不存在 | 请确认user\_ids是否填写正确 |
