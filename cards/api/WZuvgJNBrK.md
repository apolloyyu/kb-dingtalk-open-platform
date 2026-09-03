# 查询订阅事件

doc_id: WZuvgJNBrK
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/call_back/get_call_back
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
- none

## Returns
- optional: url(String), aes_key(String), token(String), call_back_tag(String[]), errmsg(String), errcode(Number)

## Limits
- 加解密需要用到的token，可以随机填写，长度大于等于6个字符且少于64个字符。

source_url: https://open.dingtalk.com/document/development/query-subscribed-events
updated_at: 2026-09-02 18:13:41
