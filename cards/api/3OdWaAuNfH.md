# 创建企业客户数据

doc_id: 3OdWaAuNfH
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/crm/objectdata/customer/create
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
- instance (ObjectDataInstanceVo, required): 企业客户数据。
- creator_userid (String, required): 记录创建人的用户ID。
- data (String, required): 客户数据内容，JSON格式字符串。传参格式详见自定义控件字段格式说明V1。
- optional: action(String), skip_duplicate_check(Boolean), extend_data(String), permission(DataPermissionVo), participant_userids(String[]), owner_userids(String[])

## Returns
- optional: result(ObjectDataCreateDto), instance_id(String), success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/dingtalk-paas-master-data-create-crm-customer-data
updated_at: 2026-08-28 10:26:54
