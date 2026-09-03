# 更新流程表单审批实例

doc_id: Ll3Be3M2ZN
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/processInstances
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
- opUserId (String, required): 操作人userId，必须为管理员身份。
- variables (Array, required): 表单数据内容，控件列表，最大列表长度：150。
- id (String, required): 控件id。
- value (String, required): 控件值。
- processInstanceId (String, required): 流程实例ID。
- optional: processCode(String), bizAlias(String), extValue(String), remark(String)

## Returns
- optional: result(Boolean)

## Limits
- 表单数据内容，控件列表，最大列表长度：150。
- - 该接口支持对流程中和已完成的实例数据进行更新，仅限以管理员身份调用。

source_url: https://open.dingtalk.com/document/development/api-premiumupdateprocessinstancevariables
updated_at: 2026-06-03 10:12:45
