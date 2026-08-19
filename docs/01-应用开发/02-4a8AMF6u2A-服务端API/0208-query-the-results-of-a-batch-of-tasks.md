---
title: "查询排班打卡结果"
source_url: "https://open.dingtalk.com/document/development/query-the-results-of-a-batch-of-tasks"
namespace: "development"
slug: "query-the-results-of-a-batch-of-tasks"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤排班 > 查询排班打卡结果"
doc_id: "EQlywHegFv"
updated_at: "2026-05-27 17:06:11"
---

> Source: https://open.dingtalk.com/document/development/query-the-results-of-a-batch-of-tasks
> Path: 应用开发 / 服务端API / 考勤 > 考勤排班 > 查询排班打卡结果
> Updated: 2026-05-27 17:06:11

# 查询排班打卡结果

调用本接口，根据排班ID查询对应的排班打卡结果，获取考勤类型、计划打卡时间、最后更新时间等信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/schedule/result/listbyids |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 是 | manager123 | 操作人userId。 |
| schedule\_ids | String | 是 | 144872188723,144872188722 | 排班ID，通过[查询企业考勤排班详情](0209-interface-for-daily-full-query-of-attendance-scheduling-information.md)接口获取plan\_id参数值。多个排班ID之间用逗号分割，每次调用最多支持100个排班ID， |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/schedule/result/listbyids" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=711cexxxx8ce772' \
-d 'op_user_id=dd_dd' \
-d 'schedule_ids=1234%2C3214'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/schedule/result/listbyids");
OapiAttendanceScheduleResultListbyidsRequest req = new OapiAttendanceScheduleResultListbyidsRequest();
req.setOpUserId("user456");
req.setScheduleIds("16xxxx530,160xxxx12");
OapiAttendanceScheduleResultListbyidsResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceScheduleResultListbyidsRequest("https://oapi.dingtalk.com/topapi/attendance/schedule/result/listbyids")

req.op_user_id="dd_dd"
req.schedule_ids="[1234,3214]"
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
$req = new OapiAttendanceScheduleResultListbyidsRequest;
$req->setOpUserId("dd_dd");
$req->setScheduleIds("[1234,3214]");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/schedule/result/listbyids");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/schedule/result/listbyids");
OapiAttendanceScheduleResultListbyidsRequest req = new OapiAttendanceScheduleResultListbyidsRequest();
req.OpUserId = "dd_dd";
req.ScheduleIds = "1234,3214";
OapiAttendanceScheduleResultListbyidsResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | TopScheduleResultVo[] | demo | 查询结果。 |
| check\_type | String | OnDuty | 考勤类型：   - **Onduty**：上班打卡 - **OffDuty**：下班打卡 |
| gmt\_modified | Date | 2020-11-11 19:03:21 | 最后更新时间。 |
| plan\_check\_time | Date | 2020-11-11 19:03:20 | 计划打卡时间。 |
| corp\_id | String | dingxxxxx1c1 | 企业的corpId。 |
| base\_check\_time | Date | 2020-11-11 19:03:00 | 允许迟到早退等规则调整后的计划打卡时间。 |
| group\_id | Number | 67xxxx4 | 考勤组ID。 |
| gmt\_create | Date | 2020-11-11 19:03:21 | 创建时间。 |
| user\_id | String | user123 | 用户的userId。 |
| work\_date | Date | 2020-11-11 00:00:00 | 工作日，代表具体哪一天的排班。 |
| id | Number | 11xxxx19 | 打卡结果ID。 |
| location\_result | String | Normal | 打卡位置结果：   - **Normal**：正常打卡 - **NotSigned**：未打卡 - **Outside**：外勤 |
| is\_legal | String | Y | 打卡是否有异常：   - **N**：没有 - **Y**：有 |
| time\_result | String | Normal | 打卡时间结果：   - **Normal**：正常打卡 - **NotSigned**：未打卡 - **Late**：迟到 - **SeriousLate**：严重迟到 - **Absenteeism**：旷工迟到 - **Early**：早退 |
| record\_id | Number | 48xxxx644 | 打卡记录。 |
| user\_check\_time | Date | 2020-11-11 19:03:20 | 打卡时间。 |
| schedule\_id | Number | 5672xxxx63 | 排班ID。 |
| success | Boolean | true | 是否成功标记。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 6k9c3cvix353 | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": [
    {
      "base_check_time": "2020-11-11 19:03:00",
      "check_type": "OnDuty",
      "corp_id": "dingxxxxx1c1",
      "gmt_create": "2020-11-11 19:03:21",
      "gmt_modified": "2020-11-11 19:03:21",
      "group_id": 67xxxx4,
      "id": 11xxxx19,
      "is_legal": "Y",
      "location_result": "Normal",
      "plan_check_time": "2020-11-11 19:03:20",
      "record_id": 48xxxx644,
      "schedule_id": 16xxxx812,
      "time_result": "Normal",
      "user_check_time": "2020-11-11 19:03:20",
      "user_id": "user456",
      "work_date": "2020-11-11 00:00:00"
    }
  ],
  "success": true,
  "request_id": "6k9c3cvix353"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
