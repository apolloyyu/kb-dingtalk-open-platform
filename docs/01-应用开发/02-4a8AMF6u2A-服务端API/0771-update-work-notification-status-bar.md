---
title: "更新工作通知状态栏"
source_url: "https://open.dingtalk.com/document/development/update-work-notification-status-bar"
namespace: "development"
slug: "update-work-notification-status-bar"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 消息通知 > 工作通知 > 更新工作通知状态栏"
doc_id: "pqDHKIzFIJ"
updated_at: "2026-07-13 09:43:54"
---

> Source: https://open.dingtalk.com/document/development/update-work-notification-status-bar
> Path: 应用开发 / 服务端API / 即时通信 > 消息通知 > 工作通知 > 更新工作通知状态栏
> Updated: 2026-07-13 09:43:54

# 更新工作通知状态栏

调用本接口，更新 OA 工作通知消息的状态。

## **接口调用说明**

- 本接口适用于 OA 工作通知类型，实时更新审批状态的场景。
- 调用本接口，只能更新7天内发出的工作通知状态栏。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/message/corpconversation/status\_bar/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| agent\_id | Number | 是 | 123 | 发送消息时使用的微应用的AgentID。   - 企业内部应用，可在[开发者后台](https://open-dev.dingtalk.com/#/appMgr/inner/h5/836390886/1)的应用详情页面查看。image - 第三方企业应用可调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 |
| task\_id | Number | 是 | 11 | 工作通知任务ID，调用[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口获取task\_id参数值。 |
| status\_value | String | 是 | 已同意 | 状态栏值。 |
| status\_bg | String | 否 | 0xFF78C06E | 状态栏背景色，推荐0xFF加六位颜色值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/message/corpconversation/status_bar/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=e4bbxxxxe7683' \
-d 'agent_id=123' \
-d 'status_bg=0xFFF65E5E' \
-d 'status_value=%E5%B7%B2%E5%AE%8C%E6%88%90' \
-d 'task_id=1111'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/status_bar/update");
OapiMessageCorpconversationStatusBarUpdateRequest req = new OapiMessageCorpconversationStatusBarUpdateRequest();
req.setAgentId(123L);
req.setTaskId(1111L);
req.setStatusValue("已完成");
req.setStatusBg("0xFFF65E5E");
OapiMessageCorpconversationStatusBarUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMessageCorpconversationStatusBarUpdateRequest("https://oapi.dingtalk.com/topapi/message/corpconversation/status_bar/update")

req.agent_id=123
req.task_id=1111
req.status_value="已完成"
req.status_bg="0xFFF65E5E"
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
$req = new OapiMessageCorpconversationStatusBarUpdateRequest;
$req->setAgentId("123");
$req->setTaskId("1111");
$req->setStatusValue("已完成");
$req->setStatusBg("0xFFF65E5E");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/message/corpconversation/status_bar/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/status_bar/update");
OapiMessageCorpconversationStatusBarUpdateRequest req = new OapiMessageCorpconversationStatusBarUpdateRequest();
req.AgentId = 123L;
req.TaskId = 1111L;
req.StatusValue = "已完成";
req.StatusBg = "0xFFF65E5E";
OapiMessageCorpconversationStatusBarUpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 4jzllmte0wau | 请求ID。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "request_id":"4jzllmte0wau"
  "errcode":0,
  "errmsg":"ok",
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errorcode） | 错误信息描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40056 | 不合法的agentid | 确认agentId是否正确 |
| 40035 | 不合法的参数 | 确认taskId是否正确 |
| 41052 | 本次发送人数过多,不再返回发送结果 | - 减少发送工作通知人员数量 - 确认工作通知消息的发送进度是否完成，若进度没有完成，则会出现该错误。 |
| 500 | 系统异常 | 出现未知的系统异常 |
