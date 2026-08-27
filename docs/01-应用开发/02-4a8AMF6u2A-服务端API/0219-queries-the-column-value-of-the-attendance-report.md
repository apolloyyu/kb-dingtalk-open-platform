---
title: "获取考勤报表列值"
source_url: "https://open.dingtalk.com/document/development/queries-the-column-value-of-the-attendance-report"
namespace: "development"
slug: "queries-the-column-value-of-the-attendance-report"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤统计 > 获取考勤报表列值"
doc_id: "9qdK9MIwfy"
updated_at: "2026-05-27 18:39:10"
---

> Source: https://open.dingtalk.com/document/development/queries-the-column-value-of-the-attendance-report
> Path: 应用开发 / 服务端API / 考勤 > 考勤统计 > 获取考勤报表列值
> Updated: 2026-05-27 18:39:10

# 获取考勤报表列值

调用本接口，获取钉钉智能考勤报表的列值数据，其中包含了一定时间段内报表某一列的所有数据，以及相关的列信息，可以供指定的ISV进行使用。

## **接口调用说明**

- 不支持获取离职人员的考勤信息，离职人员的考勤数据可以在[OA管理后台](https://attend.dingtalk.com/portal/index.html)查询。
- 本接口获取应出勤天数字段值，只支持获取距今15天内的应出勤天数value值，超过15天后的应出勤天数value值为0。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/getcolumnval |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager4220 | 用户的userId。 |
| column\_id\_list | String | 是 | 129339038 | 报表列ID，可通过[获取考勤报表列定义](0218-queries-the-enterprise-attendance-report-column.md)接口获取id参数值。多值用英文逗号分隔，最大长度20。 |
| from\_date | Date | 是 | 2018-07-11 12:12:12 | 开始时间。 |
| to\_date | Date | 是 | 2018-07-11 12:12:12 | 结束时间，结束时间减去开始时间必须在31天以内。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/getcolumnval" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=4bfc0fxxxx3916c7' \
-d 'column_id_list=1%2C2%2C3' \
-d 'from_date=2018-07-11+12%3A12%3A12' \
-d 'to_date=2018-07-11+12%3A12%3A12' \
-d 'userid=zhangsan'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getcolumnval");
OapiAttendanceGetcolumnvalRequest req = new OapiAttendanceGetcolumnvalRequest();
req.setUserid("manager4220");
req.setColumnIdList("129339038");
req.setFromDate(StringUtils.parseDateTime("2020-09-07 12:12:12"));
req.setToDate(StringUtils.parseDateTime("2020-09-09 12:12:12"));
OapiAttendanceGetcolumnvalResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGetcolumnvalRequest("https://oapi.dingtalk.com/topapi/attendance/getcolumnval")

req.userid="zhangsan"
req.column_id_list="1,2,3"
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
$req = new OapiAttendanceGetcolumnvalRequest;
$req->setUserid("zhangsan");
$req->setColumnIdList("1,2,3");
$req->setFromDate("2018-07-11 12:12:12");
$req->setToDate("2018-07-11 12:12:12");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/getcolumnval");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getcolumnval");
OapiAttendanceGetcolumnvalRequest req = new OapiAttendanceGetcolumnvalRequest();
req.Userid = "zhangsan";
req.ColumnIdList = "1,2,3";
req.FromDate = DateTime.Parse("2018-07-11 12:12:12");
req.ToDate = DateTime.Parse("2018-07-11 12:12:12");
OapiAttendanceGetcolumnvalResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 45n2azecqj21 | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| result | ColumnValListForTopVo |  | 返回结果。 |
| column\_vals | ColumnValForTopVo[] |  | 列信息与列值数据。 |
| column\_vals | ColumnDayAndVal[] |  | 列值数据。 |
| date | Date | 2020-09-09 00:00:00 | 日期。 |
| value | String | 1.0 | 列值。 |
| column\_vo | ColumnForTopVo |  | 列信息。 |
| id | Number | 129339038 | 报表列ID。 |
| fixed\_value | String | 0 | 固定值。  **[!NOTE]**  某些报表列是固定列值的，那么仅会在这个字段返回，不会在column\_vals中返回。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "column_vals": [
      {
        "column_vals": [
          {
            "date": "2020-09-07 00:00:00",
            "value": "1.0"
          },
          {
            "date": "2020-09-08 00:00:00",
            "value": "1.0"
          },
          {
            "date": "2020-09-09 00:00:00",
            "value": "1.0"
          }
        ],
        "column_vo": {
          "id": 129339038
        }
      }
    ]
  },
  "request_id": "45n2azecqj21"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
