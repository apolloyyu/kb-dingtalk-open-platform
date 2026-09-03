# 删除外部联系人

doc_id: hD9G5lxqmw
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/extcontact/delete
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_ext_write

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- user_id (String, required): 要删除的外部联系人的userId，可以调用获取外部联系人列表接口获取userid参数值。

## Returns
- optional: errcode(Number), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-external-contact
updated_at: 2026-05-27 13:09:31
