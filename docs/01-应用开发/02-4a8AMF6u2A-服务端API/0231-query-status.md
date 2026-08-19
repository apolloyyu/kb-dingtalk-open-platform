---
title: "查询请假状态"
source_url: "https://open.dingtalk.com/document/development/query-status"
namespace: "development"
slug: "query-status"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 假勤审批 > 查询请假状态"
doc_id: "1DFxFzoUPK"
updated_at: "2026-05-27 17:06:25"
---

> Source: https://open.dingtalk.com/document/development/query-status
> Path: 应用开发 / 服务端API / 考勤 > 假勤审批 > 查询请假状态
> Updated: 2026-05-27 17:06:25

# 查询请假状态

调用本接口，查询指定企业下指定用户在指定时间段内每天的请假状态和请假时长信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/getleavestatus |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_attendance\_data-考勤数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid\_list | String | 是 | user456,user123 | 待查询用户的ID列表，每次最多100个。 |
| start\_time | Number | 是 | 1538323200000 | 开始时间 ，Unix时间戳，支持最多180天的查询。 |
| end\_time | Number | 是 | 1546358399000 | 结束时间，Unix时间戳，支持最多180天的查询。 |
| offset | Number | 是 | 0 | 支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。 |
| size | Number | 是 | 10 | 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大20。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/getleavestatus" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=11b9xxxxc35a' \
-d 'end_time=1546358399000' \
-d 'offset=0' \
-d 'size=10' \
-d 'start_time=1538323200000' \
-d 'userid_list=123%2C121'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getleavestatus");
OapiAttendanceGetleavestatusRequest req = new OapiAttendanceGetleavestatusRequest();
req.setUseridList("user123,user456");
req.setStartTime(1538323200000L);
req.setEndTime(1546358399000L);
req.setOffset(0L);
req.setSize(10L);
OapiAttendanceGetleavestatusResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGetleavestatusRequest("https://oapi.dingtalk.com/topapi/attendance/getleavestatus")

req.userid_list="123,121"
req.start_time=1538323200000
req.end_time=1546358399000
req.offset=0
req.size=10
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
$req = new OapiAttendanceGetleavestatusRequest;
$req->setUseridList("123,121");
$req->setStartTime("1538323200000");
$req->setEndTime("1546358399000");
$req->setOffset("0");
$req->setSize("10");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/getleavestatus");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getleavestatus");
OapiAttendanceGetleavestatusRequest req = new OapiAttendanceGetleavestatusRequest();
req.UseridList = "123,121";
req.StartTime = 1538323200000L;
req.EndTime = 1546358399000L;
req.Offset = 0L;
req.Size = 10L;
OapiAttendanceGetleavestatusResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| result | LeaveStatusListVO |  | 查询结果。 |
| has\_more | Boolean | true | 是否有更多数据。   - **true**：有 - **false**：没有 |
| leave\_status | LeaveStatusVO[] |  | 请假状态列表。 |
| duration\_unit | String | percent\_day | 请假单位：   - **percent\_day**：天 - **percent\_hour**：小时 |
| duration\_percent | Number | 100 | 假期时长\*100，例如用户请假时长为1天，该值就等于100。 |
| end\_time | Number | 1599465600000 | 请假结束时间，Unix时间戳。 |
| start\_time | Number | 1599372000000 | 请假开始时间，Unix时间戳。 |
| userid | String | user456 | 用户ID。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | 5lbpbi9p1awk | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "has_more": false,
    "leave_status": [
      {
        "duration_percent": 650,
        "duration_unit": "percent_hour",
        "end_time": 1599465600000,
        "start_time": 1599372000000,
        "leave_code":"16f856xxxx09aa16"
        "userid": "user123"
      }
    ]
  },
  "success": true,
  "request_id": "5lbpbi9p1awk"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
