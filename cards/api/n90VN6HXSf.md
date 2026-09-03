# 更新事件接口

doc_id: n90VN6HXSf
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/call_back/update_call_back
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
- call_back_tag (String[], required): 需要监听的事件类型，可通过查询订阅事件接口获取。
- token (String, required): 加解密需要用到的token，可以随机填写，长度大于等于6个字符且少于64个字符。
- aes_key (String, required): 数据加密密钥。用于回调数据的加密，长度固定为43个字符，从a-z, A-Z, 0-9共62个字符中选取,您可以随机生成，ISV(服务提供商)推荐使用注册套件时填写的EncodingAESKey。
- url (String, required): 接收事件回调的url，必须是公网可以访问的url地址。

## Returns
- optional: errmsg(String), errcode(Number)

## Limits
- 加解密需要用到的token，可以随机填写，长度大于等于6个字符且少于64个字符。
- 数据加密密钥。用于回调数据的加密，长度固定为43个字符，从a-z, A-Z, 0-9共62个字符中选取,您可以随机生成，ISV(服务提供商)推荐使用注册套件时填写的EncodingAESKey。

source_url: https://open.dingtalk.com/document/development/update-event-interface
updated_at: 2026-09-02 18:13:40
