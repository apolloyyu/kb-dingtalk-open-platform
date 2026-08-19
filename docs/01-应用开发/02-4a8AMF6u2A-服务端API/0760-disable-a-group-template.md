---
title: "停用群模板"
source_url: "https://open.dingtalk.com/document/development/disable-a-group-template"
namespace: "development"
slug: "disable-a-group-template"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群模板 > 停用群模板"
doc_id: "nbhxGnNIo9"
updated_at: "2026-07-14 09:22:07"
---

> Source: https://open.dingtalk.com/document/development/disable-a-group-template
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 场景群 > 群模板 > 停用群模板
> Updated: 2026-07-14 09:22:07

# 停用群模板

调用本接口，根据群模板ID、群ID停用群模板（失效群模板配置项、卸载群模板机器人、关闭群模板快捷入口）。

## **接口调用说明**

支持场景：基于群模板创建的群，详情参见[创建场景群](0746-create-a-scene-group.md)。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/im/chat/scenegroup/template/close |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| owner\_user\_id | String | 是 | 013\*\*\*\*\* | 群主userid。 |
| template\_id | String | 是 | c354\*\*\*-\*\*\*-\*\*\*-b4ea-6f1ab\*\*\*65 | 群模板id，登录[开发者后台 > 开放能力 > 场景群 > 群模板](https://open-dev.dingtalk.com/fe/im#/group/list)查看id。image |
| open\_conversation\_id | String | 是 | cid9FTRQSLo+sK\*\*\*\*\*== | 群ID，调用[创建场景群](0746-create-a-scene-group.md)接口获取`open_conversation_id`参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/im/chat/scenegroup/template/close" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=aca06xxxx0ccad06e' \
-d 'open_conversation_id=123' \
-d 'owner_user_id=123' \
-d 'template_id=template123'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scenegroup/template/close");
OapiImChatScenegroupTemplateCloseRequest req = new OapiImChatScenegroupTemplateCloseRequest();
req.setOwnerUserId("123");
req.setTemplateId("template123");
req.setOpenConversationId("123");
OapiImChatScenegroupTemplateCloseResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiImChatScenegroupTemplateCloseRequest("https://oapi.dingtalk.com/topapi/im/chat/scenegroup/template/close")

req.owner_user_id="123"
req.template_id="template123"
req.open_conversation_id="123"
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
$req = new OapiImChatScenegroupTemplateCloseRequest;
$req->setOwnerUserId("123");
$req->setTemplateId("template123");
$req->setOpenConversationId("123");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/im/chat/scenegroup/template/close");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scenegroup/template/close");
OapiImChatScenegroupTemplateCloseRequest req = new OapiImChatScenegroupTemplateCloseRequest();
req.OwnerUserId = "123";
req.TemplateId = "template123";
req.OpenConversationId = "123";
OapiImChatScenegroupTemplateCloseResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 调用是否成功。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "errcode":0,
  "success":"true",
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errorcode） | 错误信息描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 665036 | 群模板不存在或停用 | 确认群模板id是否正确 |
| 660023 | 群ID 解码失败 | 确认群Id是否正确 |
| 500 | 系统异常 | 优先确认群id，群模板id是否正确，请稍后重试 |
