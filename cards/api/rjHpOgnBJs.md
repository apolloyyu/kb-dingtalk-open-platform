# 创建或更新审批表单模板

doc_id: rjHpOgnBJs
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/forms
api_version: v2-new
app_types: 第三方企业应用
permissions: Workflow.Form.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- name (String, required): 表单模板名称，最大长度200字符。
- formComponents (Array, required): 表单控件列表，单一表单最大组件个数不超过200。
- FormComponent (FormComponent, required): 表单控件列表，详情请参考FormComponent参数说明参数补充说明。
- optional: processCode(String), description(String), templateConfig(Object), disableStopProcessButton(Boolean), hidden(Boolean), disableDeleteProcess(Boolean), disableFormEdit(Boolean), disableResubmit(Boolean), disableHomepage(Boolean), dirId(String), originDirId(String)

## Returns
- optional: result(Object), processCode(String)

## Limits
- 表单模板名称，最大长度200字符。
- 表单模板描述，最大长度300字符。
- 表单控件列表，单一表单最大组件个数不超过200。
- - 每个企业最多创建200个官方审批模板，超过最大数量后调用接口会报错。

source_url: https://open.dingtalk.com/document/development/create-an-approval-form-template
updated_at: 2026-06-03 10:12:21
