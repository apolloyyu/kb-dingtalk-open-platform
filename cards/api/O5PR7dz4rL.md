# 回滚企业内部小程序版本

doc_id: O5PR7dz4rL
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/microApp/innerMiniApps/{agentId}/versions/rollback
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_microapp_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- agentId (Long, required): 应用AgentId。

## Query params
- none

## Body
- appVersionId (Long, required): 小程序版本ID，用于唯一标识一个历史版本。可通过调用获取企业内部小程序历史版本列表接口，在返回结果中获取`appVersionId`字段值。
- opUnionId (String, required): 操作人的unionId，必须为当前企业内拥有应用管理权限的有效管理员，可通过查询用户详情接口获取`unionId`参数值。

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/rollback-of-enterprise-internal-applet-version
updated_at: 2026-06-03 11:47:36
