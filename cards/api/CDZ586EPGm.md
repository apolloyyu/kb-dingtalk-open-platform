# 创建或更新审批模板

doc_id: CDZ586EPGm
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/processCentres/schemas
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
- formComponents (Array, required): 表单控件列表，支持的控件列表如下，单一表单最大组件个数不超过200。 支持的控件类型，详情请参考本文**FormComponent参数补充说明**。 - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **NumberField**：数字输入框 - **DDSelectField**：单选框 - **DDMultiSelectField**：多选框 - **DDDateField**：日期控件 - **DDDateRangeField**：时间区间控件 - **Tex
- FormComponent (FormComponent, required): 表单控件，支持的控件参考FormComponent参数说明，单一表单最大组件个数不超过200。
- optional: processCode(String), description(String), processFeatureConfig(Object), features(Array), pcUrl(String), mobileUrl(String), runType(String), callback(Object), appUuid(String), apiKey(String), version(String), config(String), templateConfig(Object), hidden(Boolean), createInstanceMobileUrl(String), createInstancePcUrl(String), templateEditUrl(String), disableSendCard(Boolean)

## Returns
- optional: result(Object), processCode(String)

## Limits
- 表单模板名称，最大长度200字符。
- 表单模板描述，最大长度300字符。
- 表单控件列表，支持的控件列表如下，单一表单最大组件个数不超过200。 支持的控件类型，详情请参考本文**FormComponent参数补充说明**。 - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **NumberField**：数字输入框 - **DDSelectField**：单选框 - **DDMultiSelectField**：多选框 - **DDDateField**：日期控件 - **DDDateRangeFi
- 表单控件，支持的控件参考FormComponent参数说明，单一表单最大组件个数不超过200。
- 三方自定义的pc端跳转链接，最大长度1024字符。
- 三方自定义的手机端跳转链接，最大长度1024字符。
- 表单创建移动端地址，最大长度1024字符。
- 表单创建PC端地址，最大长度1024字符。

source_url: https://open.dingtalk.com/document/development/create-orupdate-the-approval-template-new
updated_at: 2026-06-03 10:12:36
