# 获取用户考勤组

doc_id: wHy5x571ML
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/getusergroup
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- userid (String, required): 员工在企业内的userId。

## Returns
- optional: result(AtGroupFullForTopVo), name(String), group_id(Number), type(String), classes(AtClassVo[]), class_id(Number), sections(AtSectionVo[]), times(AtTimeVo[]), check_time(Date), check_type(String), across(Number), begin_min(Number), end_min(Number), setting(ClassSettingVo), rest_begin_time(AtTimeVo), rest_end_time(AtTimeVo), errcode(Number), errmsg(String), request_id(String)

## Limits
- 调用本接口，获取员工的考勤组信息，包括考勤组名称、考勤类型等，一个员工在一个企业中只能属于一个考勤组。

source_url: https://open.dingtalk.com/document/development/queries-a-user-attendance-group
updated_at: 2026-05-27 13:09:52
