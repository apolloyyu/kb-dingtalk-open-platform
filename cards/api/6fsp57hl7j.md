# 发布企业内部小程序版本

doc_id: 6fsp57hl7j
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/microApp/innerMiniApps/{agentId}/versions/publish
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_microapp_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- agentId (Long, required): 应用的AgentId，请参考基础概念-AgentId。

## Query params
- none

## Body
- appVersionId (Long, required): 小程序版本id，用于唯一标识小程序版本信息，可调用获取企业内部小程序的版本列表接口，获取返回参数中 `appVersionId` 字段值。
- opUnionId (String, required): 操作人的unionId，该用户必须是拥有**应用管理权限**的管理员，可调用查询用户详情接口获取。
- optional: publishType(String), miniAppOnPc(Boolean)

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/release-internal-applet-version
updated_at: 2026-06-04 19:10:07
