# 删除场景群成员

doc_id: Hq2KLlwBXZ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/im/sceneGroup/member/delete
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_chat_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的accessToken接口获取。 - 第三方企业应用，通过获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- open_conversation_id (String, required): 群会话Id。
- optional: user_ids(Array of String), union_ids(Array of String)

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-removescenegroupmember
updated_at: 2026-08-14 09:41:52
