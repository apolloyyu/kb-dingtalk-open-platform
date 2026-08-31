---
title: "创建群"
source_url: "https://open.dingtalk.com/document/development/session-management-creates-groups"
namespace: "development"
slug: "session-management-creates-groups"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 会话管理 > 群管理 > 创建群"
doc_id: "C6QxWxbnt6"
updated_at: "2026-08-25 09:37:13"
---

> Source: https://open.dingtalk.com/document/development/session-management-creates-groups
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 即时通信 > 会话管理 > 群管理 > 创建群
> Updated: 2026-08-25 09:37:13

# 创建群

调用本接口，创建内部群会话，适用于企业需要快速创建群聊的场景，如项目协作、活动组织等。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[创建群会话](0738-create-common-group-new-version-v2.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/chat/create`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| name | String | 是 | 全员群 | 群名称，长度限制为1~20个字符。 |
| owner | String | 是 | manager4220 | 群主的userId，可通过[根据手机号查询用户](0063-query-users-by-phone-number.md)接口获取userid参数值。  **[!NOTE]**  该员工必须为会话**useridlist**的成员之一。 |
| useridlist | String[] | 是 | ["userid1","userid2"] | 群成员列表，每次最多支持40人，群人数上限为1000。  可通过[根据手机号查询用户](0063-query-users-by-phone-number.md)接口获取userid参数值。 |
| showHistoryType | Number | 否 | 1 | 新成员是否可查看100条历史消息：   - **1**：可查看 - **0**：不可查看  **[!NOTE]**  如果不传值，代表不可查看。 |
| searchable | Number | 否 | 0 | 群是否可以被搜索：   - **0**（默认）：不可搜索 - **1**：可搜索 |
| validationType | Number | 否 | 0 | 入群是否需要验证：   - **0**（默认）：不验证 - **1**：入群验证 |
| mentionAllAuthority | Number | 否 | 0 | @all 使用范围：   - **0**（默认）：所有人可使用 - **1**：仅群主可@all |
| managementType | Number | 否 | 0 | 群管理类型：   - **0**（默认）：所有人可管理 - **1**：仅群主可管理 |
| chatBannedType | Number | 否 | 0 | 是否开启群禁言：   - **0**（默认）：不禁言 - **1**：全员禁言 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | cidL+NXxxxx+MSA== | 群会话的ID。 |
| chatid | String | chate39f540d572b71xxxx | 群会话的ID。  **[!IMPORTANT]**  后续版本中**chatid**将不再使用，请将**openConversationId**作为群会话唯一标识。 |
| conversationTag | Number | 2 | 会话类型：   - **2**：企业群。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/chat/create?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "name": "全员群",
    "owner": "manager4220",
    "useridlist": ["userid1", "userid2"],
    "showHistoryType":1,
    "searchable":0,
    "validationType":0,
    "mentionAllAuthority":0,
    "managementType":0,
    "chatBannedType":0
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/chat/create");
OapiChatCreateRequest req = new OapiChatCreateRequest();
req.setName("全员群");
req.setOwner("manager4220");
req.setUseridlist(Arrays.asList("userid1","userid2"));
req.setShowHistoryType(1L);
req.setSearchable(0L);
req.setValidationType(0L);
req.setMentionAllAuthority(0L);
req.setManagementType(0L);
req.setChatBannedType(0L);
OapiChatCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "chatid": "chatcf0675d404188xxxx",
    "openConversationId": "cidL+NXxxxx+MSA==",
    "conversationTag": 2
}
```

## 错误码

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 43007 | 需要授权 | 请确认access\_token是否正确 |
| 43009 | 参数需要是json格式 | 请使用json格式的参数 |
| 40031 | 无效的useridlist列表 | 请确认useridlist是否正确 |
| 40035 | 群名称不能为空 | 请填上群名称 |
| 400002 | 参数过长 | 请查看入参中长度限制 |
| 49013 | 群主不能为空 | 请填上群主的userid |
| 49010 | 群成员不能为空 | 请填入群成员 |
| 49011 | 群成员长度超限 | 请减少群成员 |
| 1002 | 组织建群超出上限 | 建议使用会话2.0建群API，API地址：[创建群](1486-create-a-scene-group-v2.md)。 |
| -1 | 系统繁忙 | 请稍后重试 |
|  |  |  |
