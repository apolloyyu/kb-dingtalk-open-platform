# 获取填表实例数据

doc_id: vM9BjJGQZs
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/collection/instance/list
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
- form_code (String, required): 填表模板code，调用获取用户创建的填表模板接口获取。
- offset (Number, required): 分页起始，从0开始。当返回结果中has_more为false时，表示没有下一页了。否则取返回结果中next_cursor的值作为下一次请求的offset。
- size (Number, required): 分页大小，最大100。
- optional: action_date(String), biz_type(Number)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(PageResult), has_more(Boolean), list(FormInstanceResponse[]), create_time(Date), submitter_userid(String), submitter_user_name(String), forms(FormData[]), value(String), label(String), key(String), student_class_name(String), student_name(String), student_class_id(Number), student_user_id(String), modify_time(Date), form_instance_id(String), next_cursor(Number)

## Limits
- 分页大小，最大100。

source_url: https://open.dingtalk.com/document/development/obtains-multiple-form-filling-records
updated_at: 2026-08-25 09:39:18
