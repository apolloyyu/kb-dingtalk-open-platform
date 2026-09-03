# 创建考勤组

doc_id: VxVPKPvmBj
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/add
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_attendance_group_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- op_user_id (String, required): 操作人的userid。
- top_group (TopGroupVo, required): 考勤组相关信息。
- type (String, required): 考考勤组类型： - **FIXED**：固定班制考勤组 - **TURN**：排班制考勤组 - **NONE**：自由工时考勤组
- members (List<TopMemberVo>, required): 考勤组成员相关设置信息。
- role (String, required): 角色，固定值Attendance。
- user_id (String, required): ID说明： - 用户userId - 部门deptId
- name (String, required): 考勤组名。
- optional: owner(String), enable_emp_select_class(Boolean), corp_id(String), skip_holidays(Boolean), special_days(String), enable_outside_camera_check(Boolean), positions(List<TopPositionVo>), address(String), latitude(String), longitude(String), accuracy(String), title(String), modify_member(Boolean), enable_face_check(Boolean), check_need_healthy_code(Boolean), enable_camera_check(Boolean), shift_vo_list(List<TopShiftVo>), id(Number), enable_outside_check(Boolean), enable_next_day(Boolean), manager_list(String[]), workday_class_list(Number[]), default_class_id(Number), offset(Number), resource_permission_map(TopGroupManageRolePermissionVo), schedule(String), group_member(String), group_type(String), check_time(String), check_position_type(String), over_time_rule(String), camera_check(String), out_side_check(String), wifis(List<TopWifiVo>), mac_addr(String), ssid(String), disable_check_without_schedule(Boolean), freecheck_work_days(Number[]), freecheck_day_start_min_offset(Number), disable_check_when_rest(Boolean), enable_position_ble(Boolean), ble_device_list(List<TopAtBleDeviceVO>), device_id(Number)

## Returns
- optional: result(TopGroupVo), name(String), id(Number), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/attendance-group-write
updated_at: 2026-05-27 13:09:41
