---
title: "更新考勤组"
source_url: "https://open.dingtalk.com/document/development/attendance-group-update-interface"
namespace: "development"
slug: "attendance-group-update-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤组管理 > 更新考勤组"
doc_id: "wgYfZYOGas"
updated_at: "2026-05-27 13:09:42"
---

> Source: https://open.dingtalk.com/document/development/attendance-group-update-interface
> Path: 应用开发 / 服务端API / 考勤 > 考勤组管理 > 更新考勤组
> Updated: 2026-05-27 13:09:42

# 更新考勤组

调用本接口，根据考勤组ID更新考勤组信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/modify |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | b5e95d101165xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 是 | 123dfd | 操作人userId。 |
| top\_group | Object | 是 |  | 考勤组信息。 |
| shift\_vo\_list | Object[] | 否 |  | 班次信息。 |
| id | Number | 否 | 123 | 班次ID，可通过[获取班次摘要信息](0203-enterprise-shift-query-in-batches.md)接口获取id参数值。 |
| id | Number | 是 | 123 | 考勤组ID。  **[!NOTE]**  如果你使用的是旧考勤组标识即group\_key，可以调用[groupKey转换为groupId](0176-convert-groupkey-to-groupid.md)接口将group\_key转换为group\_id。 |
| name | String | 否 | 白班考勤 | 考勤组名称。 |
| positions | Object[] | 否 |  | 考勤地址设置。 |
| address | String | 否 | 生物科技产业园区经二路21号 | 地址。 |
| corp\_id | String | 否 | 123dfd | 企业的CorpId，可以在[开发者后台](https://open-dev.dingtalk.com/#/index)首页获取。image |
| latitude | String | 否 | 36.687495 | 纬度(支持6位小数)。 |
| longitude | String | 否 | 101.750329 | 经度(支持6位小数)。 |
| title | String | 否 | 青藏高原自然博物馆 | 考勤标题。 |
| accuracy | String | 否 | 0 | 精度。  **[!NOTE]**  该字段无实际作用，即不会影响精度，于2022.3.7已废弃。 |
| offset | Number | 否 | 300 | 考勤范围。 |
| enable\_face\_check | Boolean | 否 | true | 是否开启人脸检测。   - **true**：开启 - **false**（默认）：关闭   **[!NOTE]**  该参数已废弃，请使用open\_face\_check参数。 |
| manager\_list | String[] | 否 | ["userId1","userId2"] | 考勤组子管理员userid列表。 |
| enable\_camera\_check | Boolean | 否 | true | 是否开启拍照打卡。   - **true**：开启 - **false**（默认）：关闭   **[!NOTE]**  该参数已废弃，请使用open\_camera\_check参数。 |
| owner | String | 否 | 123dfdf | 考勤组负责人userId。 |
| disable\_check\_when\_rest | Boolean | 否 | false | 休息日打卡是否需审批。   - **true**：需要 - **false**：不需要 |
| skip\_holidays | Boolean | 否 | true | 是否跳过节假日。   - **true**（默认）：跳过 - **false：**不跳过 |
| enable\_outside\_check | Boolean | 否 | true | 是否可以外勤打卡。   - **true**（默认）：允许 - **false**：不允许 |
| disable\_check\_without\_schedule | Boolean | 否 | false | 未排班时是否禁止员工打卡。   - **true**：禁止 - **false**：不禁止 |
| enable\_emp\_select\_class | Boolean | 否 | true | 未排班时是否允许员工选择班次打卡。   - **true**：允许 - **false**：不允许 |
| resource\_permission\_map | Object | 否 |  | 子管理员权限范围。   - **w**：可管理 - **r**：可读 |
| camera\_check | String | 否 | w | 设置拍照打卡规则。 |
| over\_time\_rule | String | 否 | r | 设置加班规则。 |
| check\_position\_type | String | 否 | w | 设置打卡方式。 |
| check\_time | String | 否 | r | 设置考勤时间。 |
| group\_type | String | 否 | w | 设置考勤类型。 |
| group\_member | String | 否 | r | 设置参与考勤人员。 |
| schedule | String | 否 | w | 员工排班。 |
| out\_side\_check | String | 否 | r | 设置外勤打卡。 |
| workday\_class\_list | Number[] | 否 | [12,12,12,12,0,0] | 周班次列表。  **[!NOTE]**   - 固定班制必填，0表示休息。 - 数组内的值，从左到右依次代表周日到周六，每日的排班情况。 |
| open\_camera\_check | Boolean | 否 | true | 是否开启拍照打卡。   - **true**：开启 - **false**（默认）：关闭 |
| open\_face\_check | Boolean | 否 | true | 是否开启人脸检测。   - **true**：开启 - **false**（默认）：关闭 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/modify" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=ca21b524-0a09-4909-b6e9-af087e28a86b' \
-d 'op_user_id=123dfd' \
-d 'top_group=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/modify");
OapiAttendanceGroupModifyRequest req = new OapiAttendanceGroupModifyRequest();
req.setOpUserId("user1");
TopGroupVo topGroupVo = new TopGroupVo();
topGroupVo.setOwner("user1");
topGroupVo.setEnableEmpSelectClass(true);
topGroupVo.setSkipHolidays(true);
List<TopPositionVo> positionVos = new ArrayList<TopPositionVo>();
TopPositionVo topPositionVo = new TopPositionVo();
positionVos.add(topPositionVo);
topPositionVo.setAddress("生物科技产业园区经二路21号");
topPositionVo.setCorpId("ding9f741xxxx");
topPositionVo.setLatitude("30.123");
topPositionVo.setAccuracy("0");
topPositionVo.setTitle("青藏高原自然博物馆");
topPositionVo.setLongitude("120.123");
topGroupVo.setPositions(positionVos);
topGroupVo.setEnableFaceCheck(true);
topGroupVo.setEnableCameraCheck(true);
List<TopShiftVo> topShiftVos = new ArrayList<TopShiftVo>();
TopShiftVo topShiftVo = new TopShiftVo();
topShiftVos.add(topShiftVo);
topShiftVo.setId(678215070L);
topGroupVo.setShiftVoList(topShiftVos);
topGroupVo.setEnableOutsideCheck(true);
topGroupVo.setName("测试考勤组1");
topGroupVo.setId(2987L);
topGroupVo.setManagerList(Arrays.asList("userId1"));
topGroupVo.setOffset(500L);
topGroupVo.setDisableCheckWithoutSchedule(false);
topGroupVo.setWorkdayClassList(Arrays.asList(12L,12L,12L,12L,12L,0L,0L));
req.setTopGroup(topGroupVo);
OapiAttendanceGroupModifyResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupModifyRequest("https://oapi.dingtalk.com/topapi/attendance/group/modify")

req.op_user_id="123dfd"
req.top_group=""
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

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST, DingTalkConstant::$FORMAT_JSON);
$req = new OapiAttendanceGroupAddRequest;
$req->setOpUserId("123dfd");

$top_group = new TopGroupVo;

// 以下字段在接口文档中存在：
$top_group->name = "白班考勤";
$top_group->type = "TURN"; // FIXED:固定班制, TURN:排班制, NONE:自由工时
$top_group->enable_face_check = "true";
$top_group->enable_camera_check = "true";
$top_group->enable_outside_camera_check = "true";
$top_group->enable_outside_check = "true";
$top_group->check_need_healthy_code = "true";
$top_group->enable_next_day = "false";
$top_group->modify_member = "true";
$top_group->offset = "500";
$top_group->default_class_id = "1234";
$top_group->manager_list = "[\"userId1\",\"userId2\"]";
$top_group->workday_class_list = "[12,12,12,12,12,0,0]";
$top_group->disable_check_without_schedule = "false";
$top_group->freecheck_work_days = "[1,2,3,4,5,6,0]";
$top_group->freecheck_day_start_min_offset = "240";
$top_group->disable_check_when_rest = "false";
$top_group->enable_position_ble = "false";

// positions - 考勤地点列表
$positions = new TopPositionVo;
$positions->title = "青藏高原自然博物馆";
$positions->address = "生物科技产业园区经二路21号";
$positions->latitude = "36.687495";
$positions->longitude = "101.750329";
$positions->accuracy = "0";
// 注意：positions中不需要设置corp_id字段
$top_group->positions = array($positions);

// members - 考勤组成员列表
$members = new TopMemberVo;
$members->user_id = "1212jfkd";
$members->type = "StaffMember";
$members->role = "Attendance";
// 注意：members中不需要设置corp_id字段
$top_group->members = array($members);

// wifis - WiFi打卡点列表
$wifis = new TopWifiVo;
$wifis->ssid = "OFFICE-WiFi";
$wifis->mac_addr = "C0:E0:D0:E0:C0:0F";
// 注意：wifis中不需要设置corp_id字段
$top_group->wifis = array($wifis);

// ble_device_list - 蓝牙设备列表
$ble_device_list = new TopAtBleDeviceVO;
$ble_device_list->device_id = "1311089987";
$top_group->ble_device_list = array($ble_device_list);

// shift_vo_list - 班次列表
$shift_vo_list = new TopShiftVo;
$shift_vo_list->id = "123";
$top_group->shift_vo_list = array($shift_vo_list);

// resource_permission_map - 资源权限映射
$resource_permission_map = new TopGroupManageRolePermissionVo;
$resource_permission_map->schedule = "w";
$resource_permission_map->group_member = "w";
$resource_permission_map->group_type = "r";
$resource_permission_map->check_time = "w";
$resource_permission_map->check_position_type = "r";
$resource_permission_map->over_time_rule = "r";
$resource_permission_map->camera_check = "w";
$resource_permission_map->out_side_check = "w";
$top_group->resource_permission_map = $resource_permission_map;

// 以下字段在接口文档中不存在，已删除：
// - owner: 考勤组负责人（应通过manager_list设置）
// - enable_emp_select_class: 非标准字段
// - corp_id: 企业ID从token中获取，不需要在请求体中设置
// - skip_holidays: 非标准字段
// - special_days: 非标准字段
// - id: 创建时不需要传入ID，由系统生成

$req->setTopGroup($top_group);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/add");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/modify");
OapiAttendanceGroupModifyRequest req = new OapiAttendanceGroupModifyRequest();
req.OpUserId = "123dfd";
OapiAttendanceGroupModifyRequest.TopGroupVoDomain obj1 = new OapiAttendanceGroupModifyRequest.TopGroupVoDomain();
List<OapiAttendanceGroupModifyRequest.TopShiftVoDomain> list3 = new List<OapiAttendanceGroupModifyRequest.TopShiftVoDomain>();
OapiAttendanceGroupModifyRequest.TopShiftVoDomain obj4 = new OapiAttendanceGroupModifyRequest.TopShiftVoDomain();
list3.Add(obj4);
obj4.Id = 123L;
obj1.ShiftVoList= list3;
obj1.Id = 123L;
obj1.Name = "百班考勤";
List<OapiAttendanceGroupModifyRequest.TopPositionVoDomain> list6 = new List<OapiAttendanceGroupModifyRequest.TopPositionVoDomain>();
OapiAttendanceGroupModifyRequest.TopPositionVoDomain obj7 = new OapiAttendanceGroupModifyRequest.TopPositionVoDomain();
list6.Add(obj7);
obj7.Address = "生物科技产业园区经二路21号";
obj7.CorpId = "123dfd";
obj7.Latitude = "36.687495";
obj7.Longitude = "101.750329";
obj7.Title = "青藏高原自然博物馆";
obj7.Accuracy = "0";
obj1.Positions= list6;
obj1.Offset = 300L;
obj1.EnableFaceCheck = true;
obj1.ManagerList = "\"userId1\",\"userId2\"";
obj1.EnableCameraCheck = true;
obj1.Owner = "123dfdf";
obj1.SkipHolidays = true;
obj1.EnableOutsideCheck = true;
obj1.DisableCheckWithoutSchedule = false;
obj1.EnableEmpSelectClass = true;
obj1.WorkdayClassList = new long[] { 12,12,12,12,0,0 };
req.TopGroup_ = obj1;
OapiAttendanceGroupModifyResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Object |  | 考勤组结果。 |
| name | String | 白班考勤 | 考勤组名称。 |
| id | Number | 123 | 考勤组ID。 |
| errmsg | String | 0 | 错误信息。 |
| errcode | Number | ok | 错误码。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |

### **响应体示例**

```
{
  "result":{
    "name":"白班考勤",
    "id":"123"
  },
  "errcode":0,
  "success":true,
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
