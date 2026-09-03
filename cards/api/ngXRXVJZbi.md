# 获取用户创建的填表模板

doc_id: ngXRXVJZbi
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/collection/form/list
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- offset (Number, required): 分页游标，从0开始。后续取返回结果中next_cursor的值。
- size (Number, required): 分页大小，最大200。
- optional: biz_type(Number), creator(String)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(PageResult), has_more(Boolean), next_cursor(Number), list(FormSchemaResponse[]), form_code(String), name(String), memo(String), setting(FormSchemaSettingVo), form_type(Number), loop_time(String), loop_days(Number[]), should_participation_cnt(Number), end_time(Date), create_time(Date), biz_type(Number), stop(Boolean), creator(String)

## Limits
- 分页大小，最大200。

source_url: https://open.dingtalk.com/document/development/obtains-the-template-that-a-user-creates
updated_at: 2026-08-25 09:39:17
