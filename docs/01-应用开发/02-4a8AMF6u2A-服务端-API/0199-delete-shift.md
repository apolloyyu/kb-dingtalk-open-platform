---
title: "删除班次"
source_url: "https://open.dingtalk.com/document/development/delete-shift"
namespace: "development"
slug: "delete-shift"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤班次 > 删除班次"
doc_id: "p4JKFrT3dF"
updated_at: "2026-07-02 10:36:15"
---

> Source: https://open.dingtalk.com/document/development/delete-shift
> Path: 应用开发 / 服务端 API / 考勤 > 考勤班次 > 删除班次
> Updated: 2026-07-02 10:36:15

# 删除班次

调用本接口，根据班次ID删除考勤班次。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/shift/delete |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | af21xxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 是 | user123 | 操作人userId。 |
| shift\_id | Number | 是 | 2423 | 班次ID，可通过[获取班次摘要信息](0203-enterprise-shift-query-in-batches.md)接口获取id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/shift/delete" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=032bc0xxxxc460ee' \
-d 'op_user_id=abc' \
-d 'shift_id=2423'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/delete");
OapiAttendanceShiftDeleteRequest req = new OapiAttendanceShiftDeleteRequest();
req.setOpUserId("user456");
req.setShiftId(2423L);
OapiAttendanceShiftDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceShiftDeleteRequest("https://oapi.dingtalk.com/topapi/attendance/shift/delete")

req.op_user_id="abc"
req.shift_id=2423
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
$req = new OapiAttendanceShiftDeleteRequest;
$req->setOpUserId("abc");
$req->setShiftId("2423");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/shift/delete");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/delete");
OapiAttendanceShiftDeleteRequest req = new OapiAttendanceShiftDeleteRequest();
req.OpUserId = "abc";
req.ShiftId = 2423L;
OapiAttendanceShiftDeleteResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | 系统错误 | 调用失败时返回的错误信息。 |
| errcode | Number | 0 | 返回码。 |
| success | Boolean | true | 调用是否成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | 16apb7hw85jjw | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "success": true,
  "request_id": "3lupjm5o0j7g"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
