---
title: "创建班次"
source_url: "https://open.dingtalk.com/document/development/create-modify-shifts"
namespace: "development"
slug: "create-modify-shifts"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤班次 > 创建班次"
doc_id: "gTaviy2npS"
updated_at: "2026-05-27 17:05:54"
---

> Source: https://open.dingtalk.com/document/development/create-modify-shifts
> Path: 应用开发 / 服务端API / 考勤 > 考勤班次 > 创建班次
> Updated: 2026-05-27 17:05:54

# 创建班次

调用本接口，创建钉钉考勤班次。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/shift/add |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 是 | user01 | 操作人userId。 |
| shift | TopAtClassVo | 是 |  | 班次。 |
| owner | String | 否 | user01 | 班次owner。 |
| class\_group\_name | String | 否 | def | 班次组名。 |
| corp\_id | String | 否 | ding23 | 企业的corpId，可在[开发者后台](https://open-dev.dingtalk.com/)查看。CorpId |
| name | String | 是 | 白班 | 班次名称。 |
| id | Number | 否 | 124 | 班次id，可通过[获取班次摘要信息](0203-enterprise-shift-query-in-batches.md)接口获取id参数值。  **[!NOTE]**  id 不传值时为创建班次，传值时是修改已有班次。 |
| sections | TopAtSectionVo[] | 是 |  | 卡段。 |
| times | TopAtTimeVo[] | 是 |  | 打卡信息。 |
| check\_type | String | 是 | OnDuty | 打卡类型：   - **OnDuty**：上班 - **OffDuty**：下班 |
| across | Number | 是 | 0 | 是否跨天：   - **0**：不跨天 - **1**：跨天 |
| end\_min | Number | 否 | -1 | 允许的最晚打卡时间，单位分钟（-1表示不限制）。 |
| check\_time | Date | 是 | 2020-12-02 09:00:00 | 打卡时间。 |
| free\_check | Boolean | 否 | false | 是否免打卡：   - **false**：需打卡 - **true**：免打卡 |
| begin\_min | Number | 否 | 30 | 允许的最早提前打卡时间，分钟为单位。 |
| setting | TopAtClassSettingVo | 否 |  | 设置。 |
| rest\_begin\_time | TopAtTimeVo | 否 |  | 休息开始。 |
| check\_type | String | 否 | OnDuty | 休息类型：   - **OnDuty**：休息开始 - **OffDuty**：休息结束 |
| check\_time | Date | 否 | 2020-12-02 09:00:00 | 休息打卡时间。 |
| free\_check | Boolean | 否 | false | 是否免打卡：   - **true**：免打卡 - **false**：需打卡 |
| across | Number | 否 | 0 | 是否跨天，跨天是指休息时间是第二天：   - **0**：不跨天 - **1**：跨天 |
| class\_id | Number | 否 | 221 | 班次id，可通过[获取班次摘要信息](0203-enterprise-shift-query-in-batches.md)接口获取id参数值。 |
| is\_flexible | Boolean | 否 | false | 是否弹性。   - **true**：弹性 - **false**：非弹性 |
| corp\_id | String | 否 | ding121 | 企业的corpId，可在[开发者后台](https://open-dev.dingtalk.com/)查看。CorpId |
| is\_deleted | String | 否 | N | 是否删除。   - **N**：是 - **Y**：否 |
| rest\_end\_time | TopAtTimeVo | 否 |  | 休息结束。 |
| check\_type | String | 否 | OffDuty | 休息类型：   - **OnDuty**：休息开始 - **OffDuty**：休息结束 |
| check\_time | Date | 否 | 2020-12-02 09:00:00 | 休息时间。 |
| free\_check | Boolean | 否 | false | 是否免打卡：   - **false**：需打卡 - **true**：免打卡 |
| across | Number | 否 | 1 | 是否跨天，跨天是指休息时间是第二天：   - **0**：不跨天 - **1**：跨天 |
| serious\_late\_minutes | Number | 否 | 31 | 严重早退/迟到的时长，单位分钟。 |
| absenteeism\_late\_minutes | Number | 否 | 60 | 旷工早退/迟到的时长，单位分钟。  **[!NOTE]**  旷工迟到的分钟数必须比严重迟到分钟数多。 |
| extras | Json | 否 | {"cause":"{\"type\":\"approve\",\"relatedId\":\"43494469-21a6-4111-953b-7810a709f27f\"}"} | 班次设置扩展字段，非临时班次无需填写。 |
| tags | String | 否 | temp:schedule:isv | 班次tags，非临时班次无需填写。 |
| service\_id | Number | 否 | 123 | 高级排班绑定服务id，非临时班次无需填写。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/shift/add" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=39cbcxxxx9058' \
-d 'op_user_id=abc' \
-d 'shift=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/add");
OapiAttendanceShiftAddRequest request = new OapiAttendanceShiftAddRequest();
TopAtClassVo topAtClassVo = new TopAtClassVo();
topAtClassVo.setOwner("user456");
topAtClassVo.setClassGroupName("测试班次组");
topAtClassVo.setCorpId("dinge8a56572xxxx");
topAtClassVo.setName("A1");
List<TopAtSectionVo> sectionVos = new ArrayList<>();
TopAtSectionVo sectionVo = new TopAtSectionVo();
List<TopAtTimeVo> timeVos = new ArrayList<>();
TopAtTimeVo timeVo = new TopAtTimeVo();
timeVo.setAcross(0L);
timeVo.setBeginMin(0L);
timeVo.setCheckTime(StringUtils.parseDateTime("2020-12-02 09:00:00"));
timeVo.setCheckType("OnDuty");
timeVo.setEndMin(-1L);
timeVo.setFreeCheck(false);
TopAtTimeVo timeVo1 = new TopAtTimeVo();
timeVo1.setAcross(0L);
timeVo1.setEndMin(0L);
timeVo1.setCheckTime(StringUtils.parseDateTime("2020-12-02 18:00:00"));
timeVo1.setCheckType("OffDuty");
timeVo1.setEndMin(-1L);
timeVo1.setFreeCheck(false);
timeVos.add(timeVo);
timeVos.add(timeVo1);
sectionVo.setTimes(timeVos);
sectionVos.add(sectionVo);
topAtClassVo.setSections(sectionVos);
TopAtClassSettingVo settingVo = new TopAtClassSettingVo();
topAtClassVo.setSetting(settingVo);
TopAtTimeVo restBeginTime = new TopAtTimeVo();
settingVo.setRestBeginTime(restBeginTime);
restBeginTime.setFreeCheck(false);
restBeginTime.setAcross(1L);
restBeginTime.setCheckType("OnDuty");
restBeginTime.setFreeCheck(false);
restBeginTime.setCheckTime(StringUtils.parseDateTime("2020-12-02 12:00:00"));
TopAtTimeVo restEndTime = new TopAtTimeVo();
settingVo.setRestEndTime(restEndTime);
restEndTime.setAcross(1L);
restEndTime.setCheckType("OffDuty");
restEndTime.setFreeCheck(false);
restEndTime.setCheckTime(StringUtils.parseDateTime("2020-12-02 13:00:00"));
settingVo.setCorpId("dinge8a56572xxxx");
settingVo.setIsDeleted("N");
settingVo.setAbsenteeismLateMinutes(60L);
settingVo.setIsFlexible(false);
settingVo.setSeriousLateMinutes(30L);
request.setOpUserId("user456");
request.setShift(topAtClassVo);
OapiAttendanceShiftAddResponse response = client.execute(request, access_token);
System.out.println(response.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceShiftAddRequest("https://oapi.dingtalk.com/topapi/attendance/shift/add")

req.op_user_id="abc"
req.shift=""
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
$req = new OapiAttendanceShiftAddRequest;
$req->setOpUserId("abc");
$shift = new TopAtClassVo;
$shift->owner="abc";
$shift->class_group_name="def";
$shift->corp_id="ding23";
$shift->name="白班";
$sections = new TopAtSectionVo;
$times = new TopAtTimeVo;
$times->check_type="OnDuty";
$times->across="0";
$times->end_min="-1";
$times->check_time="2020-03-17 12:00:00";
$times->free_check="false";
$times->begin_min="30";
$sections->times = array($times);
$shift->sections = array($sections);
$setting = new TopAtClassSettingVo;
$rest_begin_time = new TopAtTimeVo;
$rest_begin_time->check_type="OnDuty";
$rest_begin_time->check_time="2020-03-17 12:00:00";
$rest_begin_time->free_check="false";
$rest_begin_time->across="0";
$setting->rest_begin_time = $rest_begin_time;
$setting->is_flexible="false";
$setting->corp_id="ding121";
$setting->is_deleted="N";
$rest_end_time = new TopAtTimeVo;
$rest_end_time->check_type="OffDuty";
$rest_end_time->check_time="2020-03-17 13:00:00";
$rest_end_time->free_check="false";
$rest_end_time->across="1";
$setting->rest_end_time = $rest_end_time;
$setting->serious_late_minutes="31";
$setting->absenteeism_late_minutes="60";
$shift->setting = $setting;
$req->setShift($shift);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/shift/add");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/add");
OapiAttendanceShiftAddRequest req = new OapiAttendanceShiftAddRequest();
req.OpUserId = "abc";
OapiAttendanceShiftAddRequest.TopAtClassVoDomain obj1 = new OapiAttendanceShiftAddRequest.TopAtClassVoDomain();
obj1.Owner = "abc";
obj1.ClassGroupName = "def";
obj1.CorpId = "ding23";
obj1.Name = "白班";
List<OapiAttendanceShiftAddRequest.TopAtSectionVoDomain> list3 = new List<OapiAttendanceShiftAddRequest.TopAtSectionVoDomain>();
OapiAttendanceShiftAddRequest.TopAtSectionVoDomain obj4 = new OapiAttendanceShiftAddRequest.TopAtSectionVoDomain();
list3.Add(obj4);
List<OapiAttendanceShiftAddRequest.TopAtTimeVoDomain> list6 = new List<OapiAttendanceShiftAddRequest.TopAtTimeVoDomain>();
OapiAttendanceShiftAddRequest.TopAtTimeVoDomain obj7 = new OapiAttendanceShiftAddRequest.TopAtTimeVoDomain();
list6.Add(obj7);
obj7.CheckType = "OnDuty";
obj7.Across = 0L;
obj7.EndMin = -1L;
obj7.CheckTime = DateTime.Parse("2020-03-17 12:00:00");
obj7.FreeCheck = false;
obj7.BeginMin = 30L;
obj4.Times= list6;
obj1.Sections= list3;
OapiAttendanceShiftAddRequest.TopAtClassSettingVoDomain obj8 = new OapiAttendanceShiftAddRequest.TopAtClassSettingVoDomain();
OapiAttendanceShiftAddRequest.TopAtTimeVoDomain obj9 = new OapiAttendanceShiftAddRequest.TopAtTimeVoDomain();
obj9.CheckType = "OnDuty";
obj9.CheckTime = DateTime.Parse("2020-03-17 12:00:00");
obj9.FreeCheck = false;
obj9.Across = 0L;
obj8.RestBeginTime= obj9;
obj8.IsFlexible = false;
obj8.CorpId = "ding121";
obj8.IsDeleted = "N";
OapiAttendanceShiftAddRequest.TopAtTimeVoDomain obj10 = new OapiAttendanceShiftAddRequest.TopAtTimeVoDomain();
obj10.CheckType = "OffDuty";
obj10.CheckTime = DateTime.Parse("2020-03-17 13:00:00");
obj10.FreeCheck = false;
obj10.Across = 1L;
obj8.RestEndTime= obj10;
obj8.SeriousLateMinutes = 31L;
obj8.AbsenteeismLateMinutes = 60L;
obj1.Setting= obj8;
req.Shift_ = obj1;
OapiAttendanceShiftAddResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | TopAtClassVo |  | 班次信息。 |
| id | Number | 706715401 | 班次id。 |
| name | String | A1 | 班次名称。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | wp2oh4e4vlbu | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "id": 706715401,
    "name": "A1"
  },
  "success": true,
  "request_id": "wp2oh4e4vlbu"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
