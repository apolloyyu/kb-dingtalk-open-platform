# 删除部门

doc_id: OHVbp3SCVX
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/department/delete
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_manage_addresslist

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- dept_id (Number, required): 要删除的部门ID，可通过获取部门列表接口获取dept_id参数值。

## Returns
- optional: errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/address-book-deletion-department
updated_at: 2026-05-27 13:09:13
