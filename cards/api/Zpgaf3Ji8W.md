# 获取企业下的自定义空间

doc_id: Zpgaf3Ji8W
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/cspace/get_custom_space
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。
- domain (String, required): 企业调用时传入，需要为10个字节以内的字符串，仅可包含字母和数字，大小写不敏感。
- optional: agent_id(String)

## Body
- none

## Returns
- optional: spaceid(String), errmsg(String), errcode(Number)

## Limits
- 企业调用时传入，需要为10个字节以内的字符串，仅可包含字母和数字，大小写不敏感。

source_url: https://open.dingtalk.com/document/development/obtain-user-space-under-the-enterprise
updated_at: 2026-08-25 09:38:15
