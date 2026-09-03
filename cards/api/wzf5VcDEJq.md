# 根据指定条件查询自定义对象数据

doc_id: wzf5VcDEJq
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/crm/objectdata/query
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
- page_size (Number, required): 分页大小。
- name (String, required): 自定义表单code，进入自定义表单编辑页面，最下方可查看。 iShot2022-11-01 20
- optional: current_operator_userid(String), cursor(String), query_dsl(String)

## Returns
- optional: result(IterablePage), next_cursor(String), values(Values[]), creator_nick(String), gmt_modified(String), creator_userid(String), instance_id(String), data(String), extend_data(String), gmt_create(String), object_type(String), permission(DataPermissionVo), participant_userid_list(String[]), owner_userid_list(String[]), proc_inst_status(String), proc_out_result(String), has_more(Boolean), page_size(Number), errcode(Number), errmsg(String)

## Limits
- 调用本接口，带条件分页查询自定义对象数据，最多可一次获取200条数据。

source_url: https://open.dingtalk.com/document/development/retrieve-custom-crm-object-data
updated_at: 2026-08-28 10:27:07
