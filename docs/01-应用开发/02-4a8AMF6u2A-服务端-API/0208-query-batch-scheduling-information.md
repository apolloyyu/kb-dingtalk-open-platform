---
title: "批量查询人员排班信息"
source_url: "https://open.dingtalk.com/document/development/query-batch-scheduling-information"
namespace: "development"
slug: "query-batch-scheduling-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤排班 > 批量查询人员排班信息"
doc_id: "Op0Pn7ADZD"
updated_at: "2026-05-27 17:06:10"
---

> Source: https://open.dingtalk.com/document/development/query-batch-scheduling-information
> Path: 应用开发 / 服务端 API / 考勤 > 考勤排班 > 批量查询人员排班信息
> Updated: 2026-05-27 17:06:10

# 批量查询人员排班信息

调用本接口，批量查询员工在某天的排班信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/schedule/listbyusers |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 是 | user456 | 操作人userId。 |
| userids | String | 是 | user123 | 要查询的人员userId列表，多个userId用逗号分隔，一次最多可传50个。 |
| from\_date\_time | Number | 是 | 1565591096000 | 起始日期，Unix时间戳，单位毫秒。  **[!NOTE]**   - 开始时间和结束时间的间隔不能超过7天。 - 查询时间限制距今180天内。 |
| to\_date\_time | Number | 是 | 1565591096000 | 结束日期，Unix时间戳，单位毫秒。  **[!NOTE]**   - 开始时间和结束时间的间隔不能超过7天。 - 查询时间限制距今180天内。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/schedule/listbyusers" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=9ad3xxxx82a10' \
-d 'from_date_time=1565591096000' \
-d 'op_user_id=dd_dd' \
-d 'to_date_time=1565591096000' \
-d 'userids=dd_dd%2Cduogui'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/schedule/listbyusers");
OapiAttendanceScheduleListbyusersRequest req = new OapiAttendanceScheduleListbyusersRequest();
req.setOpUserId("user456");
req.setUserids("user123,user456");
req.setFromDateTime(1565591096000L);
req.setToDateTime(1565591096000L);
OapiAttendanceScheduleListbyusersResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceScheduleListbyusersRequest("https://oapi.dingtalk.com/topapi/attendance/schedule/listbyusers")

req.op_user_id="dd_dd"
req.userids="dd_dd,duogui"
req.from_date_time=1565591096000
req.to_date_time=1565591096000
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
$req = new OapiAttendanceScheduleListbyusersRequest;
$req->setOpUserId("dd_dd");
$req->setUserids("dd_dd,duogui");
$req->setFromDateTime("1565591096000");
$req->setToDateTime("1565591096000");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/schedule/listbyusers");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/schedule/listbyusers");
OapiAttendanceScheduleListbyusersRequest req = new OapiAttendanceScheduleListbyusersRequest();
req.OpUserId = "dd_dd";
req.Userids = "dd_dd,duogui";
req.FromDateTime = 1565591096000L;
req.ToDateTime = 1565591096000L;
OapiAttendanceScheduleListbyusersResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | TopScheduleVo[] | demo | 查询结果。 |
| check\_type | String | OnDuty | 考勤类型：   - **Onduty**：上班打卡 - **OffDuty**：下班打卡 |
| plan\_check\_time | Date | 2021-01-14 09:00:00 | 计划打卡时间。 |
| group\_id | Number | 394775001 | 考勤组ID。 |
| userid | String | user456 | 用户userId。 |
| approve\_id | Number | 1234 | 排班绑定的审批单ID。  **[!NOTE]**  如果当天没有审批单，则不返回该字段。 |
| work\_date | Date | 2021-01-14 00:00:00 | 工作日，代表具体哪一天的排班。 |
| id | Number | 56676915454 | 排班ID。 |
| shift\_version | Number | 588655171 | 班次版本。 |
| shift\_id | Number | 677995086 | 班次ID，该值为0，表明当天休息。 |
| is\_rest | String | N | 是否休息：   - **Y**：当天排休 - **N**：当天不休息 |
| success | Boolean | true | 是否成功标记。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回信息。 |
| request\_id | String | qkqbwcw3bq2 | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": [
    {
      "check_type": "OnDuty",
      "group_id": 394775001,
      "id": 56676915454,
      "is_rest": "N",
      "plan_check_time": "2021-01-14 09:00:00",
      "shift_id": 709595172,
      "shift_version": 617320362,
      "userid": "user456",
      "work_date": "2021-01-14 00:00:00"
    },
    {
      "check_type": "OffDuty",
      "group_id": 394775001,
      "id": 56676915454,
      "is_rest": "N",
      "plan_check_time": "2021-01-14 18:00:00",
      "shift_id": 709595172,
      "shift_version": 617320362,
      "userid": "user456",
      "work_date": "2021-01-14 00:00:00"
    }
  ],
  "success": true,
  "request_id": "4cmy9twx4atn"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
