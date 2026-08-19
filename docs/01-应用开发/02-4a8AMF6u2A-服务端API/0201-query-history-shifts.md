---
title: "查询历史班次"
source_url: "https://open.dingtalk.com/document/development/query-history-shifts"
namespace: "development"
slug: "query-history-shifts"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤班次 > 查询历史班次"
doc_id: "27rEmb6iBd"
updated_at: "2026-05-27 17:05:59"
---

> Source: https://open.dingtalk.com/document/development/query-history-shifts
> Path: 应用开发 / 服务端API / 考勤 > 考勤班次 > 查询历史班次
> Updated: 2026-05-27 17:05:59

# 查询历史班次

调用本接口，根据班次ID和version查询历史班次信息，包括历史班次信息，如班次名称、班次设置、打卡时间、休息时间等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/shift/history/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 73e9xxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 是 | user123 | 操作者userId。 |
| shift\_id | Number | 是 | 628380875 | 班次ID，可通过[获取班次摘要信息](0203-enterprise-shift-query-in-batches.md)接口获取id参数值。 |
| version | Number | 是 | 624190327 | 班次版本，可通过[批量查询人员排班信息](0206-query-batch-scheduling-information.md)接口获取shift\_version参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/shift/history/query" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=e56f7xxxxeb7ef1' \
-d 'op_user_id=dd_dd' \
-d 'shift_id=2445' \
-d 'version=222'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/history/query");
OapiAttendanceShiftHistoryQueryRequest req = new OapiAttendanceShiftHistoryQueryRequest();
req.setOpUserId("user456");
req.setShiftId(715390132L);
req.setVersion(624190327L);
OapiAttendanceShiftHistoryQueryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceShiftHistoryQueryRequest("https://oapi.dingtalk.com/topapi/attendance/shift/history/query")

req.op_user_id="dd_dd"
req.shift_id=2445
req.version=222
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
$req = new OapiAttendanceShiftHistoryQueryRequest;
$req->setOpUserId("dd_dd");
$req->setShiftId("2445");
$req->setVersion("222");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/shift/history/query");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/history/query");
OapiAttendanceShiftHistoryQueryRequest req = new OapiAttendanceShiftHistoryQueryRequest();
req.OpUserId = "dd_dd";
req.ShiftId = 2445L;
req.Version = 222L;
OapiAttendanceShiftHistoryQueryResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | TopShiftVo |  | 查询结果。 |
| shift\_group\_name | String | 常白班 | 班次组名称。 |
| corp\_id | String | dinge87fxxx | 企业的corpId。 |
| shift\_setting | TopShiftSettingVo |  | 班次设置。 |
| shift\_id | Number | 628380875 | 班次ID。 |
| gmt\_modified | Date | 2021-01-14 14:21:03 | 班次变更时间。 |
| corp\_id | String | dinge87fxxx | 企业的corpId。 |
| is\_deleted | String | N | 删除标记。 |
| work\_time\_minutes | Number | 480 | 工作时长，单位分钟，-1表示关闭该功能。 |
| id | Number | 350530359 | 班次设置ID，暂无使用场景。 |
| attend\_days | String | 21 | 该班次对应的出勤天数。 |
| gmt\_create | Date | 2021-01-14 14:18:08 | 创建时间。 |
| name | String | 常白班 | 班次名称。 |
| id | Number | 241120079 | 班次ID。 |
| sections | TopSectionVo[] |  | 卡段。 |
| punches | TopPunchVo[] |  | 卡点。 |
| check\_type | String | OnDuty | 打卡类型：   - **OnDuty**：上班 - **OffDuty**：下班 |
| end\_min | Number | 1 | 允许的最晚延后打卡时间，单位分钟。 |
| across | Number | 0 | 是否跨天：   - **0**：不跨天 - **1**：跨天 |
| check\_time | Date | 1970-01-01 09:00:00 | 打卡时间。 |
| permit\_minutes | Number | 60 | 允许早退或迟到的时长。 |
| free\_check | Boolean | false | 是否免打卡：   - **true**：免打卡 - **false**：需打卡 |
| id | Number | 376955859 | 卡点ID，暂时无使用场景。 |
| begin\_min | Number | demo | 允许的最早提前打卡时间，单位分钟。 |
| work\_time\_minutes | Number | 480 | 工作时长，单位分钟。 |
| rests | TopRestVo[] |  | 休息段。 |
| check\_type | String | OnDuty | 休息类型：   - **OnDuty**：休息开始 - **OffDuty**：休息结束 |
| across | Number | 0 | 是否跨天，跨天是指休息时间是第二天：   - **0**：不跨天 - **1**：跨天 |
| check\_time | Date | 1970-01-01 12:00:00 | 休息时间。 |
| id | Number | 376955861 | 休息点ID。 |
| id | Number | 22979360 | 卡段ID。一次上下班成为一个卡段，一个班次可能会有多个卡段。 |
| shift\_group\_id | Number | 22979 | 班组ID。 |
| success | Boolean | true | 调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | q3ef3y3sogkd | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "corp_id": "dinge87fxxx",
    "id": 628380875,
    "name": "常白班",
    "sections": [
      {
        "id": 350530359,
        "punches": [
          {
            "across": 0,
            "begin_min": 1,
            "check_time": "1970-01-01 09:00:00",
            "check_type": "OnDuty",
            "end_min": 1,
            "free_check": false,
            "id": 376955859,
            "permit_minutes": 60
          },
          {
            "across": 0,
            "begin_min": 1,
            "check_time": "1970-01-01 18:00:00",
            "check_type": "OffDuty",
            "end_min": 1,
            "free_check": false,
            "id": 376955860,
            "permit_minutes": 15
          }
        ],
        "rests": [
          {
            "across": 0,
            "check_time": "1970-01-01 12:00:00",
            "check_type": "OnDuty",
            "id": 376955861
          },
          {
            "across": 0,
            "check_time": "1970-01-01 13:00:00",
            "check_type": "OffDuty",
            "id": 376955862
          }
        ]
      }
    ],
    "shift_setting": {
      "corp_id": "dinge87fxxx",
      "gmt_create": "2021-01-14 14:18:08",
      "gmt_modified": "2021-01-14 14:21:03",
      "id": 624190327,
      "is_deleted": "N",
      "shift_id": 628380875,
      "work_time_minutes": 480
    }
  },
  "success": true,
  "request_id": "q3ef3y3sogkd"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
