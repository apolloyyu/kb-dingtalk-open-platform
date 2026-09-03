# 归档审批实例

doc_id: EGr8KincJu
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/processInstances/archive
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
- processInstanceId (String, required): 审批实例ID。 - 调用发起审批实例接口获取`InstanceId`参数值。 - 调用获取审批实例ID列表接口获取`list`参数值。
- opUserId (String, required): 操作人的userId。 需要传OA审批管理员的userId才能归档。

## Returns
- optional: result(Boolean), success(Boolean)

## Limits
- - 本接口只能归档已审批完成的审批实例，不能归档流程中的审批实例。归档后将不允许用户再次修改该审批实例。

source_url: https://open.dingtalk.com/document/development/api-archiveprocessinstance
updated_at: 2026-06-03 10:12:42
