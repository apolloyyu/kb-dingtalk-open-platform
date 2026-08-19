---
title: "更新参与考勤人员"
source_url: "https://open.dingtalk.com/document/development/attendance-group-member-update"
namespace: "development"
slug: "attendance-group-member-update"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤组管理 > 更新参与考勤人员"
doc_id: "5KKDOYZw53"
updated_at: "2026-05-27 13:09:55"
---

> Source: https://open.dingtalk.com/document/development/attendance-group-member-update
> Path: 应用开发 / 服务端API / 考勤 > 考勤组管理 > 更新参与考勤人员
> Updated: 2026-05-27 13:09:55

# 更新参与考勤人员

调用本接口，更新考勤组成员，对某个考勤组的**参与考勤人员**和**无需考勤人员**进行新增和删除操作。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/member/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 是 | user123 | 操作人userId。 |
| group\_id | Number | 是 | 98562 | 考勤组ID。  **[!NOTE]**  如果你使用的是旧考勤组标识即group\_key，可以调用[groupKey转换为groupId](0176-convert-groupkey-to-groupid.md)接口将group\_key转换为group\_id。 |
| schedule\_flag | Number | 是 | 0 | 从哪天开始排班。   - **0**：从今天开始排班 - **1**：从明天开始排班 |
| update\_param | TopGroupMemberUpdateParam | 是 |  | 更新考勤组信息。 |
| remove\_extra\_users | String[] | 否 | ["user123","user456"] | 删除无需考勤的成员，没有的话，无需赋值，每次调用最多传20个userId。 |
| remove\_depts | String[] | 否 | ["123","456"] | 删除考勤部门，没有的话，无需赋值，每次调用最多传20个部门ID。 |
| remove\_users | String[] | 否 | ["user123","user456"] | 删除考勤人员，没有的话，无需赋值，每次调用最多传20个userId。 |
| add\_depts | String[] | 否 | ["123","456"] | 添加考勤部门，没有的话，无需赋值，每次调用最多传20个部门ID。 |
| add\_users | String[] | 否 | ["user123","user456"] | 添加考勤人员，没有的话，无需赋值，每次调用最多传20个userId。 |
| add\_extra\_users | String[] | 否 | ["user123","user456"] | 添加无需考勤的人员，没有的话，无需赋值，每次调用最多传20个userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/member/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=0142dxxxxa6204' \
-d 'group_id=122' \
-d 'op_user_id=dd_dd' \
-d 'schedule_flag=0' \
-d 'update_param=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/member/update");
OapiAttendanceGroupMemberUpdateRequest req = new OapiAttendanceGroupMemberUpdateRequest();
req.setOpUserId("user123");
req.setGroupId(98562L);
req.setScheduleFlag(0L);
TopGroupMemberUpdateParam updateParam = new TopGroupMemberUpdateParam();
updateParam.setAddDepts(Arrays.asList("123"));
updateParam.setRemoveDepts(Arrays.asList("456"));
updateParam.setAddUsers(Arrays.asList("user123"));
updateParam.setAddExtraUsers(Arrays.asList("user456"));
updateParam.setRemoveExtraUsers(Arrays.asList("user789"));
updateParam.setRemoveUsers(Arrays.asList("user121"));
req.setUpdateParam(updateParam);
OapiAttendanceGroupMemberUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupMemberUpdateRequest("https://oapi.dingtalk.com/topapi/attendance/group/member/update")

req.op_user_id="dd_dd"
req.group_id=122
req.schedule_flag=0
req.update_param=""
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
$req = new OapiAttendanceGroupMemberUpdateRequest;
$req->setOpUserId("dd_dd");
$req->setGroupId("122");
$req->setScheduleFlag("0");
$update_param = new TopGroupMemberUpdateParam;
$update_param->remove_extra_users="dd_test";
$update_param->remove_depts="1234";
$update_param->remove_users="dd_dd";
$update_param->add_depts="123";
$update_param->add_users="dd_mana";
$update_param->add_extra_users="dd_d";
$req->setUpdateParam($update_param);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/member/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/member/update");
OapiAttendanceGroupMemberUpdateRequest req = new OapiAttendanceGroupMemberUpdateRequest();
req.OpUserId = "dd_dd";
req.GroupId = 122L;
req.ScheduleFlag = 0L;
OapiAttendanceGroupMemberUpdateRequest.TopGroupMemberUpdateParamDomain obj1 = new OapiAttendanceGroupMemberUpdateRequest.TopGroupMemberUpdateParamDomain();
obj1.RemoveExtraUsers = "dd_test";
obj1.RemoveDepts = "1234";
obj1.RemoveUsers = "dd_dd";
obj1.AddDepts = "123";
obj1.AddUsers = "dd_mana";
obj1.AddExtraUsers = "dd_d";
req.UpdateParam_ = obj1;
OapiAttendanceGroupMemberUpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 3pgsafymemlr | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| success | Boolean | true | 是否成功标记。   - **true**：成功 - **false**：失败 |

### **响应体示例**

```
{
  "errcode": 0,
  "success": true,
  "request_id": "5sj3lgigiqm9"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
