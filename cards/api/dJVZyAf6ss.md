# 保存流程中心外部集成审批模板

doc_id: dJVZyAf6ss
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/processCentres/schemas
api_version: v2-new
app_types: 第三方企业应用
permissions: Premium.Workflow.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- name (String, required): 表单模板名称。
- formComponents (Array, required): 表单控件列表，详情请参考FormComponent参数说明，单一表单最大组件个数不超过200。支持的控件类型如下： - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **NumberField**：数字输入框 - **DDSelectField**：单选框 - **DDMultiSelectField**：多选框 - **DDDateField**：日期控件 - **DDDateRangeField**：时间区间控件 - **TextNote**：文字说明控件 - 
- FormComponent (FormComponent, required): 表单控件，支持的控件请参考FormComponent参数说明，单一表单最大组件个数不超过200。
- optional: processCode(String), description(String), processFeatureConfig(Object), features(Array), pcUrl(String), mobileUrl(String), runType(String), callback(Object), appUuid(String), apiKey(String), version(String), templateConfig(Object), hidden(Boolean), createInstanceMobileUrl(String), createInstancePcUrl(String), templateEditUrl(String), disableSendCard(Boolean)

## Returns
- optional: result(Object), processCode(String)

## Limits
- 表单控件列表，详情请参考FormComponent参数说明，单一表单最大组件个数不超过200。支持的控件类型如下： - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **NumberField**：数字输入框 - **DDSelectField**：单选框 - **DDMultiSelectField**：多选框 - **DDDateField**：日期控件 - **DDDateRangeField**：时间区间控件 - **
- 表单控件，支持的控件请参考FormComponent参数说明，单一表单最大组件个数不超过200。
- - 每个企业最多创建流程中心200个模板，超过最大数量后调用接口会报错。

source_url: https://open.dingtalk.com/document/development/api-premiumsaveintegratedprocess
updated_at: 2026-06-03 10:12:59
