---
title: "查询企业考勤排班详情"
source_url: "https://open.dingtalk.com/document/development/interface-for-daily-full-query-of-attendance-scheduling-information"
namespace: "development"
slug: "interface-for-daily-full-query-of-attendance-scheduling-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤排班 > 查询企业考勤排班详情"
doc_id: "ZaRiz3wUGd"
updated_at: "2026-05-27 17:06:14"
---

> Source: https://open.dingtalk.com/document/development/interface-for-daily-full-query-of-attendance-scheduling-information
> Path: 应用开发 / 服务端 API / 考勤 > 考勤排班 > 查询企业考勤排班详情
> Updated: 2026-05-27 17:06:14

# 查询企业考勤排班详情

调用本接口，查询企业某天所有员工考勤班次信息和排班信息等。

## **接口调用说明**

- 固定班制只能查到未来15天的排班信息。
- 本接口仅支持企业总人数10000人以下使用。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/listschedule |
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
| workDate | Date | 是 | 2020-09-06 | 排班时间，只取年月日部分。 |
| offset | Number | 否 | 0 | 支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。 |
| size | Number | 否 | 200 | 分页大小，最大值200。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/listschedule" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=b9305xxxxea83' \
-d 'offset=0' \
-d 'size=200' \
-d 'workDate=2016-03-09+11%3A11%3A11'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/listschedule");
OapiAttendanceListscheduleRequest req = new OapiAttendanceListscheduleRequest();
req.setWorkDate(StringUtils.parseDateTime("2016-03-09 11:11:11"));
req.setOffset(0L);
req.setSize(200L);
OapiAttendanceListscheduleResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceListscheduleRequest("https://oapi.dingtalk.com/topapi/attendance/listschedule")

req.workDate="2016-03-09 11:11:11"
req.offset=0
req.size=200
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
$req = new OapiAttendanceListscheduleRequest;
$req->setWorkDate("2016-03-09 11:11:11");
$req->setOffset("0");
$req->setSize("200");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/listschedule");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/listschedule");
OapiAttendanceListscheduleRequest req = new OapiAttendanceListscheduleRequest();
req.WorkDate = DateTime.Parse("2016-03-09 11:11:11");
req.Offset = 0L;
req.Size = 200L;
OapiAttendanceListscheduleResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | AtScheduleListForTopVo |  | 查询结果。 |
| schedules | AtScheduleForTopVo[] |  | 排班表。 |
| plan\_id | Number | 157062792171 | 排班ID。 |
| check\_type | String | OnDuty | 打卡类型：   - **Onduty**：上班打卡 - **OffDuty**：下班打卡 |
| approve\_id | Number | 1 | 审批ID。  **[!NOTE]**  没有审批单则不返回该参数。 |
| userid | String | user01 | 考勤的用户userId。 |
| class\_id | Number | 677995086 | 考勤班次ID。 |
| class\_setting\_id | Number | 599315627 | 班次配置ID。  **[!NOTE]**  使用全局配置则不返回该参数。 |
| plan\_check\_time | Date | 2020-11-11 09:30:00 | 打卡时间。 |
| group\_id | Number | 685935028 | 考勤组ID。 |
| changed\_check\_time | Date | 2020-09-06 15:36:04 | 调整后的卡点时间。 |
| has\_more | Boolean | false | 是否还有下一页。   - **true**：有 - **false**：没有 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 6ha75i2o99fj | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "has_more": false,
    "schedules": [
      {
        "check_type": "OnDuty",
        "class_id": 677995086,
        "class_setting_id": 599315627,
        "group_id": 685935028,
        "plan_check_time": "2020-11-11 09:30:00",
        "plan_id": 157062792171,
        "userid": "user01"
      },
      {
        "check_type": "OffDuty",
        "class_id": 677995086,
        "class_setting_id": 599315627,
        "group_id": 685935028,
        "plan_check_time": "2020-11-11 18:30:00",
        "plan_id": 157062792172,
        "userid": "user01"
      }
    ]
  },
  "request_id": "6ha75i2o99fj"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
