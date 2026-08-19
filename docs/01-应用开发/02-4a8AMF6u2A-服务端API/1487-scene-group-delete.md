---
title: "删除群成员"
source_url: "https://open.dingtalk.com/document/development/scene-group-delete"
namespace: "development"
slug: "scene-group-delete"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 会话管理 > 场景群 > 删除群成员"
doc_id: "mxakLjLchG"
updated_at: "2026-05-13 15:50:35"
---

> Source: https://open.dingtalk.com/document/development/scene-group-delete
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 即时通信 > 会话管理 > 场景群 > 删除群成员
> Updated: 2026-05-13 15:50:35

# 删除群成员

调用本接口，根据群ID和群成员ID删除群成员，适用于企业需要批量移除群成员的场景，如员工离职、项目结束等。

> **[!IMPORTANT]**
>
> 当前接口已完成升级迭代且不再支持新应用申请，存量应用调用不受影响，建议未接入的开发者使用[删除群成员](0750-api-removescenegroupmember.md)接口，已接入的开发者结合实际尽快完成迁移。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | **[!IMPORTANT]**  不支持新增申请 | — |
| 第三方企业应用 | 否 | **[!IMPORTANT]**  不支持新增申请 | — |
| 第三方个人应用 | 否 | 暂不支持 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/im/chat/scenegroup/member/delete`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | be311\*\*\*\*\* | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| open\_conversation\_id | String | 是 | cid15\*\*\*\*\*== | 群ID，调用[创建群](1484-create-a-scene-group-v2.md)接口获取`open_conversation_id`参数值。 |
| user\_ids | String | 是 | manager35\*\*\*\*\*,013\*\*\*\*\* | 批量删除的成员userid。  **[!NOTE]**  多个userid之间使用英文逗号分隔，最多传100个。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 5pk47xj1k76k | 请求ID，标识唯一的一次请求。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/im/chat/scenegroup/member/delete?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "user_ids":"manager35*****,013*****",
        "open_conversation_id":"cid15*****=="
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scenegroup/member/delete");
OapiImChatScenegroupMemberDeleteRequest req = new OapiImChatScenegroupMemberDeleteRequest();
req.setOpenConversationId("cid15*****==");
req.setUserIds("manager35*****,013*****");
OapiImChatScenegroupMemberDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "errmsg": "ok",
        "success":true,
        "request_id": "5pk47xj1k76k"
}
```

## 错误码

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40035 | 无效的参数，群ID和user\_ids不能为空 | 请确认群ID填写是否正确，user\_ids为非空 |
| 400020 | 没有访问权限 | 请在调用[创建群](1484-create-a-scene-group-v2.md)接口后，延迟几秒再调用本接口 |
| 400020 | 没有访问权限 | 请确认access\_token所属企业与群所属企业是否一致 |
| 400001 | 系统错误 | 请稍后重试 |
