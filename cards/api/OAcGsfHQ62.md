# 智能人事员工转正

doc_id: OAcGsfHQ62
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrm/processes/regulars/become
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
- userId (String, required): 待转正用户userId。
- regularDate (Long, required): 转正时间，unix时间戳，单位毫秒。
- operationId (String, required): 操作用户userId。
- optional: remark(String)

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/intelligent-personnel-staff-to-become-regular
updated_at: 2026-06-04 19:10:32
