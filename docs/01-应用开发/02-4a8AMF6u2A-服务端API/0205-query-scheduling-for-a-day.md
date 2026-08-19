---
title: "查询成员排班信息"
source_url: "https://open.dingtalk.com/document/development/query-scheduling-for-a-day"
namespace: "development"
slug: "query-scheduling-for-a-day"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤排班 > 查询成员排班信息"
doc_id: "zPTYTKGX9C"
updated_at: "2026-07-08 14:13:46"
---

> Source: https://open.dingtalk.com/document/development/query-scheduling-for-a-day
> Path: 应用开发 / 服务端API / 考勤 > 考勤排班 > 查询成员排班信息
> Updated: 2026-07-08 14:13:46

# 查询成员排班信息

调用本接口，查询某人在某日的排班相关信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/schedule/listbyday |
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
| op\_user\_id | String | 是 | manager123 | 操作人的userId。 |
| user\_id | String | 是 | dd\_dd | 要查询的人员userId。 |
| date\_time | Number | 是 | 1564145519000 | 查询的时间，Unix时间戳，单位毫秒。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/schedule/listbyday" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=5d7f91f3-e22c-41ca-aee3-aa008603e00b' \
-d 'date_time=1564145519000' \
-d 'op_user_id=dd_dd' \
-d 'user_id=dd_dd'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/schedule/listbyday");
OapiAttendanceScheduleListbydayRequest req = new OapiAttendanceScheduleListbydayRequest();
req.setOpUserId("user123");
req.setUserId("user456");
req.setDateTime(1564145519000L);
OapiAttendanceScheduleListbydayResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceScheduleListbydayRequest("https://oapi.dingtalk.com/topapi/attendance/schedule/listbyday")

req.op_user_id="dd_dd"
req.user_id="dd_dd"
req.date_time=1564145519000
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
$req = new OapiAttendanceScheduleListbydayRequest;
$req->setOpUserId("dd_dd");
$req->setUserId("dd_dd");
$req->setDateTime("1564145519000");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/schedule/listbyday");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/schedule/listbyday");
OapiAttendanceScheduleListbydayRequest req = new OapiAttendanceScheduleListbydayRequest();
req.OpUserId = "dd_dd";
req.UserId = "dd_dd";
req.DateTime = 1564145519000L;
OapiAttendanceScheduleListbydayResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | TopScheduleVo[] |  | 查询结果。 |
| check\_type | String | OnDuty | 考勤类型：   - **Onduty**：上班打卡 - **OffDuty**：下班打卡 |
| approve\_type | String | demo | 审批类型。  **[!NOTE]**  如果当天没有审批单，则不返回该字段。 |
| gmt\_modified | Date | 2020-11-10 14:33:13 | 最后更新时间。 |
| gmt\_create | Date | 2020-10-26 03:26:59 | 创建时间。 |
| corp\_id | String | dinge8xxxx | 企业的corpId，可在[开发者后台](https://open-dev.dingtalk.com/)首页查看。CorpId |
| check\_date\_time | Date | 2020-11-10 14:33:13 | 该员工打卡时间。 |
| group\_id | Number | 394775001 | 考勤组ID。 |
| class\_name | String | dsdsd | 班次名称。 |
| user\_id | String | dd\_test | 用户的userId。 |
| approve\_biz\_type | Number | demo | 排班绑定的假勤审批类型：   - **1**：加班 - **2**：出差 - **3**：请假   **[!NOTE]**  如果当天没有审批单，则不返回该字段。 |
| approve\_id | Number | 123 | 排班绑定的审批单ID。  **[!NOTE]**  如果当天没有审批单，则不返回该字段。 |
| class\_setting\_id | Number | 297490031 | 排班关联的班次设置ID。  **[!NOTE]**  如果使用的全局配置，则不返回该字段。 |
| approve\_tag\_name | String | 请假 | 排班绑定的假勤审批单名称。  **[!NOTE]**  如果当天没有审批单，则不返回该字段。 |
| features | String | {\"dataSource\":\"adminSetting\",\"flexMinutes\":[60,60],\"overtimeSettingId\":221375127,\"punchId\":524588947} | 扩展字段。   - **dataSource**：该字段暂无实际意义 - f**lexMinutes**：所在班次设置的允许晚到晚走，早到早走的时间，单位分钟 - **punchId**：对应卡点 - **idovertimeSettingId**：加班规则ID |
| class\_id | Number | 370370019 | 班次ID。 |
| check\_status | String | Timeout | 打卡状态：   - **Init**：未打 - **Checked**：已打卡 - **Timeout**：缺卡 |
| work\_date | Date | 2020-11-10 00:00:00 | 工作日，代表具体哪一天的排班。 |
| check\_end\_time | Date | 2020-09-08 09:30:00 | 结束打卡时间。 |
| is\_rest | String | N | 是否休息：   - **Y**：当天排休 - **N**：不休息 |
| check\_begin\_time | Date | 2020-09-08 09:00:00 | 开始打卡时间。 |
| real\_plan\_time | Date | 2020-09-08 10:00:00 | 开启弹性工时卡点调整后用户应打卡时间。 |
| id | Number | 56676915454 | 排班ID。 |
| success | Boolean | true | 是否成功标记。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | demo | 返回码描述。 |
| request\_id | String | 6bzhf2vn89pv | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": [
    {
      "check_date_time": "2020-11-10 09:30:00",
      "check_status": "Timeout",
      "check_type": "OnDuty",
      "class_id": 677995086,
      "class_name": "A",
      "class_setting_id": 599315627,
      "corp_id": "dinge8xxxx",
      "features": "{\"flexMinutes\":[30,30],\"overtimeSettingId\":581490201,\"punchId\":346266563}",
      "gmt_create": "2020-10-26 03:26:59",
      "gmt_modified": "2020-11-10 14:33:13",
      "group_id": 685935028,
      "id": 156270023005,
      "is_rest": "N",
      "real_plan_time": "2020-11-10 09:30:00",
      "user_id": "user123",
      "work_date": "2020-11-10 00:00:00"
    },
    {
      "check_date_time": "2020-11-10 18:30:00",
      "check_status": "Timeout",
      "check_type": "OffDuty",
      "class_id": 677995086,
      "class_name": "A",
      "class_setting_id": 599315627,
      "corp_id": "dinge8xxxx",
      "features": "{\"flexMinutes\":[30,30],\"overtimeSettingId\":581490201,\"punchId\":346266564}",
      "gmt_create": "2020-10-26 03:26:59",
      "gmt_modified": "2020-11-11 02:30:45",
      "group_id": 685935028,
      "id": 156270023006,
      "is_rest": "N",
      "real_plan_time": "2020-11-10 18:30:00",
      "user_id": "user123",
      "work_date": "2020-11-10 00:00:00"
    }
  ],
  "success": true,
  "request_id": "6bzhf2vn89pv"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
