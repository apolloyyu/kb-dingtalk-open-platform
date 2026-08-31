---
title: "获取入群二维码链接"
source_url: "https://open.dingtalk.com/document/development/obtain-a-qr-code-link"
namespace: "development"
slug: "obtain-a-qr-code-link"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 群管理 > 获取入群二维码链接"
doc_id: "3wHxW0nbs6"
updated_at: "2026-07-14 09:22:04"
---

> Source: https://open.dingtalk.com/document/development/obtain-a-qr-code-link
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 群管理 > 获取入群二维码链接
> Updated: 2026-07-14 09:22:04

# 获取入群二维码链接

调用本接口，获取群入群二维码邀请链接，适用于企业需要快速邀请成员加入群聊的场景，如组织活动、项目协作等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/chat/qrcode/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_chat\_base\_read-钉钉群管理基础信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 30c36943eaxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| chatid | String | 是 | chat3234dfs423a | 群会话的chatid，可调用[创建群会话](0738-create-common-group-new-version-v2.md)接口获取chatid参数值。 |
| userid | String | 是 | manager4220 | 分享二维码用户的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/chat/qrcode/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=a1582fxxxx790254a' \
-d 'chatid=chat3234dfs423a' \
-d 'userid=314137418341347'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/chat/qrcode/get");
OapiChatQrcodeGetRequest req = new OapiChatQrcodeGetRequest();
req.setChatid("chat3234dfs423a");
req.setUserid("manager4220");
OapiChatQrcodeGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiChatQrcodeGetRequest("https://oapi.dingtalk.com/topapi/chat/qrcode/get")

req.chatid="chat3234dfs423a"
req.userid="314137418341347"
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
$req = new OapiChatQrcodeGetRequest;
$req->setChatid("chat3234dfs423a");
$req->setUserid("314137418341347");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/chat/qrcode/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/chat/qrcode/get");
OapiChatQrcodeGetRequest req = new OapiChatQrcodeGetRequest();
req.Chatid = "chat3234dfs423a";
req.Userid = "314137418341347";
OapiChatQrcodeGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | String | https://test/action/join?1233 | 返回入群的链接。 |
| success | Boolean | true | 是否调用成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 2tgtcjyjhptd | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": "https://qr.dingtalk.com/action/joingroup?code=v1=&_dt_no_comment=1&origin=11",
  "success": true,
  "request_id": "4jzlii1im1ui"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 34001 | 无效的会话id | 请检查chatId是否正确 |
| 40003 | 不合法的userid | 请确认userid是否正确 |
| 60124 | 用户不在此群中 | 请确认userid是否正确 |
| 400001 | 系统错误 | 请稍后再试 |
