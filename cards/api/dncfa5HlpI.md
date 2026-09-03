# 查询优先级列表

doc_id: dncfa5HlpI
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/project/organizations/users/{userId}/priorities
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_project

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。

## Query params
- none

## Body
- none

## Returns
- optional: result(Array), color(String), name(String), priorityId(String), priority(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-a-priority-list
updated_at: 2026-06-04 19:11:44
