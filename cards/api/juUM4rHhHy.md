# 获取招聘流程标识

doc_id: juUM4rHhHy
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/ats/flows/ids
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_recruitment_plugin

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- relationEntity (String, required): 招聘流程关联实体，参数请传interview。 目前仅支持面试。
- relationEntityId (String, required): 招聘流程关联实体标识。
- optional: bizCode(String)

## Body
- none

## Returns
- optional: flowId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-recruitment-process-identity
updated_at: 2026-06-04 19:10:35
