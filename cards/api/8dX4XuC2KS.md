# 常见问题

doc_id: 8dX4XuC2KS
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/v2/user/getuserinfo
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
- none

## Limits
- **关键术语说明**：`tmp_auth_code` 是通过前端 JSAPI（如`dd.getAuthCode`或`dd.runtime.permission.requestAuthCode`）获取的一次性临时授权码，有效期为 5 分钟，仅能使用一次。服务端需将其传递给钉钉 API（如`/user/get`），以换取用户身份标识。
- - 免登授权码生成后，有效期为 **5分钟**，超过时间则失效。
- - ssoCode 通常具有较短的有效期（约5分钟），请确保及时使用。

source_url: https://open.dingtalk.com/document/development/development-mlogon-faq
updated_at: 2026-08-03 09:18:07
