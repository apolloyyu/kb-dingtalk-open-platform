# 根据指定条件查询跟进记录数据

doc_id: RO3Ytp4ye8
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/crm/objectdata/followrecord/query
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_crm_maindata_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- page_size (Number, required): 分页大小。
- optional: current_operator_userid(String), cursor(String), query_dsl(String)

## Returns
- optional: result(IterablePage), next_cursor(String), values(Values[]), creator_nick(String), gmt_modified(String), creator_userid(String), instance_id(String), data(String), extend_data(String), gmt_create(String), object_type(String), permission(DataPermissionVo), owner_userid_list(String[]), participant_userid_list(String[]), has_more(Boolean), page_size(Number), errcode(Number), errmsg(String)

## Limits
- 调用本接口，根据指定查询条件批量获取跟进记录数据，最多可一次获取200条数据。

source_url: https://open.dingtalk.com/document/development/query-and-dingtalk-data-of-track-records-in-apsara-stack
updated_at: 2026-06-08 09:53:23
