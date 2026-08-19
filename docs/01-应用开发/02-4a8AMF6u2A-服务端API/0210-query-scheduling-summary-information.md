---
title: "批量查询成员排班概要信息"
source_url: "https://open.dingtalk.com/document/development/query-scheduling-summary-information"
namespace: "development"
slug: "query-scheduling-summary-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤排班 > 批量查询成员排班概要信息"
doc_id: "SPTRTU9cJH"
updated_at: "2026-05-27 17:06:13"
---

> Source: https://open.dingtalk.com/document/development/query-scheduling-summary-information
> Path: 应用开发 / 服务端API / 考勤 > 考勤排班 > 批量查询成员排班概要信息
> Updated: 2026-05-27 17:06:13

# 批量查询成员排班概要信息

调用本接口，查询用户在某个时间段内的排班概要信息，包括班次名称、班次版本ID、考勤组ID等内容。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/schedule/shift/listbydays |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 57cf92xxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 是 | manager123 | 操作者的userId。 |
| userids | String | 是 | user123,user456 | 需要查询的用户userId列表，多个userId之间使用逗号分隔，且每次查询最多不能超过20。 |
| from\_date\_time | Number | 是 | 1564985177000 | 开始日期的Unix时间戳，单位毫秒。  **[!NOTE]**  时间跨度不能超过7天。 |
| to\_date\_time | Number | 是 | 1564985177000 | 结束日期的Unix时间戳，单位毫秒。  **[!NOTE]**  时间跨度不能超过7天。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/schedule/shift/listbydays" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=ecff22xxxx1f8d5d' \
-d 'from_date_time=1564985177000' \
-d 'op_user_id=dd_dd' \
-d 'to_date_time=1564985177000' \
-d 'userids=dd_test%2Ctl2342'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/schedule/shift/listbydays");
OapiAttendanceScheduleShiftListbydaysRequest req = new OapiAttendanceScheduleShiftListbydaysRequest();
req.setOpUserId("manager123");
req.setUserids("user123,user456");
req.setFromDateTime(1564985177000L);
req.setToDateTime(1564985177000L);
OapiAttendanceScheduleShiftListbydaysResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceScheduleShiftListbydaysRequest("https://oapi.dingtalk.com/topapi/attendance/schedule/shift/listbydays")

req.op_user_id="dd_dd"
req.userids="dd_test,tl2342"
req.from_date_time=1564985177000
req.to_date_time=1564985177000
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
$req = new OapiAttendanceScheduleShiftListbydaysRequest;
$req->setOpUserId("dd_dd");
$req->setUserids("dd_test,tl2342");
$req->setFromDateTime("1564985177000");
$req->setToDateTime("1564985177000");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/schedule/shift/listbydays");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/schedule/shift/listbydays");
OapiAttendanceScheduleShiftListbydaysRequest req = new OapiAttendanceScheduleShiftListbydaysRequest();
req.OpUserId = "dd_dd";
req.Userids = "dd_test,tl2342";
req.FromDateTime = 1564985177000L;
req.ToDateTime = 1564985177000L;
OapiAttendanceScheduleShiftListbydaysResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | TopDayScheduleShiftVo[] |  | 返回结果列表。 |
| work\_date | Date | 2020-12-14 00:00:00 | 工作日。 |
| shift\_names | String[] | ["A"] | 班次名称。 |
| userid | String | user123 | 用户的userId。 |
| shift\_versions | Number[] | [9527] | 班次版本ID。 |
| shift\_ids | Number[] | [9087] | 班次ID。 |
| group\_id | Number | 7786 | 考勤组ID。 |
| corp\_id | String | dinge8xxx | 企业的corpId。 |
| success | Boolean | true | 调用是否成功的标记。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 5fyefrdh2mf4 | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": [
    {
      "corp_id": "dinge8xxx",
      "group_id": 685935028,
      "shift_ids": [
        677995086
      ],
      "shift_names": [
        "A"
      ],
      "shift_versions": [
        603766106
      ],
      "userid": "user456",
      "work_date": "2020-12-14 00:00:00"
    }
  ],
  "success": true,
  "request_id": "5fyefrdh2mf4"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
