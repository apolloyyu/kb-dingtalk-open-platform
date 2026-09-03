# 删除企业客户数据

doc_id: BRH3j2YyY6
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/crm/objectdata/customer/delete
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- operator_userid (String, required): 操作人用户userid。
- data_id (String, required): 客户实例ID，可通过根据指定条件查询个人或企业客户数据接口获取。

## Returns
- optional: result(ObjectDataDeleteDto), instance_id(String), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-crm-customer
updated_at: 2026-08-28 10:26:57
