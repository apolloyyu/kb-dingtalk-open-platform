---
title: "计算请假时长"
source_url: "https://open.dingtalk.com/document/development/calculate-leave-duration"
namespace: "development"
slug: "calculate-leave-duration"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 假勤审批 > 计算请假时长"
doc_id: "SPDtnro01v"
updated_at: "2026-05-27 17:06:24"
---

> Source: https://open.dingtalk.com/document/development/calculate-leave-duration
> Path: 应用开发 / 服务端API / 考勤 > 假勤审批 > 计算请假时长
> Updated: 2026-05-27 17:06:24

# 计算请假时长

调用本接口，获取自动根据排班规则统计出每个员工的请假时长。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/getleaveapproveduration |
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
| userid | String | 是 | user123 | 员工在企业内的userId，企业用来唯一标识用户的字段。 |
| from\_date | Date | 是 | 2016-03-09 11:11:11 | 请假开始时间。 |
| to\_date | Date | 是 | 2016-03-10 11:11:11 | 请假结束时间。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/getleaveapproveduration" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=6777xxxx6f4eff' \
-d 'from_date=2016-03-09+11%3A11%3A11' \
-d 'to_date=2016-03-10+11%3A11%3A11' \
-d 'userid=zhangsan'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getleaveapproveduration");
OapiAttendanceGetleaveapprovedurationRequest req = new OapiAttendanceGetleaveapprovedurationRequest();
req.setUserid("user123");
req.setFromDate(StringUtils.parseDateTime("2016-03-09 11:11:11"));
req.setToDate(StringUtils.parseDateTime("2016-03-10 11:11:11"));
OapiAttendanceGetleaveapprovedurationResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGetleaveapprovedurationRequest("https://oapi.dingtalk.com/topapi/attendance/getleaveapproveduration")

req.userid="zhangsan"
req.from_date="2016-03-09 11:11:11"
req.to_date="2016-03-10 11:11:11"
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
$req = new OapiAttendanceGetleaveapprovedurationRequest;
$req->setUserid("zhangsan");
$req->setFromDate("2016-03-09 11:11:11");
$req->setToDate("2016-03-10 11:11:11");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/getleaveapproveduration");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getleaveapproveduration");
OapiAttendanceGetleaveapprovedurationRequest req = new OapiAttendanceGetleaveapprovedurationRequest();
req.Userid = "zhangsan";
req.FromDate = DateTime.Parse("2016-03-09 11:11:11");
req.ToDate = DateTime.Parse("2016-03-10 11:11:11");
OapiAttendanceGetleaveapprovedurationResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ApproveDurationForTopVo |  | 返回结果。 |
| duration\_in\_minutes | Number | 0 | 请假时长，单位分钟。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 3ynh2gp5ndke | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "duration_in_minutes": 480
  },
  "request_id": "6porp1hqkb9k"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
