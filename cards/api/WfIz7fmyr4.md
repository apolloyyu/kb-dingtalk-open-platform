# 创建CRM自定义对象数据

doc_id: WfIz7fmyr4
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/create
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_crm_customdata_write

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- instance (ObjectDataInstanceVo, required): 自定义对象数据。
- creator_userid (String, required): 创建人的用户userId。
- data (String, required): 数据内容，JSON格式字符串。传参格式详见自定义控件字段格式说明V1。
- form_code (String, required): 自定义对象表单code，进入自定义表单编辑页面，最下方可查看。 iShot2022-11-01 20
- optional: extend_data(String), permission(DataPermissionVo), participant_userids(String[])

## Returns
- optional: result(ObjectDataCreateDto), instance_id(String), success(Boolean), errcode(Number), errmsg(String)

## Limits
- 本接口只能创建纯表单数据，不能用于创建流程表单数据。

source_url: https://open.dingtalk.com/document/development/dingtalk-paas-master-create-custom-crm-object-data
updated_at: 2026-06-08 09:53:21
