---
title: "通知审批撤销"
source_url: "https://open.dingtalk.com/document/development/notify-the-attendance-to-modify-the-punch-result-when-the"
namespace: "development"
slug: "notify-the-attendance-to-modify-the-punch-result-when-the"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 假勤审批 > 通知审批撤销"
doc_id: "Ozmm0CHD6y"
updated_at: "2026-05-27 17:06:21"
---

> Source: https://open.dingtalk.com/document/development/notify-the-attendance-to-modify-the-punch-result-when-the
> Path: 应用开发 / 服务端API / 考勤 > 假勤审批 > 通知审批撤销
> Updated: 2026-05-27 17:06:21

# 通知审批撤销

调用本接口，通知审批撤销，支持加班、请假、外出、出差和补卡类型。

## **接口调用说明**

当调用[通知审批通过](0226-api-processapprovefinish.md)接口之后，由于各种原因提交的审批单需要被撤销时，需要调用本接口撤销修改的考勤记录。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/approve/cancel |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager4220 | 员工的userId。 |
| approve\_id | String | 是 | 2376620852 | 审批ID，来自[通知审批通过](0226-api-processapprovefinish.md)接口自定义的参数approve\_id。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/approve/cancel" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=95676xxxxdee' \
-d 'approve_id=1234abcd' \
-d 'userid=dd_dd'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/approve/cancel");
OapiAttendanceApproveCancelRequest req = new OapiAttendanceApproveCancelRequest();
req.setUserid("manager4220");
req.setApproveId("2376620852");
OapiAttendanceApproveCancelResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceApproveCancelRequest("https://oapi.dingtalk.com/topapi/attendance/approve/cancel")

req.userid="dd_dd"
req.approve_id="1234abcd"
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
$req = new OapiAttendanceApproveCancelRequest;
$req->setUserid("dd_dd");
$req->setApproveId("1234abcd");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/approve/cancel");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/approve/cancel");
OapiAttendanceApproveCancelRequest req = new OapiAttendanceApproveCancelRequest();
req.Userid = "dd_dd";
req.ApproveId = "1234abcd";
OapiAttendanceApproveCancelResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "errcode":0,
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
