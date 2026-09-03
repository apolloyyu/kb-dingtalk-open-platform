# 获取部门用户基础信息

doc_id: 5bintD8CMc
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/user/simplelist
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。
- department_id (Number, required): 获取的部门ID。1表示根部门。
- optional: lang(String), offset(Number), size(Number), order(String)

## Body
- none

## Returns
- optional: userlist(Userlist[]), userid(String), name(String), errcode(Number), errmsg(String), hasMore(Boolean)

## Limits
- 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。

source_url: https://open.dingtalk.com/document/development/obtain-the-basic-information-of-department-users
updated_at: 2026-08-25 09:36:52
