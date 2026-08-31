---
title: "撤回工作通知消息"
source_url: "https://open.dingtalk.com/document/development/notification-of-work-withdrawal"
namespace: "development"
slug: "notification-of-work-withdrawal"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 消息通知 > 工作通知 > 撤回工作通知消息"
doc_id: "qWS8CBrckf"
updated_at: "2026-07-14 09:22:12"
---

> Source: https://open.dingtalk.com/document/development/notification-of-work-withdrawal
> Path: 应用开发 / 服务端 API / 即时通信 > 消息通知 > 工作通知 > 撤回工作通知消息
> Updated: 2026-07-14 09:22:12

# 撤回工作通知消息

调用本接口，撤回工作通知消息，适用于企业内部应用需要撤回误发的工作通知场景。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/message/corpconversation/recall |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| agent\_id | Number | 是 | 836390886 | 发送消息时使用的微应用的AgentID。   - 企业内部应用，可在[开发者后台](https://open-dev.dingtalk.com/#/appMgr/inner/h5/836390886/1)的应用详情页面查看。image - 第三方企业应用可调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 |
| msg\_task\_id | Number | 是 | 256271667526 | 发送消息时钉钉返回的任务ID，调用[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口获取task\_id参数值。  **[!NOTE]**  仅支持撤回24小时内的工作消息通知。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/message/corpconversation/recall" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=404080xxxx4ab30' \
-d 'agent_id=1000' \
-d 'msg_task_id=2000'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/recall");
OapiMessageCorpconversationRecallRequest req = new OapiMessageCorpconversationRecallRequest();
req.setAgentId(1000L);
req.setMsgTaskId(2000L);
OapiMessageCorpconversationRecallResponse rsp = client.execute(req, accessToken);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMessageCorpconversationRecallRequest("https://oapi.dingtalk.com/topapi/message/corpconversation/recall")

req.agent_id=1000
req.msg_task_id=2000
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
$req = new OapiMessageCorpconversationRecallRequest;
$req->setAgentId("1000");
$req->setMsgTaskId("2000");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/message/corpconversation/recall");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/recall");
OapiMessageCorpconversationRecallRequest req = new OapiMessageCorpconversationRecallRequest();
req.AgentId = 1000L;
req.MsgTaskId = 2000L;
OapiMessageCorpconversationRecallResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "errcode":0,
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errorcode） | 错误信息描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 400002 | agentId不合法或taskId不合法 | 确认agentId或taskId是否正确 |
| 500 | 系统异常 | 出现未知的系统异常 |
