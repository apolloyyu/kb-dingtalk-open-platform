# 获取定制应用的access_token

doc_id: zpla4g9gDQ
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/service/get_corp_token
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- optional: expires_in(Number), access_token(String), errmsg(String), errcode(Number)

## Limits
- - access_token的有效期为7200秒（2小时），有效期内重复获取会返回新的access_token。

source_url: https://open.dingtalk.com/document/development/obtains-the-enterprise-authorized-credential
updated_at: 2026-08-25 09:36:32
