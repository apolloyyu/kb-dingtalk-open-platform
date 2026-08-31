---
title: "获取推送失败的事件列表"
source_url: "https://open.dingtalk.com/document/development/obtain-the-event-list-of-failed-push-messages"
namespace: "development"
slug: "obtain-the-event-list-of-failed-push-messages"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "事件订阅 > 获取推送失败的事件列表"
doc_id: "IWvcsmVAaV"
updated_at: "2026-05-08 17:50:33"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-event-list-of-failed-push-messages
> Path: 应用开发 / 服务端 API / 事件订阅 > 获取推送失败的事件列表
> Updated: 2026-05-08 17:50:33

# 获取推送失败的事件列表

调用本接口获取推送失败的变更事件。钉钉服务器给回调地址推送数据时，有可能因为各种原因推送失败（例如网络异常），此时钉钉将保留此次变更事件。

## **接口调用说明**

事件订阅推送失败，会进行重新推送，重试规则如下：

| **第几次重试** | **与上次重试时间间隔** |
| --- | --- |
| 1 | 10秒 |
| 2 | 30秒 |

例如：事件第一次推送失败后，经过10秒，进行第一次重试，直至第 2 次重试失败后，可在3～5分钟内通过本接口获取推送失败的事件列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/call\_back/get\_call\_back\_failed\_result |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 577bfxxxx473f99d40c | 调用服务端API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用，通过[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

### **请求示例**

curl

```
curl -X GET "https://oapi.dingtalk.com/call_back/get_call_back_failed_result" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=577bfxxxx473f99d40c'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/call_back/get_call_back_failed_result");
OapiCallBackGetCallBackFailedResultRequest req = new OapiCallBackGetCallBackFailedResultRequest();
req.setHttpMethod("GET");
OapiCallBackGetCallBackFailedResultResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api
req=dingtalk.api.OapiCallBackGetCallBackFailedResultRequest("https://oapi.dingtalk.com/call_back/get_call_back_failed_result")
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
$req = new OapiCallBackGetCallBackFailedResultRequest;
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/call_back/get_call_back_failed_result");
```

Node.js

```
let { Config, OapiCallBackGetCallBackFailedResultParams, OapiCallBackGetCallBackFailedResultRequest } = require('./client.js');
let Client = require('./client.js').default
async function test() {
  const config = new Config()
  config.serverUrl = 'https://oapi.dingtalk.com/call_back/get_call_back_failed_result'
  const params = new OapiCallBackGetCallBackFailedResultParams();
  params.access_token = 'b341dc8xxxxe0bbf';
  const request = new OapiCallBackGetCallBackFailedResultRequest()
  request.params = params
  const client = new Client(config)
  try {
    const res = await client.oapiCallBackGetCallBackFailedResult(request)
    console.log(res.body)
  } catch (err) {
    console.log(err)
  }
}
test()
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/call_back/get_call_back_failed_result");
OapiCallBackGetCallBackFailedResultRequest req = new OapiCallBackGetCallBackFailedResultRequest();
req.SetHttpMethod("GET");
OapiCallBackGetCallBackFailedResultResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| failed\_list | Failed[] |  | 推送失败的事件列表，一次最多200个。 |
| call\_back\_tag | String | user\_add\_org | 事件类型。 |
| event\_time | Number |  | 事件的时间戳。 |
| bpms\_instance\_change | Json |  | failed\_list数组下每个单元的key，表示不同的回调tag。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 对返回码的文本描述内容。 |
| has\_more | Boolean | false | 是否还有推送失败的变更事件，若为true，则表示还有未回调的事件。 |
| corpid | String | ding241f334c339e175b35c2f4657xxxx | 回调失败数据所属corpid。 |
| bpmsCallBackData|callbackData|roleLabelChange | Json |  | 具体回调失败的数据所属key。   - **bpmsCallBackData**：审批回调 - **roleLabelChange**：角色回调 - **callbackData**：其他回调 |

### **响应体示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "failed_list": [
        {
            "user_add_org": {
                "userid": [
                    "zhangsan"
                ],
                "corpid": "ding241f334c339e175b35c2f4657xxxx"
            },
            "call_back_tag": "user_add_org",
            "event_time": 1606126433000
        },
        {
            "bpms_instance_change": {
                "bpmsCallBackData": {},
                "corpid": "ding241f334c339e175b35c2f4657xxxx"
            },
            "call_back_tag": "bpms_instance_change",
            "event_time": 1606126433000
        },
        {
            "label_conf_add": {
                "roleLabelChange": {},
                "corpid": "ding241f334c339e175b35c2f4657xxxx"
            },
            "call_back_tag": "label_conf_add",
            "event_time": 1606126433000
        }
    ],
    "has_more": false
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
