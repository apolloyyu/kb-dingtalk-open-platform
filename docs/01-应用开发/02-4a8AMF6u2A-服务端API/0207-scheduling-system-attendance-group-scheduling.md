---
title: "排班制考勤组排班"
source_url: "https://open.dingtalk.com/document/development/scheduling-system-attendance-group-scheduling"
namespace: "development"
slug: "scheduling-system-attendance-group-scheduling"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤排班 > 排班制考勤组排班"
doc_id: "5R0SttN7DM"
updated_at: "2026-05-27 17:06:08"
---

> Source: https://open.dingtalk.com/document/development/scheduling-system-attendance-group-scheduling
> Path: 应用开发 / 服务端API / 考勤 > 考勤排班 > 排班制考勤组排班
> Updated: 2026-05-27 17:06:08

# 排班制考勤组排班

调用本接口，给排班制考勤组成员进行排班，确保排班的考勤组类型为**排班制**。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/schedule/async |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 是 | user456 | 操作人userId。 |
| group\_id | Number | 是 | 2987 | 考勤组ID。  **[!NOTE]**  如果你使用的是旧考勤组标识即group\_key，可以调用[groupKey转换为groupId](0176-convert-groupkey-to-groupid.md)接口将group\_key转换为group\_id。 |
| schedules | TopScheduleParam[] | 是 |  | 排班详情。示例如下：   ``` {   "is_rest": false,   "work_date": 1605150671000,   "shift_id": 1,   "userid": "user123" } ```   **[!NOTE]**  最大列表长度200。 |
| shift\_id | Number | 是 | 1 | 班次ID，休息班次传1，可通过[获取班次摘要信息](0203-enterprise-shift-query-in-batches.md)接口获取id参数值。  **[!NOTE]**   - 当is\_rest参数传true时，shift\_id传1。 - 如果你需要清空排班，shift\_id传 -2。 |
| work\_date | Number | 是 | 1564985177000 | 排班日期。  **[!NOTE]**  可排班日期不早于180天前，不晚于180天后。 |
| is\_rest | Boolean | 否 | false | 是否休息：   - **true**：休息  **[!NOTE]**  当该参数为true时，shift\_id传1。 - **false**：不休息 |
| userid | String | 是 | user123 | 用户的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/schedule/async" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=d64b3xxxx57b23' \
-d 'group_id=2987' \
-d 'op_user_id=dd_test' \
-d 'schedules=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/schedule/async");
OapiAttendanceGroupScheduleAsyncRequest req = new OapiAttendanceGroupScheduleAsyncRequest();
req.setOpUserId("user456");
req.setGroupId(2987L);
List<TopScheduleParam> list2 = new ArrayList<TopScheduleParam>();
TopScheduleParam obj3 = new TopScheduleParam();
obj3.setShiftId(1L);
obj3.setWorkDate(1564985177000L);
obj3.setIsRest(false);
obj3.setUserid("user123");
list2.add(obj3);
req.setSchedules(list2);
OapiAttendanceGroupScheduleAsyncResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupScheduleAsyncRequest("https://oapi.dingtalk.com/topapi/attendance/group/schedule/async")

req.op_user_id="dd_test"
req.group_id=2987
req.schedules=""
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
$req = new OapiAttendanceGroupScheduleAsyncRequest;
$req->setOpUserId("dd_test");
$req->setGroupId("2987");
$schedules = new TopScheduleParam;
$schedules->shift_id="1";
$schedules->work_date="1564985177000";
$schedules->is_rest="false";
$schedules->userid="dd_test";
$req->setSchedules(array($schedules));
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/schedule/async");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/schedule/async");
OapiAttendanceGroupScheduleAsyncRequest req = new OapiAttendanceGroupScheduleAsyncRequest();
req.OpUserId = "dd_test";
req.GroupId = 2987L;
List<OapiAttendanceGroupScheduleAsyncRequest.TopScheduleParamDomain> list2 = new List<OapiAttendanceGroupScheduleAsyncRequest.TopScheduleParamDomain>();
OapiAttendanceGroupScheduleAsyncRequest.TopScheduleParamDomain obj3 = new OapiAttendanceGroupScheduleAsyncRequest.TopScheduleParamDomain();
list2.Add(obj3);
obj3.ShiftId = 1L;
obj3.WorkDate = 1564985177000L;
obj3.IsRest = false;
obj3.Userid = "dd_test";
req.Schedules_ = list2;
OapiAttendanceGroupScheduleAsyncResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 是否成功标记。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | zpd0i7dlr7bi | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "errmsg":"ok",
  "success":true,
  "request_id":"zpd0i7dlr7bi"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
