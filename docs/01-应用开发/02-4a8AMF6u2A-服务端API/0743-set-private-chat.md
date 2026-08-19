---
title: "设置禁止群成员私聊"
source_url: "https://open.dingtalk.com/document/development/set-private-chat"
namespace: "development"
slug: "set-private-chat"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 群管理 > 设置禁止群成员私聊"
doc_id: "0s8TsaLqIS"
updated_at: "2026-07-14 09:22:03"
---

> Source: https://open.dingtalk.com/document/development/set-private-chat
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 群管理 > 设置禁止群成员私聊
> Updated: 2026-07-14 09:22:03

# 设置禁止群成员私聊

调用本接口设置群成员之间是否可以添加好友和私聊，适用于企业内部群需要管控成员交流范围、保护信息安全等场景。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/chat/member/friendswitch/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| chatid | String | 是 | chatdafe234xxxx | 企业会话ID。可以通过以下方式获取。   - 调用服务端[创建群会话](0738-create-common-group-new-version-v2.md)接口获取chatid参数值。 - 调用客户端[chooseChat](../03-Ogu5SlPY4t-客户端JSAPI/0318-jsapi-choose-chat.md)获取chatId参数值。 |
| is\_prohibit | Boolean | 是 | true | 是否开启禁止开关。   - **true**：开启禁止开关 - **false**：关闭禁止开关 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/chat/member/friendswitch/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=774fdexxxx4bdd68c' \
-d 'chatid=chatdafe234sdf3sdf' \
-d 'is_prohibit=true'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/chat/member/friendswitch/update");
OapiChatMemberFriendswitchUpdateRequest req = new OapiChatMemberFriendswitchUpdateRequest();
req.setChatid("chatdafe234xxxx");
req.setIsProhibit(true);
OapiChatMemberFriendswitchUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiChatMemberFriendswitchUpdateRequest("https://oapi.dingtalk.com/topapi/chat/member/friendswitch/update")

req.chatid="chatdafe234sdf3sdf"
req.is_prohibit=true
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
$req = new OapiChatMemberFriendswitchUpdateRequest;
$req->setChatid("chatdafe234sdf3sdf");
$req->setIsProhibit("true");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/chat/member/friendswitch/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/chat/member/friendswitch/update");
OapiChatMemberFriendswitchUpdateRequest req = new OapiChatMemberFriendswitchUpdateRequest();
req.Chatid = "chatdafe234sdf3sdf";
req.IsProhibit = true;
OapiChatMemberFriendswitchUpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 是否设置成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 10c0wc48i6qzz | 请求ID。 |

### **响应体示例**

```
{
  "success":true,
  "errcode":0,
  "errmsg":"ok",
  "request_id":"10c0wc48i6qzz"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 34001 | 无效的chatid | 请检查chatid是否符合要求 |
| 40036 | 参数为空 | 请确认必填参数是否都已经填入 |
| 400001 | 系统错误 | 请稍后重试 |
