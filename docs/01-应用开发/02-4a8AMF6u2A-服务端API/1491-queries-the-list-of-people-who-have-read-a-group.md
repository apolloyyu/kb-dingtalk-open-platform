---
title: "查询群消息已读人员列表"
source_url: "https://open.dingtalk.com/document/development/queries-the-list-of-people-who-have-read-a-group"
namespace: "development"
slug: "queries-the-list-of-people-who-have-read-a-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 消息通知 > 企业群消息 > 查询群消息已读人员列表"
doc_id: "75uq9mkCvk"
updated_at: "2026-08-25 09:37:20"
---

> Source: https://open.dingtalk.com/document/development/queries-the-list-of-people-who-have-read-a-group
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 即时通信 > 消息通知 > 企业群消息 > 查询群消息已读人员列表
> Updated: 2026-08-25 09:37:20

# 查询群消息已读人员列表

调用本接口查询群消息已读人员列表。

> **[!IMPORTANT]**
>
> - 为提升接口的使用体验，当前接口计划升级，重新开放时间请[开放概览](0764-message-corpconversation-overview.md#section-rtj-q87-8ea)。
> - 不再支持新应用接入，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，该接口权限默认添加，无需申请。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/chat/getReadList`

## Query参数

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | String | 是 | 调用服务端API的应用凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |
| messageId | String | 是 | [发送消息到企业群](1490-send-group-messages.md)接口返回的加密消息id。  **[!IMPORTANT]**  消息id中包含url特殊字符时需要encode后再使用。 |
| cursor | Number | 是 | 分页查询的游标，第一次可以传0，后续传返回结果中的next\_cursor的值。  当返回结果中，没有next\_cursor时，表示没有后续的数据了，可以结束调用。 |
| size | Number | 是 | 分页查询的大小，最大可以传100，且不能超过群的总人数。 |

## 返回参数

| 参数 | 类型 | 示例值 | 说明 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码的描述。 |
| next\_cursor | Number | 10 | 下次分页获取的起始游标。 |
| readUserIdList | String[] | user123 | 已读人员的userid列表。  已读人员为空时不返回该参数。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/chat/getReadList?access_token=ACCESS_TOKEN&messageId=111&cursor=0&size=10
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/chat/getReadList");
OapiChatGetReadListRequest req = new OapiChatGetReadListRequest();
req.setMessageId("111");
req.setCursor(0L);
req.setSize(10L);
req.setHttpMethod("GET");
OapiChatGetReadListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "next_cursor": 200467002472,
    "readUserIdList": [
        "user123"
    ]
}
```

## 错误码

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40035 | 无效的参数 | 请确认参数是否符合上述入参要求 |
| 40068 | 无效的偏移量 | 请确认偏移量是否合法 |
| 40069 | 无效的大小 | 请确认查询大小是否合法 |
| -1 | 系统繁忙 | 请稍后再试 |
