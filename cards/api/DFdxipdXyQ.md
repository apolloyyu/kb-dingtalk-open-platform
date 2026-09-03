# 查询员工智能考勤机列表

doc_id: DFdxipdXyQ
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/smartdevice/atmachine/get_by_userid
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_dingtalk_attendance_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- param (UserMachineInfoRequestVo, required): 请求结构。
- offset (Number, required): 分页游标，从0开始的非负整数。
- size (Number, required): 每页大小，最大值50。
- userid (String, required): 员工userId。

## Returns
- optional: result(MachineInfoResultVo), machine_list(MachineVo[]), deviceid(String), device_name(String), product_name(String), devid(Number), has_more(Boolean), errcode(Number), errmsg(String)

## Limits
- 每页大小，最大值50。

source_url: https://open.dingtalk.com/document/development/query-the-list-of-employee-intelligent-attendance-machines
updated_at: 2026-05-27 17:06:20
