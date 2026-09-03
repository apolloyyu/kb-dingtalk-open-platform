# 获取指定角色的员工列表

doc_id: BTSzqDJMWg
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/role/simplelist
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
- role_id (Number, required): 角色roleId，可通过调用获取角色列表接口获取id参数值。
- optional: size(Number), offset(Number)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(PageVo), hasMore(Boolean), list(OpenEmpSimple[]), userid(String), name(String), manageScopes(OrgDeptVo[]), dept_id(Number)

## Limits
- 分页大小。 **[!NOTE]** 与offset参数同时设置时才生效，此参数代表分页大小，默认值20，最大100。

source_url: https://open.dingtalk.com/document/development/obtain-the-list-of-employees-of-a-role
updated_at: 2026-05-27 13:09:29
