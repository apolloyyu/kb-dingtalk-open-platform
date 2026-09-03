# 获取公告详情

doc_id: vWebo1XTiO
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/blackboard/get
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，可通过获取企业内部应用的access_token接口获取。

## Body
- blackboard_id (String, required): 公告id，可以通过获取公告ID列表接口获取id参数值。
- operation_userid (String, required): 操作人userId。

## Returns
- optional: result(Object), id(String), author(String), title(String), content(String), category_id(String), private_level(Number), depname_list(String[]), username_list(String[]), gmt_create(String), gmt_modified(String), read_count(Number), unread_count(Number), coverpic_url(String), user_list(Object[]), staff_id(String), name(String), deptList(Object[]), dept_id(String), success(Boolean), errcode(Number), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-details-of-a-bulletin-that-is-not-deleted
updated_at: 2026-08-25 09:38:09
