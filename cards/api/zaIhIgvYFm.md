# 获取部门用户基础信息

doc_id: zaIhIgvYFm
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/user/listsimple
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
- dept_id (Number, required): 部门ID，如果是根部门，该参数传1，可调用获取部门列表获取dept_id参数值。
- cursor (Number, required): 分页查询的游标，最开始传0，后续传返回参数中的next_cursor值。
- size (Number, required): 分页长度，最大值100。
- optional: order_field(String), contain_access_limit(Boolean), language(String)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(PageResult), has_more(Boolean), next_cursor(Number), list(ListUserSimpleResponse[]), userid(String), name(String)

## Limits
- 分页长度，最大值100。

source_url: https://open.dingtalk.com/document/development/queries-the-simple-information-of-a-department-user
updated_at: 2026-06-08 09:28:33
