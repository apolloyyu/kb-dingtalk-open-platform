# 查询实人认证状态

doc_id: hLhTovXZJz
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/persons/identificationStates/query
api_version: v2-new
app_types: 企业内部应用
permissions: Custom.Ding.RealPeople.Recognize

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userIds (Array of String, required): 员工userId列表。

## Returns
- optional: data(Array), state(Integer), userId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-the-id-verification-status
updated_at: 2026-06-02 19:19:55
