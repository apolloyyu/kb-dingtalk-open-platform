---
title: "消息撤回"
source_url: "https://open.dingtalk.com/document/development/service-number-message-withdrawal"
namespace: "development"
slug: "service-number-message-withdrawal"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 互动服务窗 > 消息群发 > 消息撤回"
doc_id: "7oyHexzCL5"
updated_at: "2026-06-01 09:15:37"
---

> Source: https://open.dingtalk.com/document/development/service-number-message-withdrawal
> Path: 应用开发 / 服务端API / 专属钉钉 > 互动服务窗 > 消息群发 > 消息撤回
> Updated: 2026-06-01 09:15:37

# 消息撤回

调用本接口，根据消息发送的任务id撤回24小时内的消息。

## **接口调用说明**

发送超过24小时的消息，不支持通过本接口进行撤回。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/message/mass/recall |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_service\_account\_message-服务号消息管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 30c36943eaxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| unionid | String | 是 | jYdrxxxxTo0iE | 服务号的unionid，可以通过[查询服务号详情](0813-inquire-about-service-number-details.md)接口获取。 |
| task\_id | String | 是 | pushWxxxx2rjeI2SswiEiE | 消息发送任务id，可以通过[消息群发](1625-interactive-service-window-group-message-sending-interface.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/message/mass/recall" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=2a52exxxx32ae4fe' \
-d 'task_id=pushWxxxx2rjeI2SswiEiE' \
-d 'unionid=jYdrxxxxTo0iE'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/mass/recall");
OapiMessageMassRecallRequest req = new OapiMessageMassRecallRequest();
req.setUnionid("jYdrxxxxTo0iE");
req.setTaskId("pushWxxxx2rjeI2SswiEiE");
OapiMessageMassRecallResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMessageMassRecallRequest("https://oapi.dingtalk.com/topapi/message/mass/recall")

req.unionid="jYdrxxxxTo0iE"
req.task_id="pushWxxxx2rjeI2SswiEiE"
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
$req = new OapiMessageMassRecallRequest;
$req->setUnionid("jYdrxxxxTo0iE");
$req->setTaskId("pushWxxxx2rjeI2SswiEiE");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/message/mass/recall");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/mass/recall");
OapiMessageMassRecallRequest req = new OapiMessageMassRecallRequest();
req.Unionid = "jYdrxxxxTo0iE";
req.TaskId = "pushWxxxx2rjeI2SswiEiE";
OapiMessageMassRecallResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | ouad0q1rtlhw | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "request_id":"ouad0q1rtlhw"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码 | 说明 | 排查方法 |
| --- | --- | --- |
| 800025 | task\_id不合法 | 检查传入task\_id是否正确。 |
