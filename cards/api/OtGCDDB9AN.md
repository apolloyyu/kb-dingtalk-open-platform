# 根据unionid获取用户userid

doc_id: OtGCDDB9AN
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/user/getUseridByUnionid
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。
- unionid (String, required): 用户在当前钉钉开放平台账号范围内的唯一标识，同一个钉钉开放平台账号可以包含多个开放应用，同时也包含ISV的套件应用及企业应用。 可通过调用查询用户详情接口获取。

## Body
- none

## Returns
- optional: errmsg(String), errcode(Number), contactType(Number), userid(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/you-can-call-this-operation-to-retrieve-the-userids-of
updated_at: 2026-08-25 09:36:56
