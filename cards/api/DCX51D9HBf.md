# 通知补卡通过

doc_id: DCX51D9HBf
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/approve/check
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_attendance_group_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- userid (String, required): 员工的userId。
- work_date (String, required): 要补卡的时间，可通过批量查询人员排班信息接口获取的work_date值。
- punch_id (Number, required): 要补的排班ID，可通过批量查询人员排班信息接口获取的shift_id值。
- punch_check_time (String, required): 排班的打卡时间，可通过批量查询人员排班信息接口获取的plan_check_time值。
- user_check_time (String, required): 用户打卡时间。
- approve_id (String, required): 审批单ID，自定义值。
- jump_url (String, required): 审批单跳转地址。
- tag_name (String, required): 审批单名称。

## Returns
- optional: errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/make-up-the-card-after-approval
updated_at: 2026-05-27 17:06:22
