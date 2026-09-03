# 删除CRM自定义对象数据

doc_id: EmvpMXNXQx
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/crm/customObjectDatas/instances/{instanceId}
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_crm_maindata_write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- instanceId (String, required): CRM自定义对象数据ID，可通过根据指定条件查询自定义对象数据接口获取instance_id参数值。

## Query params
- formCode (String, required): 自定义对象表单code。 在客户管理应用的**客户管理管理后台**页面，进入表单编辑页面，在最下方可查看表单code。

## Body
- none

## Returns
- optional: instanceId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-crm-custom-object-data
updated_at: 2026-06-04 19:12:15
