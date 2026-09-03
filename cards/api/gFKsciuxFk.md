# 删除联系人数据

doc_id: gFKsciuxFk
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/crm/objectdata/contact/delete
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_crm_maindata_write

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- operator_userid (String, required): 操作人用户userId。
- data_id (String, required): 联系人实例ID，通过根据指定条件查询联系人数据接口获取instance_id参数值。

## Returns
- optional: result(ObjectDataDeleteDto), instance_id(String), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-crm-contact
updated_at: 2026-06-08 09:53:28
