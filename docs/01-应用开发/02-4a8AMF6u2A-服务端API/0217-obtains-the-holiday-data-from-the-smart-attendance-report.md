---
title: "获取报表假期数据"
source_url: "https://open.dingtalk.com/document/development/obtains-the-holiday-data-from-the-smart-attendance-report"
namespace: "development"
slug: "obtains-the-holiday-data-from-the-smart-attendance-report"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤统计 > 获取报表假期数据"
doc_id: "94WUTZWXFz"
updated_at: "2026-05-27 17:06:17"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-holiday-data-from-the-smart-attendance-report
> Path: 应用开发 / 服务端API / 考勤 > 考勤统计 > 获取报表假期数据
> Updated: 2026-05-27 17:06:17

# 获取报表假期数据

调用本接口，根据假期名称和用户ID获取钉钉智能考勤报表的假期数据，其中包含了一定时间段内报表假期列的所有数据，由于假期列是一个动态列，因此需要根据假期名称获取数据。

## **接口调用说明**

更多数据开放及消费能力请移至[数据资产平台](../../07-数据资产/01-fIz0pQ6X4y-平台介绍/0001-dataopen-overview.md)。数据资产平台（dPaaS）是为企业提供的统一数据管理平台，基于钉钉构建安全、可扩展、易维护和管理的数据服务，助力业务决策！

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/getleavetimebynames |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager123 | 用户的userId。 |
| leave\_names | String | 是 | 年假 | 假期名称，多个用英文逗号分隔，最大长度20。 |
| from\_date | Date | 是 | 2020-09-09 12:12:12 | 开始时间，不支持获取 225 天之前的数据。 |
| to\_date | Date | 是 | 2020-09-11 12:12:12 | 结束时间，结束时间减去开始时间必须在31天以内。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/getleavetimebynames" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=1b8b85xxxxx3ccfdd' \
-d 'from_date=2018-07-11+12%3A12%3A12' \
-d 'leave_names=%E5%B9%B4%E5%81%87' \
-d 'to_date=2018-07-11+12%3A12%3A12' \
-d 'userid=zhangsan'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getleavetimebynames");
OapiAttendanceGetleavetimebynamesRequest req = new OapiAttendanceGetleavetimebynamesRequest();
req.setUserid("zhangsan");
req.setLeaveNames("年假");
req.setFromDate(StringUtils.parseDateTime("2020-09-01 00:00:00"));
req.setToDate(StringUtils.parseDateTime("2020-09-30 00:00:00"));
OapiAttendanceGetleavetimebynamesResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGetleavetimebynamesRequest("https://oapi.dingtalk.com/topapi/attendance/getleavetimebynames")

req.userid="zhangsan"
req.leave_names="年假"
req.from_date="2018-07-11 12:12:12"
req.to_date="2018-07-11 12:12:12"
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
$req = new OapiAttendanceGetleavetimebynamesRequest;
$req->setUserid("zhangsan");
$req->setLeaveNames("年假");
$req->setFromDate("2018-07-11 12:12:12");
$req->setToDate("2018-07-11 12:12:12");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/getleavetimebynames");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getleavetimebynames");
OapiAttendanceGetleavetimebynamesRequest req = new OapiAttendanceGetleavetimebynamesRequest();
req.Userid = "zhangsan";
req.LeaveNames = "年假";
req.FromDate = DateTime.Parse("2018-07-11 12:12:12");
req.ToDate = DateTime.Parse("2018-07-11 12:12:12");
OapiAttendanceGetleavetimebynamesResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ColumnValListForTopVo |  | 返回结果。 |
| columns | ColumnValForTopVo[] |  | 列信息与列值数据。 |
| columnvo | ColumnForTopVo |  | 列信息。 |
| name | String | 事假 | 假期名称。 |
| sub\_type | Number | 0 | 子类型。 |
| status | Number | 0 | 列状态。 |
| alias | String | leave\_ | 别名。 |
| type | Number | 0 | 列类型。 |
| columnvals | ColumnDayAndVal[] |  | 列值数据。 |
| value | String | 1.0 | 每天的值。 |
| date | Date | 2020-09-09 12:12:12 | 开始时间。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | whv0fhtk8cnc | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "columns": [
      {
        "columnvals": [
          {
            "date": "2020-09-01 00:00:00",
            "value": "0.0"
          },
          {
            "date": "2020-09-02 00:00:00",
            "value": "0.0"                   
          }
        ],
        "columnvo": {
          "alias": "leave_",
          "name": "事假",
          "status": 0,
          "sub_type": 0,
          "type": 0
        }
      }
    ]
  },
  "request_id": "whv0fhtk8cnc"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
