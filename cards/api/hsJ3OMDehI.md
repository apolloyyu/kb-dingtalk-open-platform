# 获取未登录钉钉的员工列表

doc_id: hsJ3OMDehI
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/inactive/user/get
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，可通过获取企业内部应用的access_token接口获取。

## Body
- query_date (String, required): 查询日期，日期格式为yyyyMMdd。
- offset (Number, required): 支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。
- size (Number, required): 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。

## Returns
- optional: result(PageVo), has_more(Boolean), list(String[]), request_id(String), errcode(Number)

## Limits
- 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。
- > - 调用本接口只能获取一个月内未登录钉钉的员工列表。

source_url: https://open.dingtalk.com/document/development/query-data-of-inactive-users
updated_at: 2026-08-25 09:36:55
