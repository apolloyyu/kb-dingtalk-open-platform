---
title: "创建考勤组"
source_url: "https://open.dingtalk.com/document/development/attendance-group-write"
namespace: "development"
slug: "attendance-group-write"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤组管理 > 创建考勤组"
doc_id: "VxVPKPvmBj"
updated_at: "2026-05-27 13:09:41"
---

> Source: https://open.dingtalk.com/document/development/attendance-group-write
> Path: 应用开发 / 服务端API / 考勤 > 考勤组管理 > 创建考勤组
> Updated: 2026-05-27 13:09:41

# 创建考勤组

调用本接口，创建考勤组。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/add |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 4c9d5xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 是 | 123dfd | 操作人的userid。 |
| top\_group | TopGroupVo | 是 |  | 考勤组相关信息。 |
| owner | String | 否 | 123dfdf | 考勤组负责人。 |
| enable\_emp\_select\_class | Boolean | 否 | true | 未排班时是否允许员工选择班次打卡。   - **true**：允许 - **false**：不允许 |
| corp\_id | String | 否 | dingdfe | 企业的CorpId，可以在[开发者后台](https://open-dev.dingtalk.com/#/index)首页获取。image |
| skip\_holidays | Boolean | 否 | true | 是否跳过节假日。   - **true**（默认）：跳过 - **false：**不跳过 |
| special\_days | String | 否 | {"onDuty":{1400000:123,1400001:123},"offDuty":[1400000,1400001]} | 特殊日期配置。 |
| enable\_outside\_camera\_check | Boolean | 否 | true | 是否开启外勤打卡必须拍照。   - **true**：开启 - **false**（默认）：关闭 |
| positions | List<TopPositionVo> | 否 |  | 考勤地点相关设置信息。 |
| address | String | 否 | 生物科技产业园区经二路21号 | 考勤地址。 |
| corp\_id | String | 否 | 123dfd | 企业的CorpId，可以在[开发者后台](https://open-dev.dingtalk.com/#/index)首页获取。image |
| latitude | String | 否 | 36.687495 | 纬度。 |
| longitude | String | 否 | 101.750329 | 经度。 |
| accuracy | String | 否 | 0 | 精度。  **[!NOTE]**  该字段无实际作用，即不会影响精度，于2022.3.7已废弃。 |
| title | String | 否 | 青藏高原自然博物馆 | 考勤标题。 |
| modify\_member | Boolean | 否 | true | 是否有修改考勤组成员相关信息。   - **true**：修改 - **false**：未修改 |
| type | String | 是 | TURN | 考考勤组类型：   - **FIXED**：固定班制考勤组 - **TURN**：排班制考勤组 - **NONE**：自由工时考勤组 |
| enable\_face\_check | Boolean | 否 | true | 是是否开启人脸检测。   - **true**：开启 - **false**（默认）：关闭 |
| check\_need\_healthy\_code | Boolean | 否 | true | 打卡是否需要健康码：   - **true**：开启 - **false**（默认）：关闭 |
| enable\_camera\_check | Boolean | 否 | true | 是否开启拍照打卡。   - **true**：开启 - **false**（默认）：关闭 |
| shift\_vo\_list | List<TopShiftVo> | 否 |  | 班次相关配置信息。 |
| id | Number | 否 | 123 | 班次ID，可通过[获取班次摘要信息](0203-enterprise-shift-query-in-batches.md)接口获取id参数值。 |
| enable\_outside\_check | Boolean | 否 | true | 是否可以外勤打卡。   - **true**（默认）：允许 - **false**：不允许 |
| members | List<TopMemberVo> | 是 |  | 考勤组成员相关设置信息。 |
| role | String | 是 | Attendance | 角色，固定值Attendance。 |
| corp\_id | String | 否 | 123dfd | 企业的CorpId，可以在[开发者后台](https://open-dev.dingtalk.com/#/index)首页获取。image |
| type | String | 是 | StaffMember | 类型：   - StaffMember：人员类型 - DeptMember：部门类型 |
| user\_id | String | 是 | 1212jfkd | ID说明：   - 用户userId - 部门deptId |
| name | String | 是 | 白班考勤 | 考勤组名。 |
| id | Number | 否 | 123 | 考勤组ID。 |
| enable\_next\_day | Boolean | 否 | false | 是否第二天生效。   - **true**：是 - **false**：否 |
| manager\_list | String[] | 否 | ["userId1","userId2"] | 考勤组子管理员userid列表。 |
| workday\_class\_list | Number[] | 否 | [0,12,12,12,12,12,0] | 周班次列表。  **[!NOTE]**   - 固定班制必填，0表示休息。 - 数组内的值，从左到右依次代表周日到周六，每日的排班情况。 |
| default\_class\_id | Number | 否 | 1234 | 默认班次ID。  **[!NOTE]**  固定班制必填，可通过[获取班次摘要信息](0203-enterprise-shift-query-in-batches.md)接口获取id参数值。 |
| offset | Number | 否 | 500 | 考勤范围。 |
| resource\_permission\_map | TopGroupManageRolePermissionVo | 否 |  | 子管理员权限范围。   - **w**：可管理 - **r**：可读 |
| schedule | String | 否 | w | 员工排班。 |
| group\_member | String | 否 | w | 设置参与考勤人员。 |
| group\_type | String | 否 | r | 设置考勤类型。 |
| check\_time | String | 否 | w | 设置考勤时间。 |
| check\_position\_type | String | 否 | r | 设置打卡方式。 |
| over\_time\_rule | String | 否 | r | 设置加班规则。 |
| camera\_check | String | 否 | w | 设置拍照打卡规则。 |
| out\_side\_check | String | 否 | w | 设置外勤打卡。 |
| wifis | List<TopWifiVo> | 否 |  | 考勤wifi打卡相关配置信息。 |
| mac\_addr | String | 否 | C0:E0:D0:E0:C0:0F | mac地址。 |
| ssid | String | 否 | OFFICE-WiFi | wifi的ssid。 |
| corp\_id | String | 否 | 123dfd | 企业的CorpId，可以在[开发者后台](https://open-dev.dingtalk.com/#/index)首页获取。image |
| disable\_check\_without\_schedule | Boolean | 否 | false | 未排班时是否禁止员工打卡。   - **true**：禁止 - **false**：不禁止 |
| freecheck\_work\_days | Number[] | 否 | [1,2,3,4,5,6,0] | 自由工时考勤组工作日。  **[!NOTE]**     - 0表示休息。 - 数组内的值，从左到右依次代表周日到周六，每日的排班情况。 |
| freecheck\_day\_start\_min\_offset | Number | 否 | 240 | 自由工时考勤组考勤开始时间与当天0点偏移分钟数。  例如：540表示9:00 |
| disable\_check\_when\_rest | Boolean | 否 | false | 休息日打卡是否需审批：   - **true**：需要 - **false**：不需要 |
| enable\_position\_ble | Boolean | 否 | false | 是否启用蓝牙定位。   - **true**：启用 - **false**：不启用 |
| ble\_device\_list | List<TopAtBleDeviceVO> | 否 |  | 蓝牙打卡相关配置信息。 |
| device\_id | Number | 否 | 1311089987 | 设备ID，调用[查询员工智能考勤机列表](0221-query-the-list-of-employee-intelligent-attendance-machines.md)获取deviceid参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/add" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=e02c4xxxx5043' \
-d 'op_user_id=123dfd' \
-d 'top_group=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/add");
OapiAttendanceGroupAddRequest req = new OapiAttendanceGroupAddRequest();
req.setOpUserId("dinge8xxxx");
TopGroupVo topGroupVo = new TopGroupVo();
topGroupVo.setOwner("user1");
topGroupVo.setEnableEmpSelectClass(true);
topGroupVo.setCorpId("dinge8xxxx");
topGroupVo.setSkipHolidays(true);
topGroupVo.setSpecialDays("{\"onDuty\":{1400000:123,1400001:123},\"offDuty\":[1400000,1400001]}");
topGroupVo.setEnableOutsideCameraCheck(true);
List<TopPositionVo> positionVos = new ArrayList<TopPositionVo>();
TopPositionVo topPositionVo = new TopPositionVo();
positionVos.add(topPositionVo);
topPositionVo.setAddress("生物科技产业园区经二路21号");
topPositionVo.setCorpId("dinge8xxxx");
topPositionVo.setLatitude("36.687495");
topPositionVo.setAccuracy("0");
topPositionVo.setTitle("青藏高原自然博物馆");
topPositionVo.setLongitude("101.750329");
topGroupVo.setPositions(positionVos);
topGroupVo.setModifyMember(true);
topGroupVo.setType("TURN");
topGroupVo.setEnableFaceCheck(true);
topGroupVo.setCheckNeedHealthyCode(true);
topGroupVo.setEnableCameraCheck(true);
List<TopShiftVo> topShiftVos = new ArrayList<TopShiftVo>();
TopShiftVo topShiftVo = new TopShiftVo();
topShiftVos.add(topShiftVo);
topShiftVo.setId(123L);
topGroupVo.setShiftVoList(topShiftVos);
topGroupVo.setEnableOutsideCheck(true);
List<TopMemberVo> memberVos = new ArrayList<TopMemberVo>();
TopMemberVo topMemberVo = new TopMemberVo();
memberVos.add(topMemberVo);
topMemberVo.setRole("Attendance");
topMemberVo.setCorpId("dinge8xxxx");
topMemberVo.setType("StaffMember");
topMemberVo.setUserId("user1");
topGroupVo.setMembers(memberVos);
topGroupVo.setName("白班考勤");
topGroupVo.setEnableNextDay(false);
topGroupVo.setManagerList(Arrays.asList("userId1","userId2"));
topGroupVo.setDefaultClassId(1234L);
topGroupVo.setOffset(500L);
TopGroupManageRolePermissionVo groupManageRolePermissionVo = new TopGroupManageRolePermissionVo();
groupManageRolePermissionVo.setSchedule("w");
groupManageRolePermissionVo.setGroupMember("w");
groupManageRolePermissionVo.setGroupType("r");
groupManageRolePermissionVo.setCheckTime("w");
groupManageRolePermissionVo.setCheckPositionType("r");
groupManageRolePermissionVo.setOverTimeRule("r");
groupManageRolePermissionVo.setCameraCheck("w");
groupManageRolePermissionVo.setOutSideCheck("w");
topGroupVo.setResourcePermissionMap(groupManageRolePermissionVo);
List<TopWifiVo> topWifiVos = new ArrayList<TopWifiVo>();
TopWifiVo topWifiVo = new TopWifiVo();
topWifiVos.add(topWifiVo);
topWifiVo.setMacAddr("C0:E0:D0:E0:C0:0F");
topWifiVo.setSsid("OFFICE-WiFi");
topWifiVo.setCorpId("dinge8xxxx");
topGroupVo.setWifis(topWifiVos);
topGroupVo.setDisableCheckWithoutSchedule(false);
topGroupVo.setFreecheckDayStartMinOffset(240L);
topGroupVo.setDisableCheckWhenRest(true);
req.setTopGroup(topGroupVo);
OapiAttendanceGroupAddResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupAddRequest("https://oapi.dingtalk.com/topapi/attendance/group/add")

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
$top_group->name = "白班考勤";
$top_group->type = "TURN"; 
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
$positions = new TopPositionVo;
$positions->title = "青藏高原自然博物馆";
$positions->address = "生物科技产业园区经二路21号";
$positions->latitude = "36.687495";
$positions->longitude = "101.750329";
$positions->accuracy = "0";
$top_group->positions = array($positions);
$members = new TopMemberVo;
$members->user_id = "1212jfkd";
$members->type = "StaffMember";
$members->role = "Attendance";
$top_group->members = array($members);
$wifis = new TopWifiVo;
$wifis->ssid = "OFFICE-WiFi";
$wifis->mac_addr = "C0:E0:D0:E0:C0:0F";
$top_group->wifis = array($wifis);
$ble_device_list = new TopAtBleDeviceVO;
$ble_device_list->device_id = "1311089987";
$top_group->ble_device_list = array($ble_device_list);
$shift_vo_list = new TopShiftVo;
$shift_vo_list->id = "123";
$top_group->shift_vo_list = array($shift_vo_list);
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
$req->setTopGroup($top_group);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/add");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/add");
OapiAttendanceGroupAddRequest req = new OapiAttendanceGroupAddRequest();
req.OpUserId = "123dfd";
OapiAttendanceGroupAddRequest.TopGroupVoDomain obj1 = new OapiAttendanceGroupAddRequest.TopGroupVoDomain();
obj1.Owner = "123dfdf";
obj1.EnableEmpSelectClass = true;
obj1.CorpId = "dingdfe";
obj1.SkipHolidays = true;
obj1.SpecialDays = "{\"onDuty\":{1400000:123,1400001:123},\"offDuty\":[1400000,1400001]}";
obj1.EnableOutsideCameraCheck = true;
List<OapiAttendanceGroupAddRequest.TopPositionVoDomain> list3 = new List<OapiAttendanceGroupAddRequest.TopPositionVoDomain>();
OapiAttendanceGroupAddRequest.TopPositionVoDomain obj4 = new OapiAttendanceGroupAddRequest.TopPositionVoDomain();
list3.Add(obj4);
obj4.Address = "生物科技产业园区经二路21号";
obj4.CorpId = "123dfd";
obj4.Latitude = "36.687495";
obj4.Accuracy = "0";
obj4.Title = "青藏高原自然博物馆";
obj4.Longitude = "101.750329";
obj1.Positions = list3;
obj1.ModifyMember = true;
obj1.Type = "TURN";
obj1.EnableFaceCheck = true;
obj1.CheckNeedHealthyCode = true;
obj1.EnableCameraCheck = true;
List<OapiAttendanceGroupAddRequest.TopShiftVoDomain> list6 = new List<OapiAttendanceGroupAddRequest.TopShiftVoDomain>();
OapiAttendanceGroupAddRequest.TopShiftVoDomain obj7 = new OapiAttendanceGroupAddRequest.TopShiftVoDomain();
list6.Add(obj7);
obj7.Id = 123L;
obj1.ShiftVoList = list6;
obj1.EnableOutsideCheck = true;
List<OapiAttendanceGroupAddRequest.TopMemberVoDomain> list9 = new List<OapiAttendanceGroupAddRequest.TopMemberVoDomain>();
OapiAttendanceGroupAddRequest.TopMemberVoDomain obj10 = new OapiAttendanceGroupAddRequest.TopMemberVoDomain();
list9.Add(obj10);
obj10.Role = "Attendance";
obj10.CorpId = "123dfd";
obj10.Type = "StaffMember";
obj10.UserId = "1212jfkd";
obj1.Members = list9;
obj1.Name = "白班考勤";
obj1.EnableNextDay = false;
obj1.ManagerList = "\"userId1\",\"userId2\"";
obj1.DefaultClassId = 1234L;
obj1.Offset = 500L;
OapiAttendanceGroupAddRequest.TopGroupManageRolePermissionVoDomain obj11 = new OapiAttendanceGroupAddRequest.TopGroupManageRolePermissionVoDomain();
obj11.Schedule = "w";
obj11.GroupMember = "w";
obj11.GroupType = "r";
obj11.CheckTime = "w";
obj11.CheckPositionType = "r";
obj11.OverTimeRule = "r";
obj11.CameraCheck = "w";
obj11.OutSideCheck = "w";
obj1.ResourcePermissionMap = obj11;
List<OapiAttendanceGroupAddRequest.TopWifiVoDomain> list13 = new List<OapiAttendanceGroupAddRequest.TopWifiVoDomain>();
OapiAttendanceGroupAddRequest.TopWifiVoDomain obj14 = new OapiAttendanceGroupAddRequest.TopWifiVoDomain();
list13.Add(obj14);
obj14.MacAddr = "C0:E0:D0:E0:C0:0F";
obj14.Ssid = "OFFICE-WiFi";
obj14.CorpId = "123dfd";
obj1.Wifis = list13;
obj1.DisableCheckWithoutSchedule = false;
obj1.FreecheckDayStartMinOffset = 240L;
obj1.DisableCheckWhenRest = false;
req.TopGroup_ = obj1;
OapiAttendanceGroupAddResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | TopGroupVo |  | 调用结果。 |
| name | String | 白班考勤 | 考勤组名。 |
| id | Number | 712070073 | 考勤组id。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 系统错误 | 返回码描述。 |
| request\_id | String | 6pcx0i2ujtt9 | 请求ID。 |

### **响应体示例**

```
{
  "result":{
    "name":"白班考勤",
    "id":712070073
  },
  "errcode":0,
  "success":true,
  "errmsg":"ok",
  "request_id":"6pcx0i2ujtt9"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
