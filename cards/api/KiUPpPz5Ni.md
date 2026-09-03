# 获取企业已有的所有离职原因

doc_id: KiUPpPz5Ni
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/hrm/dismission/reasons
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
- none

## Returns
- optional: requestId(String), success(Boolean), result(Object), passiveList(Array), id(String), name(String), voluntaryList(Array)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getalldismissionreasons
updated_at: 2026-06-04 19:10:30
