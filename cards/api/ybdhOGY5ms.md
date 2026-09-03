# 获取未登录钉钉的员工列表

doc_id: ybdhOGY5ms
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/inactive/user/v2/get
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_liveness_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- is_active (Boolean, required): 是否活跃： - **false**：未登录 - **true**：登录
- offset (Number, required): 支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。
- size (Number, required): 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。
- query_date (String, required): 查询日期，日期格式为：yyyyMMdd。
- optional: dept_ids(String)

## Returns
- optional: result(PageVo), next_cursor(Number), list(String[]), has_more(Boolean), errmsg(String), errcode(Number), request_id(String)

## Limits
- 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。
- - 调用本接口只能获取一个月内未登录钉钉的员工列表。

source_url: https://open.dingtalk.com/document/development/queries-the-inactive-users-or-active-users-under-an-enterprise
updated_at: 2026-06-08 09:28:37
