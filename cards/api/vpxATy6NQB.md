# 获取管理员的应用管理权限

doc_id: vpxATy6NQB
completeness: full
archived: false
method: GET
endpoint: https://oapi.dingtalk.com/user/can_access_microapp
api_version: v1-oapi
app_types: 第三方企业应用
permissions: qyapi_get_member

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取第三方企业的access_token接口获取。
- appId (Number, required): 应用ID。可在**钉钉开发者后台** **> 第三方企业应用**的应用详情页获取AppID。
- userId (String, required): 要查询的管理员员工ID，可调用获取管理员列表接口获取userid参数值。

## Body
- none

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), canAccess(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-administrator-s-microapplication-management-permission
updated_at: 2026-06-08 09:28:42
