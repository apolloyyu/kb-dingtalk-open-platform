# 批量新增地点

doc_id: zq96ahcncm
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/positions/add
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
- group_key (String, required): 考勤组ID。 **[!NOTE]** 如果你使用的考勤组标识是group_id，可以调用groupId转换为groupKey接口将group_id转换为group_key。
- position_list (Object[], required): postion列表，每次新增最多支持新增100个地点信息。
- address (String, required): 地址描述。
- foreign_id (String, required): 业务方positionId。
- longitude (String, required): 经度(支持6位小数)。
- latitude (String, required): 纬度(支持6位小数)。
- optional: op_userid(String), offset(Number)

## Returns
- optional: result(DingOpenResult), error_info_list(ErrorInfo[]), failure_list(Position[]), foreign_id(String), address(String), latitude(String), longitude(String), position_key(String), msg(String), code(String), success_list(Position[]), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- postion列表，每次新增最多支持新增100个地点信息。

source_url: https://open.dingtalk.com/document/development/atch-add-position-under-attendance-group
updated_at: 2026-05-27 13:10:08
