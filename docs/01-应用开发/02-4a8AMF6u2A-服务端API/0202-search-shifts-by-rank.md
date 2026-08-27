---
title: "按名称搜索班次"
source_url: "https://open.dingtalk.com/document/development/search-shifts-by-rank"
namespace: "development"
slug: "search-shifts-by-rank"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤班次 > 按名称搜索班次"
doc_id: "VDR2Owy0Ox"
updated_at: "2026-05-27 17:06:00"
---

> Source: https://open.dingtalk.com/document/development/search-shifts-by-rank
> Path: 应用开发 / 服务端API / 考勤 > 考勤班次 > 按名称搜索班次
> Updated: 2026-05-27 17:06:00

# 按名称搜索班次

调用本接口，根据名称模糊搜索班次，返回班次名称和ID信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/shift/search |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 是 | manager4220 | 操作人的userId。 |
| shift\_name | String | 是 | A | 班次名称。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/shift/search" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=ab85bxxxx739d5' \
-d 'op_user_id=dd_dd' \
-d 'shift_name=%E5%B8%B8%E7%99%BD%E7%8F%AD'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/search");
OapiAttendanceShiftSearchRequest req = new OapiAttendanceShiftSearchRequest();
req.setOpUserId("dd_dd");
req.setShiftName("常白班");
OapiAttendanceShiftSearchResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceShiftSearchRequest("https://oapi.dingtalk.com/topapi/attendance/shift/search")

req.op_user_id="dd_dd"
req.shift_name="常白班"
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
$req = new OapiAttendanceShiftSearchRequest;
$req->setOpUserId("dd_dd");
$req->setShiftName("常白班");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/shift/search");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/search");
OapiAttendanceShiftSearchRequest req = new OapiAttendanceShiftSearchRequest();
req.OpUserId = "dd_dd";
req.ShiftName = "常白班";
OapiAttendanceShiftSearchResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | TopMinimalismShiftVO[] |  | 查询结果。 |
| name | String | 常白班 | 班次名称。 |
| id | Number | 677995086 | 班次ID。 |
| success | Boolean | true | 是否成功标记。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码信息。 |
| request\_id | String | 4wsw01tcq1h4 | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": [
    {
      "id": 677995086,
      "name": "常白班"
    }
  ],
  "success": true,
  "request_id": "4wsw01tcq1h4"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
