# 查询管理员是否有应用管理权限

doc_id: IFROzfBJX5
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/microApp/apps/{agentId}/users/{userId}/adminAccess
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_get_member

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- agentId (Long, required): 授权企业安装三方应用时的agentId，可调用获取企业开通应用后的授权信息接口获取agentId参数值。
- userId (String, required): 授权企业管理员userId，可调用获取管理员列表接口获取userid参数值。

## Query params
- none

## Body
- none

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/check-whether-the-administrator-has-application-management-permissions
updated_at: 2026-06-01 16:10:32
