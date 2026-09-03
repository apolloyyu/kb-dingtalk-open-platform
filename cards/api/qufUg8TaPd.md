# 获取审批表单控件字段操作权限

doc_id: qufUg8TaPd
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/processes/fields/settings/query
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
- processInstanceId (String, required): 审批实例ID： - 调用发起审批实例接口获取`InstanceId`参数值。 - 调用获取审批实例ID列表接口获取`list`参数值。
- userId (String, required): 当前审批人userId。

## Returns
- optional: result(Array), fieldId(String), fieldBehavior(String), componentType(String), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-premiumgetinstfieldsetting
updated_at: 2026-06-03 10:12:46
