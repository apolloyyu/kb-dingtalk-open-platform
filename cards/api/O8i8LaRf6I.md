# 获取用户考勤数据

doc_id: O8i8LaRf6I
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/getupdatedata
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_get_attendance_data

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- userid (String, required): 用户的userId。
- work_date (Date, required): 查询日期。

## Returns
- optional: errmsg(String), result(AtCheckInfoForOpenVo), work_date(Date), attendance_result_list(AtAttendanceResultForOpenVo[]), record_id(Number), source_type(String), plan_check_time(Date), class_id(Number), location_method(String), location_result(String), outside_remark(String), plan_id(Number), user_address(String), group_id(Number), user_check_time(Date), procInst_id(String), check_type(String), time_result(String), userid(String), approve_list(AtApproveForOpenVo[]), duration_unit(String), duration(String), sub_type(String), tag_name(String), begin_time(Date), biz_type(Number), end_time(Date), gmt_finished(Date), check_record_list(AtAttendanceRecordForOpenVo[]), user_accuracy(String), valid_matched(Boolean), user_longitude(String), user_ssid(String), base_accuracy(String), user_mac_addr(String), user_latitude(String), base_address(String), invalid_record_msg(String), invalid_record_type(String), corpId(String), class_setting_info(AtClassSettingInfoForOpenVo), rest_time_vo_list(AtRestTimeVo[]), rest_end_time(Number), rest_begin_time(Number), errcode(Number), success(Boolean), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-attendance-update-data
updated_at: 2026-06-23 10:39:15
