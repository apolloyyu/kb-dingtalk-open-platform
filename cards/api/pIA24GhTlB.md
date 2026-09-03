# 获取应用自定义空间使用详情

doc_id: pIA24GhTlB
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/cspace/used_info
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。
- domain (String, required): 企业调用时传入，需要为10个字节以内的字符串，仅可包含字母和数字，大小写不敏感。
- agent_id (String, required): 应用的AgentId。 - 企业内部应用可以在开发者后台的应用详情页获取。 - 第三方企业应用可以调用获取企业授权信息接口获取。

## Body
- none

## Returns
- optional: used_size(String), errmsg(String), errcode(Number)

## Limits
- 企业调用时传入，需要为10个字节以内的字符串，仅可包含字母和数字，大小写不敏感。

source_url: https://open.dingtalk.com/document/development/queries-the-usage-details-of-a-custom-application-space
updated_at: 2026-08-25 09:38:17
