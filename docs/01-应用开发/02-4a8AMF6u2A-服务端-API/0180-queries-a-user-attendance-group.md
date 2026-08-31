---
title: "获取用户考勤组"
source_url: "https://open.dingtalk.com/document/development/queries-a-user-attendance-group"
namespace: "development"
slug: "queries-a-user-attendance-group"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤组管理 > 获取用户考勤组"
doc_id: "wHy5x571ML"
updated_at: "2026-05-27 13:09:52"
---

> Source: https://open.dingtalk.com/document/development/queries-a-user-attendance-group
> Path: 应用开发 / 服务端 API / 考勤 > 考勤组管理 > 获取用户考勤组
> Updated: 2026-05-27 13:09:52

# 获取用户考勤组

调用本接口，获取员工的考勤组信息，包括考勤组名称、考勤类型等，一个员工在一个企业中只能属于一个考勤组。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/getusergroup |
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
| userid | String | 是 | user123 | 员工在企业内的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/getusergroup" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=04cd6xxxx91f77' \
-d 'userid=zhangsan'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getusergroup");
OapiAttendanceGetusergroupRequest req = new OapiAttendanceGetusergroupRequest();
req.setUserid("user123");
OapiAttendanceGetusergroupResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGetusergroupRequest("https://oapi.dingtalk.com/topapi/attendance/getusergroup")

req.userid="zhangsan"
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
$req = new OapiAttendanceGetusergroupRequest;
$req->setUserid("zhangsan");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/getusergroup");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getusergroup");
OapiAttendanceGetusergroupRequest req = new OapiAttendanceGetusergroupRequest();
req.Userid = "zhangsan";
OapiAttendanceGetusergroupResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | AtGroupFullForTopVo |  | 查询结果。 |
| name | String | 考勤 | 考勤组名称。 |
| group\_id | Number | 685935028 | 考勤组ID。  **[!NOTE]**  如果你使用的是旧考勤组标识**group\_key**，可通过[groupKey转换为groupId](0176-convert-groupkey-to-groupid.md)接口将**group\_key**转换为**group\_id**。 |
| type | String | TURN | 考勤类型：   - **FIXED**：固定排班 - **TURN**：轮班排班 - **NONE**：无班次 |
| classes | AtClassVo[] |  | 考勤组中的班次列表。 |
| class\_id | Number | 678215070 | 班次ID。 |
| name | String | A班 | 班次名称。 |
| sections | AtSectionVo[] |  | 班次中上下班列表。 |
| times | AtTimeVo[] |  | 班次中上下班详情列表。 |
| check\_time | Date | 1970-01-01 19:00:00 | 打卡时间。 |
| check\_type | String | OnDuty | 打卡类型：   - **OnDuty**：上班 - **OffDuty**：下班 |
| across | Number | 0 | 打卡跨越的时间天数。 |
| begin\_min | Number | 30 | 允许的最早提前打卡时间，单位分钟。 |
| end\_min | Number | 0 | 允许的最晚延后打卡时间，单位分钟。 |
| setting | ClassSettingVo |  | 班次配置。 |
| rest\_begin\_time | AtTimeVo |  | 休息开始设置。 |
| across | Number | 0 | 时间跨度。   - **0**：不跨天 - **1**：跨天 |
| begin\_min | Number | 0 | 开始时间。 |
| end\_min | Number | 0 | 结束时间。 |
| check\_time | Date | 1970-01-01 19:00:00 | 休息开始时间。 |
| check\_type | String | OnDuty | 设置类型：   - **OnDuty**：休息开始 - **OffDuty**：休息结束 |
| rest\_end\_time | AtTimeVo |  | 休息结束时间设置。 |
| across | Number | 0 | 时间跨度。 |
| begin\_min | Number | 0 | 开始时间。 |
| end\_min | Number | 0 | 结束时间。 |
| check\_time | Date | 1970-01-01 20:00:00 | 休息结束时间。 |
| check\_type | String | OffDuty | 打卡类型：   - **OnDuty**：休息开始 - **OffDuty**：休息结束 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | f8zybbfze3e8 | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "classes": [
      {
        "class_id": 677995086,
        "name": "A",
        "sections": [
          {
            "times": [
              {
                "across": 0,
                "check_time": "1970-01-01 09:30:00",
                "check_type": "OnDuty"
              },
              {
                "across": 0,
                "check_time": "1970-01-01 18:30:00",
                "check_type": "OffDuty"
              }
            ]
          }
        ],
        "setting": {}
      },
      {
        "class_id": 678215070,
        "name": "B",
        "sections": [
          {
            "times": [
              {
                "across": 0,
                "check_time": "1970-01-01 19:00:00",
                "check_type": "OnDuty"
              },
              {
                "across": 1,
                "check_time": "1970-01-01 05:00:00",
                "check_type": "OffDuty"
              }
            ]
          }
        ],
        "setting": {}
      }
    ],
    "group_id": 685935028,
    "name": "考勤",
    "type": "FIXED"
  },
  "request_id": "f8zybbfze3e8"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
