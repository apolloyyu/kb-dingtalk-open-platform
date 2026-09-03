# 获取角色列表

doc_id: rtTxtM7fQC
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/role/list
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
- optional: size(Number), offset(Number)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(PageVo), hasMore(Boolean), list(OpenRoleGroup[]), name(String), groupId(Number), roles(OpenRole[]), id(Number)

## Limits
- 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小**，**默认值20**，**最大值200。

source_url: https://open.dingtalk.com/document/development/obtains-a-list-of-enterprise-roles
updated_at: 2026-05-27 13:09:27
