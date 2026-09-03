# 获取模板code

doc_id: 15oFA2ERsw
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/get_by_name
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- name (String, required): 模板名称。

## Returns
- optional: errcode(Number), errmsg(String), request_id(String), process_code(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-template-code-based-on-the-template-name
updated_at: 2026-08-25 09:37:53
