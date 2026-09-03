# 撤销员工待离职

doc_id: tdooKbEXXL
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrm/pendingDismission/revoke
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
- optional: userId(String)

## Returns
- optional: requestId(String), result(Boolean), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-revoketermination
updated_at: 2026-06-04 19:10:29
