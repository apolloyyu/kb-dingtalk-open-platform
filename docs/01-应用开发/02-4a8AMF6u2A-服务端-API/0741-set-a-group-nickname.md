---
title: "更新群成员的群昵称"
source_url: "https://open.dingtalk.com/document/development/set-a-group-nickname"
namespace: "development"
slug: "set-a-group-nickname"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 群管理 > 更新群成员的群昵称"
doc_id: "hLfKuDVLRe"
updated_at: "2026-07-14 09:22:03"
---

> Source: https://open.dingtalk.com/document/development/set-a-group-nickname
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 群管理 > 更新群成员的群昵称
> Updated: 2026-07-14 09:22:03

# 更新群成员的群昵称

调用本接口更新群成员在群中的昵称，适用于群管理员统一规范群成员昵称和群成员自行修改昵称等场景。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/chat/updategroupnick |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | beE3xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | user123 | 要更改群昵称的群成员userId，可通过[查询群信息](0740-obtain-a-group-session.md)接口获取群成员userId。 |
| chatid | String | 是 | chate3929fxxxx | 群会话ID，可通过[创建群会话](0738-create-common-group-new-version-v2.md)接口获取chatid参数值。 |
| group\_nick | String | 是 | 钉钉小二 | 该成员在群中的昵称。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/chat/updategroupnick" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=61a72xxxx8d62' \
-d 'chatid=0' \
-d 'group_nick=nick' \
-d 'userid=0'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/chat/updategroupnick");
OapiChatUpdategroupnickRequest req = new OapiChatUpdategroupnickRequest();
req.setUserid("user123");
req.setChatid("chate39f540d572b71cf97a556d95929fxxxx");
req.setGroupNick("钉钉小二");
OapiChatUpdategroupnickResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiChatUpdategroupnickRequest("https://oapi.dingtalk.com/topapi/chat/updategroupnick")

req.userid="0"
req.chatid="0"
req.group_nick="nick"
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

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST , DingTalkConstant::$FORMAT_JSON);
$req = new OapiChatUpdategroupnickRequest;
$req->setUserid("0");
$req->setChatid("0");
$req->setGroupNick("nick");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/chat/updategroupnick");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/chat/updategroupnick");
OapiChatUpdategroupnickRequest req = new OapiChatUpdategroupnickRequest();
req.Userid = "0";
req.Chatid = "0";
req.GroupNick = "nick";
OapiChatUpdategroupnickResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 操作是否成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | id1aatxt9mco | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "success": true,
  "request_id": "id1aatxt9mco"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40003 | 无效的userid | 请确认userid是否填写正确 |
| 34001 | 无效的chatid | 请确认chatid是否正确 |
| 41049 | 包含违禁内容 | 请修改输入的昵称 |
| 60124 | 用户不在对应的群内 | 请更新群内的用户 |
| 400002 | 参数错误 | 请检查参数是否按上述入参要求填写 |
| 400001 | 系统错误 | 请稍后再试 |
