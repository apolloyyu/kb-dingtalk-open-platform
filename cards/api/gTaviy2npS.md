# 创建班次

doc_id: gTaviy2npS
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/shift/add
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
- op_user_id (String, required): 操作人userId。
- shift (TopAtClassVo, required): 班次。
- name (String, required): 班次名称。
- sections (TopAtSectionVo[], required): 卡段。
- times (TopAtTimeVo[], required): 打卡信息。
- check_type (String, required): 打卡类型： - **OnDuty**：上班 - **OffDuty**：下班
- across (Number, required): 是否跨天： - **0**：不跨天 - **1**：跨天
- check_time (Date, required): 打卡时间。
- optional: owner(String), class_group_name(String), corp_id(String), id(Number), end_min(Number), free_check(Boolean), begin_min(Number), setting(TopAtClassSettingVo), rest_begin_time(TopAtTimeVo), class_id(Number), is_flexible(Boolean), is_deleted(String), rest_end_time(TopAtTimeVo), serious_late_minutes(Number), absenteeism_late_minutes(Number), extras(Json), tags(String), service_id(Number)

## Returns
- optional: result(TopAtClassVo), id(Number), name(String), errmsg(String), errcode(Number), success(Boolean), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-modify-shifts
updated_at: 2026-05-27 17:05:54
