# 更新企业客户数据

doc_id: AkrTjiDKmL
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/crm/objectdata/customer/update
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
- instance (ObjectDataInstanceVo, required): 客户数据。
- data (String, required): 数据内容，JSON格式字符串。
- instance_id (String, required): 客户数据ID，可通过批量获取客户数据接口获取。
- modifier_userid (String, required): 用户userid。
- optional: extend_data(String), permission(DataPermissionVo), participant_userids(String[]), owner_userids(String[]), modifier_nick(String), skip_duplicate_check(Boolean), action(String)

## Returns
- optional: result(ObjectDataCreateDto), instance_id(String), success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/dingtalk-paas-master-data-update-crm-customer-data
updated_at: 2026-08-28 10:26:56
