---
title: "查询场景群基本信息"
source_url: "https://open.dingtalk.com/document/development/queries-the-basic-information-of-a-scenario-group"
namespace: "development"
slug: "queries-the-basic-information-of-a-scenario-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群管理 > 查询场景群基本信息"
doc_id: "610NIo2cBV"
updated_at: "2026-08-14 09:41:58"
---

> Source: https://open.dingtalk.com/document/development/queries-the-basic-information-of-a-scenario-group
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 场景群 > 群管理 > 查询场景群基本信息
> Updated: 2026-08-14 09:41:58

# 查询场景群基本信息

调用本接口，根据群ID获取群名称、群图标、群主id、入群链接、群设置项等信息，适用于需要查看群详细信息的场景，如群管理、群数据分析等。

## **接口调用说明**

支持场景：基于群模板创建的群，详情参见[创建群](1484-create-a-scene-group-v2.md)。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/im/chat/scenegroup/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_chat\_read-钉钉群基础信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| open\_conversation\_id | String | 是 | cid9FTRQSLo+s\*\*\*\*\*== | 群ID，调用[创建场景群](0746-create-a-scene-group.md)接口获取`open_conversation_id`参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/im/chat/scenegroup/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=b09cxxxxb8f731' \
-d 'open_conversation_id=123123'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scenegroup/get");
OapiImChatScenegroupGetRequest req = new OapiImChatScenegroupGetRequest();
req.setOpenConversationId("cid9FTRQSLo+s*****==");
OapiImChatScenegroupGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiImChatScenegroupGetRequest("https://oapi.dingtalk.com/topapi/im/chat/scenegroup/get")

req.open_conversation_id="123123"
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
$req = new OapiImChatScenegroupGetRequest;
$req->setOpenConversationId("123123");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/im/chat/scenegroup/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scenegroup/get");
OapiImChatScenegroupGetRequest req = new OapiImChatScenegroupGetRequest();
req.OpenConversationId = "123123";
OapiImChatScenegroupGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | DecorationGroupQueryResponse |  | 返回结果。 |
| icon | String | @lADOADma\*\*\*\*\*QKA | 群头像。 |
| management\_options | ManagementOptions |  | 群配置。 |
| chat\_banned\_type | String | 0 | 是否开启群禁言：   - **0**（默认）：不禁言 - **1**：全员禁言 |
| searchable | String | 0 | 群是否可搜索：   - **0**（默认）：不可搜索 - **1**：可搜索 |
| validation\_type | String | 0 | 入群是否需要验证：   - **0**（默认）：不验证入群 - **1**：入群验证 |
| mention\_all\_authority | String | 0 | @all 权限：   - **0**（默认）：所有人 - **1**：仅群主 |
| management\_type | String | 0 | 管理类型：   - **0**（默认）：所有人可管理 - **1**：仅群主可管理 |
| show\_history\_type | String | 0 | 新成员是否可查看聊天历史消息：   - **0**（默认）：否 - **1**：是 |
| title | String | 测试群 | 群标题。 |
| template\_id | String | c354\*\*\*-\*\*\*-\*\*\*-b4ea-6f1ab\*\*\*65 | 模板id。 |
| open\_conversation\_id | String | cid9FTRQSLo+s\*\*\*\*\*== | 群id。 |
| sub\_admin\_staff\_ids | String[] | ["072\*\*\*\*\*","013\*\*\*\*\*"] | 群管理员的userId。 |
| owner\_staff\_id | String | 022\*\*\*\*\* | 群主的userId。 |
| group\_url | String | https://example.com | 入群链接。 |
| success | Boolean | true | 是否成功。 |
| errcode | Number | 1001 | 错误码。 |
| errmsg | String | systemerror | 错误信息。 |
| request\_id | String | 5ocnguahrf | 请求ID。 |

### **响应体示例**

```
{
  "result":{
    "sub_admin_staff_ids": [
      "072*****", 
      "013*****"
    ], 
    "open_conversation_id":"cid9FTRQSLo+s*****==",
    "icon":"@lADOADma*****QKA",
    "template_id":"c354***-***-***-b4ea-6f1ab***65",
    "title":"测试群",
    "owner_staff_id":"022*****",
    "management_options":{
      "chat_banned_type":"0",
      "validation_type":"0",
      "mention_all_authority":"0",
      "management_type":"0",
      "searchable":"0",
      "show_history_type":"0"
    },
    "group_url":"https://example.com"
  },
  "errcode":0,
  "success":true,
  "errmsg":"ok",
  "request_id": "5ocnguahrf"   
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40035 | 无效的请求参数 | 请确认参数是否符合上述入参要求 |
| 400020 | 无访问权限 | 请确认群内是否安装群模板，或者安装的群模板是否属于当前token对应的应用名下 |
| 400001 | 系统错误 | 优先确认群ID是否正确，请稍后重试 |
