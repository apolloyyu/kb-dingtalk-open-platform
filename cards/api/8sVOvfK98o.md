# 获取角色组列表

doc_id: 8sVOvfK98o
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/role/getrolegroup
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_get_department_list

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- group_id (Number, required): 角色组的ID。

## Returns
- optional: role_group(OpenRoleGroup), roles(OpenRole[]), role_id(Number), role_name(String), group_name(String), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-role-group-information
updated_at: 2026-05-27 13:09:26
