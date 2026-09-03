# 修改已离职员工信息

doc_id: 5DlAg1fVZ6
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/hrm/processes/employees/terminations
api_version: v2-new
app_types: 企业内部应用
permissions: Hrm.Process.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 已离职员工的userId，可调用获取离职员工列表接口获取离职员工userId。
- lastWorkDate (Long, required): 最后工作日，即离职日期，格式为毫秒值时间戳。
- dismissionMemo (String, required): 离职备注信息。

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/modify-resigned-employee-information
updated_at: 2026-06-04 19:10:27
