# 批量获取企业客户数据

doc_id: CTZd30TsOp
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/crm/objectdata/customer/list
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
- data_id_list (String, required): 数据ID列表，多个用英文逗号隔开，可通过批量获取客户数据接口获取。
- optional: current_operator_userid(String)

## Returns
- optional: result_list(ObjectDataInstanceVo[]), creator_nick(String), gmt_modified(String), creator_userid(String), instance_id(String), data(String), extend_data(String), gmt_create(String), object_type(String), permission(DataPermissionVo), participant_userid_list(String[]), owner_userid_list(String[]), errcode(Number), errmsg(String)

## Limits
- 调用本接口根据实例ID列表批量获取客户记录数据，最多可一次获取200条数据。

source_url: https://open.dingtalk.com/document/development/obtains-customer-data-in-batches-based-on-the-id-list
updated_at: 2026-08-28 10:27:01
