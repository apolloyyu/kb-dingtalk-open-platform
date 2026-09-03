# 按照ID列表批量获取联系人数据

doc_id: AAf00PI4WI
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/crm/objectdata/contact/list
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_crm_maindata_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- data_id_list (String, required): 数据ID列表，通过根据指定条件查询联系人数据接口获取instance_id参数值，多个用英文逗号隔开。
- optional: current_operator_userid(String), provider_corpid(String)

## Returns
- optional: result_list(ObjectDataInstanceVo[]), gmt_modified(String), creator_userid(String), instance_id(String), data(String), extend_data(String), gmt_create(String), object_type(String), permission(DataPermissionVo), participant_userid_list(String[]), owner_userid_list(String[]), errcode(Number), errmsg(String)

## Limits
- 调用本接口，根据联系人实例id列表批量获取联系人数据，最多可一次获取200条数据。

source_url: https://open.dingtalk.com/document/development/retrieves-contact-data-in-batches-based-on-the-id-list
updated_at: 2026-06-08 09:53:25
