---
title: "获取推送失败的事件列表"
source_url: "https://open.dingtalk.com/document/development/list-of-events-where-historical-push-notifications-failed"
namespace: "development"
slug: "list-of-events-where-historical-push-notifications-failed"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 回调接口 > 获取推送失败的事件列表"
doc_id: "yD3p7TGT2j"
updated_at: "2025-12-05 19:33:01"
---

> Source: https://open.dingtalk.com/document/development/list-of-events-where-historical-push-notifications-failed
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 回调接口 > 获取推送失败的事件列表
> Updated: 2025-12-05 19:33:01

# 获取推送失败的事件列表

调用本获取推送失败的变更事件。钉钉服务器给回调地址推送数据时，有可能因为各种原因推送失败（例如网络异常），此时钉钉将保留此次变更事件。

## 权限

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 默认开通，无需申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingtalk.oapi.call_back.get_call_back_failed_result) |
| 第三方企业应用 | 是 | 默认开通，无需申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=dingtalk.oapi.call_back.get_call_back_failed_result) |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/call_back/get_call_back_failed_result`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## 返回参数

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

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/call_back/get_call_back_failed_result?access_token=ACCESS_TOKEN
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/call_back/get_call_back_failed_result");
OapiCallBackGetCallBackFailedResultRequest req = new OapiCallBackGetCallBackFailedResultRequest();
req.setHttpMethod("GET");
OapiCallBackGetCallBackFailedResultResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

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
