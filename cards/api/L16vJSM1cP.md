# 按照ID列表批量获取CRM自定义表单数据

doc_id: L16vJSM1cP
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/crm/objectdata/list
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_crm_customdata_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- data_id_list (String, required): 数据ID列表，多个用英文逗号隔开，可通过根据指定条件查询自定义对象数据接口获取instance_id参数值。
- name (String, required): 表单code，进入表单编辑页面，最下方可查看。iShot2022-11-01 20
- optional: current_operator_userid(String)

## Returns
- optional: result_list(ObjectDataInstanceVo[]), creator_nick(String), gmt_modified(String), creator_userid(String), instance_id(String), data(String), extend_data(String), gmt_create(String), object_type(String), permission(DataPermissionVo), participant_userid_list(String[]), owner_userid_list(String[]), proc_out_result(String), proc_inst_status(String), errcode(Number), errmsg(String)

## Limits
- 调用本接口，根据实例ID列表批量获取CRM自定义对象数据，最多可一次获取200条数据。

source_url: https://open.dingtalk.com/document/development/retrieves-custom-crm-forms-from-the-id-list
updated_at: 2026-06-08 09:53:18
