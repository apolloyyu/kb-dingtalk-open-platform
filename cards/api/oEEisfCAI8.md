# 获取模板code

doc_id: oEEisfCAI8
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/processCentres/schemaNames/processCodes
api_version: v2-new
app_types: 第三方企业应用
permissions: Workflow.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- name (String, required): 模板名称，最大长度64字符，可通过创建或更新审批模版接口入参字段表单模板名称`name`字段获取。

## Body
- none

## Returns
- optional: result(Object), processCode(String), gmtModified(String)

## Limits
- 模板名称，最大长度64字符，可通过创建或更新审批模版接口入参字段表单模板名称`name`字段获取。

source_url: https://open.dingtalk.com/document/development/obtain-the-template-code
updated_at: 2026-06-02 15:41:20
