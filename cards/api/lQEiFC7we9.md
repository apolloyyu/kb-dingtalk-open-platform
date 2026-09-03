# 根据指定条件查询联系人数据

doc_id: lQEiFC7we9
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/crm/objectdata/contact/query
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- page_size (Number, required): 分页大小。
- optional: current_operator_userid(String), cursor(String), provider_corpid(String), query_dsl(String)

## Returns
- optional: result(IterablePage), next_cursor(String), values(Values[]), gmt_modified(String), creator_userid(String), instance_id(String), data(String), extend_data(String), gmt_create(String), object_type(String), permission(DataPermissionVo), participant_userid_list(String[]), owner_userid_list(String[]), has_more(Boolean), page_size(Number), errcode(Number), errmsg(String)

## Limits
- 调用本接口，根据指定查询条件批量获取联系人数据，最多可一次获取200条数据。

source_url: https://open.dingtalk.com/document/development/dingtalk-the-contact-data-query-api
updated_at: 2026-08-28 10:27:05
