# 获取离职员工列表

doc_id: zEgGjCM3r4
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/querydimission
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- offset (Number, required): 分页游标，从0开始。根据返回结果里的next_cursor是否为空来判断是否还有下一页，且再次调用时offset设置成next_cursor的值。
- size (Number, required): 分页大小，最大50。

## Returns
- optional: result(Paginator), next_cursor(Number), data_list(String[]), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- 分页大小，最大50。

source_url: https://open.dingtalk.com/document/development/intelligent-personnel-query-company-turnover-list
updated_at: 2026-08-25 09:39:09
