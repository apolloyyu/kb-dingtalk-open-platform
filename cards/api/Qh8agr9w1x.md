# 获取jsapi_ticket

doc_id: Qh8agr9w1x
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/get_jsapi_ticket
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
- none

## Returns
- optional: expires_in(Number), ticket(String), errmsg(String), errcode(Number)

## Limits
- 生成的临时jsapi_ticket。 **[!NOTE]** 企业内部应用是以应用维度获取jsapi_ticket的，所以在使用的时候需要将jsapi_ticket以appKey为维度进行缓存下来（设置缓存过期时间2小时），并不需要每次都通过接口拉取。

source_url: https://open.dingtalk.com/document/development/obtain-jsapi-ticket
updated_at: 2026-08-25 09:36:28
