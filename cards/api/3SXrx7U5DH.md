# 创建或更新数据表单模板

doc_id: 3SXrx7U5DH
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/dataForms/templates
api_version: v2-new
app_types: 企业内部应用
permissions: Premium.Workflow.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- name (String, required): 表单模板名称。
- formComponents (Array, required): 表单控件列表，单一表单最大组件个数不超过200。
- FormComponent (FormComponent, required): 表单控件列表。详情请参考**FormComponent参数补充说明**。
- userId (String, required): 操作人userId，需为管理员。
- optional: processCode(String), description(String)

## Returns
- optional: result(Object), processCode(String)

## Limits
- 表单控件列表，单一表单最大组件个数不超过200。

source_url: https://open.dingtalk.com/document/development/api-premiumsaveform
updated_at: 2026-06-03 10:13:02
