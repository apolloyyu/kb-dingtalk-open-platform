# 获取角色详情

doc_id: 5sZArHG6MW
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/role/getrole
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_get_department_member

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- roleId (Number, required): 角色ID，可调用获取角色列表接口获取id参数值。

## Returns
- optional: role(OpenRole), name(String), groupId(Number), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-role-details
updated_at: 2026-05-27 13:09:28
