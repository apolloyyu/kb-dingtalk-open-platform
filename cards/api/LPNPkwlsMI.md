# 获取企业应用的可使用范围

doc_id: LPNPkwlsMI
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/microApp/apps/{agentId}/scopes
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_microapp_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- agentId (Long, required): 应用agentId，参考AgentId。

## Query params
- none

## Body
- none

## Returns
- optional: result(Object), userIds(Array of String), deptIds(Array of Long), roleIds(Array of Long), onlyAdminVisible(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-application-visible-range
updated_at: 2026-10-09 18:08:49
