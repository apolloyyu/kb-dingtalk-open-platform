# 更新自定义对象数据

doc_id: ZQ3qGl80Y0
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/update
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_crm_customdata_write

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- instance (ObjectDataInstanceVo, required): 自定义对象数据。
- data (String, required): 数据内容。
- instance_id (String, required): 自定义对象数据ID，可通过根据指定条件查询自定义对象数据接口获取instance_id参数值。
- form_code (String, required): 自定义对象表单code，进入自定义表单编辑页面，最下方可查看。iShot2022-11-01 20
- modifier_userid (String, required): 钉钉用户userId。
- optional: extend_data(String), permission(DataPermissionVo), participant_userids(String[]), modifier_nick(String)

## Returns
- optional: result(ObjectDataCreateDto), instance_id(String), success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/crm-master-data-opens-interface-for-updating-custom-object-data
updated_at: 2026-06-08 09:53:20
