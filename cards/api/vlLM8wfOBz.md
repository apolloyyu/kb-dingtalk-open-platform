# 查询用户是否实名

doc_id: vlLM8wfOBz
completeness: full
archived: true
method: GET
endpoint: https://api.dingtalk.com/v1.0/esign/users/{userId}
api_version: v2-new
app_types: 第三方企业应用
permissions: not_stated

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 当前用户userid。

## Query params
- none

## Body
- none

## Returns
- optional: data(Object), realName(Boolean), userRealName(String), code(Integer), message(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-whether-a-user-has-a-real-name
updated_at: 2026-08-25 09:37:30
