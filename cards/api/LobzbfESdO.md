# 获取企业内部小程序的版本列表

doc_id: LobzbfESdO
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/microApp/innerMiniApps/{agentId}/versions
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_get_microapp_list

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- agentId (Long, required): 应用AgentId。 image

## Query params
- none

## Body
- none

## Returns
- optional: appVersionList(Array), appVersionId(Long), miniAppId(String), appVersion(String), appVersionType(Integer), miniAppOnPc(Boolean), createTime(String), modifyTime(String), entranceLink(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-the-version-list-of-the-enterprise-internal-applet
updated_at: 2026-07-14 09:22:21
