# 获取应用的 Access Token

doc_id: Py2b80tmOx
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/oauth2/{corpId}/token
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- corpId (String, required): 组织ID，应用运行在哪个组织就填写哪个组织的 corpId： - 企业内部应用：填写本企业 corpId。 - 第三方企业应用：填写开通应用的授权企业的 corpId。

## Query params
- none

## Body
- client_id (String, required): 应用的 ClientID。
- client_secret (String, required): 应用的 ClientSecret。
- grant_type (String, required): 授权类型：client_credentials

## Returns
- optional: access_token(String), expires_in(Integer)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-gettoken
updated_at: 2026-06-08 12:02:05
