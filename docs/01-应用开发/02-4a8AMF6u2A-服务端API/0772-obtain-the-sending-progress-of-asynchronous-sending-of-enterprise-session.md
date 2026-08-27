---
title: "获取工作通知消息的发送进度"
source_url: "https://open.dingtalk.com/document/development/obtain-the-sending-progress-of-asynchronous-sending-of-enterprise-session"
namespace: "development"
slug: "obtain-the-sending-progress-of-asynchronous-sending-of-enterprise-session"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 消息通知 > 工作通知 > 获取工作通知消息的发送进度"
doc_id: "wPTW8V2My4"
updated_at: "2026-07-13 09:45:38"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-sending-progress-of-asynchronous-sending-of-enterprise-session
> Path: 应用开发 / 服务端API / 即时通信 > 消息通知 > 工作通知 > 获取工作通知消息的发送进度
> Updated: 2026-07-13 09:45:38

# 获取工作通知消息的发送进度

调用本接口，获取工作通知消息的发送进度，适用于企业需监控消息推送状态、排查消息发送异常等场景。

## **接口调用说明**

调用本接口，只能获取7天内工作通知消息的发送进度。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/message/corpconversation/getsendprogress |
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
| task\_id | Number | 是 | 256271667526 | 发送消息时钉钉返回的任务ID，调用[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口获取task\_id参数值。  **[!NOTE]**  仅支持查询24小时内的任务。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/message/corpconversation/getsendprogress" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=a0a25xxxxed3ff' \
-d 'agent_id=123' \
-d 'task_id=456'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/getsendprogress");
OapiMessageCorpconversationGetsendprogressRequest req = new OapiMessageCorpconversationGetsendprogressRequest();
req.setAgentId(123L);
req.setTaskId(456L);
OapiMessageCorpconversationGetsendprogressResponse rsp = client.execute(req, accessToken);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMessageCorpconversationGetsendprogressRequest("https://oapi.dingtalk.com/topapi/message/corpconversation/getsendprogress")

req.agent_id=123
req.task_id=456
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
$req = new OapiMessageCorpconversationGetsendprogressRequest;
$req->setAgentId("123");
$req->setTaskId("456");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/message/corpconversation/getsendprogress");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/getsendprogress");
OapiMessageCorpconversationGetsendprogressRequest req = new OapiMessageCorpconversationGetsendprogressRequest();
req.AgentId = 123L;
req.TaskId = 456L;
OapiMessageCorpconversationGetsendprogressResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 5y2znla8tw3d | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| progress | AsyncSendProgress |  | 返回结果。 |
| progress\_in\_percent | Number | 100 | 取值0~100，表示处理的百分比。 |
| status | Number | 2 | 任务执行状态：   - **0**：未开始 - **1**：处理中 - **2**：处理完毕 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "progress": {
    "progress_in_percent": 100,
    "status": 2
  },
  "request_id": "5y2znla8tw3d"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errorcode） | 错误信息描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40035 | 不合法的参数 | 确认task\_id或者agent\_id是否正确 |
| 500 | 系统异常 | 出现未知的系统异常 |
