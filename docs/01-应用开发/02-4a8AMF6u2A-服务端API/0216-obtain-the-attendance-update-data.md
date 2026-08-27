---
title: "获取用户考勤数据"
source_url: "https://open.dingtalk.com/document/development/obtain-the-attendance-update-data"
namespace: "development"
slug: "obtain-the-attendance-update-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤统计 > 获取用户考勤数据"
doc_id: "O8i8LaRf6I"
updated_at: "2026-06-23 10:39:15"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-attendance-update-data
> Path: 应用开发 / 服务端API / 考勤 > 考勤统计 > 获取用户考勤数据
> Updated: 2026-06-23 10:39:15

# 获取用户考勤数据

调用本接口，可获取用户的考勤数据，包括打卡流水记录、打卡结果和审批列表等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/getupdatedata |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_get\_attendance\_data-考勤数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | user01 | 用户的userId。 |
| work\_date | Date | 是 | 2021-01-14 | 查询日期。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/getupdatedata" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=e67ccxxxx2144c' \
-d 'userid=userId123456' \
-d 'work_date=2018-05-02+00%3A00%3A00'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getupdatedata");
OapiAttendanceGetupdatedataRequest req = new OapiAttendanceGetupdatedataRequest();
req.setUserid("user01");
req.setWorkDate(StringUtils.parseDateTime("2021-01-14"));
OapiAttendanceGetupdatedataResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGetupdatedataRequest("https://oapi.dingtalk.com/topapi/attendance/getupdatedata")

req.userid="userId123456"
req.work_date="2018-05-02 00:00:00"
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
$req = new OapiAttendanceGetupdatedataRequest;
$req->setUserid("userId123456");
$req->setWorkDate("2018-05-02 00:00:00");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/getupdatedata");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getupdatedata");
OapiAttendanceGetupdatedataRequest req = new OapiAttendanceGetupdatedataRequest();
req.Userid = "userId123456";
req.WorkDate = DateTime.Parse("2018-05-02 00:00:00");
OapiAttendanceGetupdatedataResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| result | AtCheckInfoForOpenVo |  | 调用结果。 |
| work\_date | Date | 2021-01-14 00:00:00 | 查询日期 |
| attendance\_result\_list | AtAttendanceResultForOpenVo[] |  | 打卡结果。 |
| record\_id | Number | 53429818546 | 打卡流水ID。 |
| source\_type | String | USER | 打卡来源。   - **ATM**：考勤机 - **BEACON：IBeacon** - **DING\_ATM**：钉钉考勤机 - **USER**：用户打卡 - **BOSS**：老板改签 - **APPROVE**：审批系统 - **SYSTEM**：考勤系统 - **AUTO\_CHECK**：自动打卡 |
| plan\_check\_time | Date | 2021-01-14 09:00:00 | 标准打卡时间。 |
| class\_id | Number | 709595172 | 班次ID。 |
| location\_method | String | MAP | 定位方法。 |
| location\_result | String | Normal | 定位结果。   - **Normal**：范围内 - **Outside**：范围外 - **NotSigned**：未打卡 |
| outside\_remark | String | 外勤 | 外勤备注。 |
| plan\_id | Number | 176929277767 | 排班ID。 |
| user\_address | String | 绿城未来park | 用户打卡地址。 |
| group\_id | Number | 710705191 | 考勤组ID。 |
| user\_check\_time | Date | 2021-01-14 11:21:59 | 用户打卡时间。 |
| procInst\_id | String | PRO-xxx | 审批单ID。 |
| check\_type | String | OnDuty | 打卡类型。   - **OnDuty**：上班 - **OffDuty**：下班 |
| time\_result | String | Late | 打卡的时间结果。   - **Normal**：正常 - **Early**：早退 - **Late**：迟到 - **SeriousLate**：严重迟到 - **Absenteeism**：旷工迟到 - **NotSigned**：未打卡 |
| userid | String | user01 | 用户userId。 |
| approve\_list | AtApproveForOpenVo[] |  | 审批单列表。 |
| duration\_unit | String | day | 审批单的单位。 |
| duration | String | 2.0 | 时长。 |
| sub\_type | String | 年假 | 子类型名称。 |
| tag\_name | String | 请假 | 审批单类型名称。支持类型如下：   - **请假** - **出差** - **外出** - **加班** |
| procInst\_id | String | 1234abcd | 审批单ID。 |
| begin\_time | Date | 2019-08-15 | 审批单开始时间。 |
| biz\_type | Number | 3 | 审批单类型：   - **1**：加班 - **2**：出差/外出 - **3**：请假 |
| end\_time | Date | 2019-08-17 | 审批单结束时间。 |
| gmt\_finished | Date | 2019-08-15 | 审批单审批完成时间。 |
| check\_record\_list | AtAttendanceRecordForOpenVo[] |  | 打卡详情。 |
| record\_id | Number | 52710882700 | 打卡记录ID。 |
| source\_type | String |  | 打卡来源。   - **ATM**：考勤机 - **BEACON**：IBeacon - **DING\_ATM**：钉钉考勤机 - **USER**：用户打卡 - **BOSS**：老板改签 - **APPROVE**：审批系统 - **SYSTEM**：考勤系统 - **AUTO\_CHECK**：自动打卡 |
| user\_accuracy | String | 15.0 | 用户定位精度。 |
| valid\_matched | Boolean | false | 是否匹配打卡结果的流水。   - **true**：匹配 - **false**：不匹配 |
| user\_check\_time | Date | 2021-01-14 11:19:04 | 用户打卡时间。 |
| user\_longitude | String | 120.017267 | 打卡经度。 |
| user\_ssid | String | alibaba-inc1 | wifi名称。 |
| base\_accuracy | String | 0.0 | 基本定位精度。 |
| user\_mac\_addr | String | 11:11:11:11:11:11 | MAC地址。 |
| user\_latitude | String | 30.285938 | 打卡纬度。 |
| base\_address | String | 测试 | 打卡基础地址。 |
| invalid\_record\_msg | String | 需要二次确认 | 打卡无效的原因。 |
| invalid\_record\_type | String | Other | 打卡无效的类型。 |
| corpId | String | dinge8xxxx | 企业corpId。 |
| class\_setting\_info | AtClassSettingInfoForOpenVo |  | 当前排班对应的休息时间段。 |
| rest\_time\_vo\_list | AtRestTimeVo[] |  | 班次内休息信息。 |
| rest\_end\_time | Number | 0 | 休息结束时间。 |
| rest\_begin\_time | Number | 0 | 休息开始时间。 |
| errcode | Number | 0 | 返回码。 |
| success | Boolean | true | 是否调用成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | f1zwcp4fr28h | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "approve_list": [],
    "attendance_result_list": [
      {
        "location_method": "MAP",
        "record_id": 53429818546,
        "group_id": 710705191,
        "location_result": "Normal",
        "class_id": 709595172,
        "time_result": "Late",
        "user_address": "绿城未来park",
        "user_check_time": "2021-01-14 11:21:59",
        "plan_check_time": "2021-01-14 09:00:00",
        "check_type": "OnDuty",
        "source_type": "USER",
        "plan_id": 176929277767
      }
    ],
    "corpId": "dinge8xxxx",
    "work_date": "2021-01-14 09:00:00",
    "userid": "user01",
    "check_record_list": [
      {
        "record_id": 52710882700,
        "user_check_time": "2021-01-14 11:19:04",
        "valid_matched": false,
        "user_accuracy": "15.0",
        "source_type": "USER",
        "invalid_record_msg": "外勤打卡需要审批",
        "invalid_record_type": "Other",
        "user_longitude": "120.017267",
        "user_latitude": "30.286036"
      },
      {
        "record_id": 53019968340,
        "user_check_time": "2021-01-14 17:00:45",
        "valid_matched": false,
        "source_type": "ATM",
        "invalid_record_msg": "当前不在可打卡的时间范围，请和管理员联系",
        "invalid_record_type": "Other"
      }
    ]
  },
  "success": true,
  "request_id": "f1zwcp4fr28h"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
