---
title: "查询群信息"
source_url: "https://open.dingtalk.com/document/development/obtain-a-group-session"
namespace: "development"
slug: "obtain-a-group-session"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 群管理 > 查询群信息"
doc_id: "nqDZ6FziCZ"
updated_at: "2026-06-08 09:21:15"
---

> Source: https://open.dingtalk.com/document/development/obtain-a-group-session
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 群管理 > 查询群信息
> Updated: 2026-06-08 09:21:15

# 查询群信息

调用本接口获取群设置和成员信息。，适用于群管理员查看群设置和成员信息、进行群管理决策等场景。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/chat/get |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_chat\_read-钉钉群基础信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |
| chatid | String | 是 | chate39f540dxxxx | 群会话的ID。   - 仅支持通过调用服务端[创建群会话](0738-create-common-group-new-version-v2.md)接口获取的chatid参数值。 - 不支持通过调用前端JSAPI获取的chatid。 |

### **请求示例**

curl

```
curl -X GET "https://oapi.dingtalk.com/chat/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=0d7e495xxxxa3f694fd6e' \
-d 'chatid=chatid'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/chat/get");
OapiChatGetRequest req = new OapiChatGetRequest();
req.setChatid("chate39f540dxxxx");
req.setHttpMethod("GET");
OapiChatGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiChatGetRequest("https://oapi.dingtalk.com/chat/get")

req.chatid="chatid"
try:
  resp= req.getResponse(access_token)
  print(resp)
except Exception,e:
  print(e)
```

PHP

```
include "TopSdk.php";
date_default_timezone_set('Asia/Shanghai');

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_GET , DingTalkConstant::$FORMAT_JSON);
$req = new OapiChatGetRequest;
$req->setChatid("chatid");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/chat/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/chat/get");
OapiChatGetRequest req = new OapiChatGetRequest();
req.Chatid = "chatid";
req.SetHttpMethod("GET");
OapiChatGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| chat\_info | ChatInfo |  | 群会话信息。 |
| name | String | 全员群 | 群名称。 |
| owner | String | manager4220 | 群主的userId。 |
| useridlist | String[] | ["user123","manager4220"] | 群成员的userId列表。 |
| conversationTag | Number | 2 | 会话类型：   - **2**：企业群。 |
| chatBannedType | Number | 0 | 是否开启群禁言：   - **0**（默认）：不禁言 - **1**：全员禁言 |
| searchable | Number | 0 | 群是否可以被搜索：   - **0**（默认）：不可搜索 - **1**：可搜索 |
| validationType | Number | 0 | 入群是否需要验证   - **0**（默认）：不验证 - **1**：入群验证 |
| mentionAllAuthority | Number | 0 | @all 使用范围：   - **0**（默认）：所有人可使用 - **1**：仅群主可@all |
| managementType | Number | 0 | 群管理类型：   - **0**（默认）：所有人可管理 - **1**：仅群主可管理 |
| showHistoryType | Number | 0 | 新成员是否可查看100条历史消息：   - **1**：可查看 - **0**：不可查看  如果不传值，代表不可查看。 |
| icon | String | @lADPDfJ6Q7LLejDNAljNAlg | 群头像的mediaID。 |
| status | Number | 1 | 状态。   - 1：正常 - 2：已解散 |

### **响应体示例**

```
{
  "errcode":0,
  "errmsg":"ok",
  "chat_info":{
    "owner":"manager4220",
    "mentionAllAuthority":0,
    "showHistoryType":0,
    "chatid":"chate39f540dxxxx",
    "conversationTag":2,
    "validationType":0,
    "useridlist":[
      "user123",
      "manager4220"
    ],
    "icon":"@lADPDfJ6Q7LLejDNAljNAlg",
    "name":"全员群",
    "searchable":0,
    "chatBannedType":0,
    "managementType":0
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 43007 | 没有调用权限 | 请确认是否是当前应用生成access\_token。 |
| 49000 | 需要参数chatid | 请填入chatid |
| 40001 | 无效的token | 请确认access\_token是否正确 |
| 70001 | 企业不存在 | 请确认参数是否正确 |
| 40016 | 无效的chatid | 请确认access\_token和chatid来自同一个企业 |
| -1 | 系统繁忙 | 请稍后重试 |
