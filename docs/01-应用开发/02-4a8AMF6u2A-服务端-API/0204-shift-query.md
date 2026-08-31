---
title: "获取班次详情"
source_url: "https://open.dingtalk.com/document/development/shift-query"
namespace: "development"
slug: "shift-query"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤班次 > 获取班次详情"
doc_id: "6QEvezLhmC"
updated_at: "2026-05-27 17:06:03"
---

> Source: https://open.dingtalk.com/document/development/shift-query
> Path: 应用开发 / 服务端 API / 考勤 > 考勤班次 > 获取班次详情
> Updated: 2026-05-27 17:06:03

# 获取班次详情

调用本接口，根据班次ID查询班次的详细信息，如班次名称、打卡时间、休息时段等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/shift/query |
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
| op\_user\_id | String | 是 | user123 | 操作者的userId。 |
| shift\_id | Number | 是 | 678215070 | 班次ID，可通过[获取班次摘要信息](0203-enterprise-shift-query-in-batches.md)接口获取id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/shift/query" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=d946568c-08dd-44bf-acd3-cfc07d7829dd' \
-d 'op_user_id=dd_dd' \
-d 'shift_id=2445'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/query");
OapiAttendanceShiftQueryRequest req = new OapiAttendanceShiftQueryRequest();
req.setOpUserId("user123");
req.setShiftId(678215070L);
OapiAttendanceShiftQueryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceShiftQueryRequest("https://oapi.dingtalk.com/topapi/attendance/shift/query")

req.op_user_id="dd_dd"
req.shift_id=2445
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
$req = new OapiAttendanceShiftQueryRequest;
$req->setOpUserId("dd_dd");
$req->setShiftId("2445");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/shift/query");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/query");
OapiAttendanceShiftQueryRequest req = new OapiAttendanceShiftQueryRequest();
req.OpUserId = "dd_dd";
req.ShiftId = 2445L;
OapiAttendanceShiftQueryResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | TopShiftVo |  | 班次详情。 |
| shift\_group\_name | String | 考勤班 | 班次组名称。 |
| corp\_id | String | dinge87f1xxxx | 企业的corpId。 |
| shift\_setting | TopShiftSettingVo |  | 班次设置信息。 |
| shift\_id | Number | 678215070 | 班次ID。 |
| gmt\_modified | Date | 2020-09-06 15:49:27 | 班次变更时间。 |
| corp\_id | String | dinge87f1xxxx | 企业的corpId。 |
| work\_time\_minutes | Number | 600 | 工作时长，单位分钟，-1表示关闭该功能。 |
| id | Number | 233840112 | 班次设置ID。 |
| attend\_days | String | 12 | 该班次对应的出勤天数。 |
| gmt\_create | Date | 2020-09-06 15:49:27 | 创建时间。 |
| name | String | B | 班次名称。 |
| id | Number | 678215070 | 班次ID。 |
| sections | TopSectionVo[] |  | 卡段。 |
| punches | TopPunchVo[] |  | 卡点。 |
| check\_type | String | OnDuty | 打卡类型：   - **OnDuty**：上班 - **OffDuty**：下班 |
| end\_min | Number | -1 | 允许的最晚的打卡时间。  单位是分钟，用打卡时间加上分钟数可以计算出最晚打卡时间。 |
| across | Number | 0 | 是否跨天，跨天是指打卡时间是第二天：   - **0**：不跨天 - **1**：跨天 |
| check\_time | Date | 1970-01-01 19:00:00 | 打卡时间，Unix时间戳，仅有时分秒信息。 |
| permit\_minutes | Number | 0 | 允许早退/迟到的时长，单位分钟。 |
| free\_check | Boolean | false | 是否免打卡：   - **true**：免打卡 - **false**：需打卡 |
| id | Number | 33928201 | 卡点ID。 |
| begin\_min | Number | 20 | 允许的最早提前打卡时间，分钟为单位。 |
| absenteeism\_late\_minutes | String | -1 | 旷工早退/迟到的时长，单位分钟。 |
| serious\_late\_minutes | String | -1 | 严重早退/迟到的时长，单位分钟。 |
| rests | TopRestVo[] |  | 休息时段信息。 |
| check\_type | String | OnDuty | 休息类型：   - **OnDuty**：休息开始 - **OffDuty**：休息结束 |
| across | Number | 1 | 是否跨天，跨天是指休息时间是第二天：   - **0**：不跨天 - **1**：跨天 |
| check\_time | String | 1970-01-01 05:00:00 | 休息时间。 |
| id | Number | 33928203 | 休息点ID。 |
| id | Number | 22979360 | 卡段ID。一次上下班成为一个卡段，一个班次可能会有多个卡段。 |
| shift\_group\_id | Number | demo | 班次组ID。 |
| owner | String | user123 | 班次负责人的userId。 |
| success | Boolean | true | 调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | demo | 返回码描述。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "demo",
  "result": {
    "corp_id": "dinge87f1xxxx",
    "id": 678215070,
    "name": "B",
    "sections": [
      {
        "id": 316940162,
        "punches": [
          {
            "absenteeism_late_minutes": "-1",
            "across": 0,
            "check_time": "1970-01-01 19:00:00",
            "check_type": "OnDuty",
            "free_check": false,
            "id": 340055347,
            "permit_minutes": 0,
            "serious_late_minutes": "-1"
          },
          {
            "across": 1,
            "check_time": "1970-01-01 05:00:00",
            "check_type": "OffDuty",
            "free_check": false,
            "id": 340055348
          }
        ],
        "rests": []
      }
    ],
    "shift_setting": {
      "corp_id": "dinge87f1xxxx",
      "gmt_create": "2020-09-06 15:49:27",
      "gmt_modified": "2020-09-06 15:49:27",
      "id": 586985140,
      "is_deleted": "N",
      "shift_id": 678215070,
      "work_time_minutes": 600
    }
  },
  "success": true,
  "request_id": "3pph7tq865kz"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
