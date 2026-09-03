# 查询花名册中有权限的字段列表

doc_id: ShGePqnuem
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/hrm/rosters/meta/authorities/fields
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_hrm_read_user

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- appAgentId (Long, required): 应用的agentId，可调用获取获取企业授权信息接口获取agentId参数值。

## Body
- none

## Returns
- optional: result(Array), fieldCode(String), fieldName(String), fieldType(String), optionText(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-the-list-of-fields-with-permissions-in-the-roster
updated_at: 2026-06-04 19:10:25
