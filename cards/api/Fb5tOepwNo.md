# 钉钉文本翻译

doc_id: Fb5tOepwNo
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/ai/mt/translate
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- query (String, required): 翻译源文字符串。
- source_language (String, required): 翻译源语言类型。
- target_language (String, required): 翻译目标语言类型。

## Returns
- optional: result(String), errcode(Number), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/dingtalk-translation
updated_at: 2026-06-03 09:50:59
