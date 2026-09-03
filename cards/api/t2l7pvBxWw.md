# 获取指定用户可见的审批表单列表

doc_id: t2l7pvBxWw
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/listbyuserid
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- offset (Number, required): 分页游标，从0开始。根据返回结果里的next_cursor是否为空来判断是否还有下一页，且再次调用时offset设置成next_cursor的值。
- size (Number, required): 分页大小，最大可设置成100。
- optional: userid(String)

## Returns
- optional: request_id(String), errmsg(String), errcode(Number), result(HomePageProcessTemplateVo), process_list(ProcessTopVo[]), name(String), icon_url(String), process_code(String), url(String), next_cursor(Number)

## Limits
- 分页大小，最大可设置成100。
- 调用本接口根据员工的userid分页获取该用户可见的审批表单列表，每次最多获取100个表单。

source_url: https://open.dingtalk.com/document/development/you-can-call-this-operation-to-retrieve-a-list-of
updated_at: 2026-08-25 09:37:46
