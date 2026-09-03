# 退回审批任务

doc_id: lQWeKp0T9Q
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/tasks/revert
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
- taskId (Long, required): 审批任务ID，可调用获取单个审批实例详情接口获取。
- processInstanceId (String, required): 审批实例ID： - 调用发起审批实例接口获取`InstanceId`参数值。 - 调用获取审批实例ID列表接口获取`list`参数值。
- operateUserId (String, required): 操作人的用户ID，需要跟任务的当前执行人保持一致，否则无法通过校验。
- targetActivityId (String, required): 退回到的节点ID。 - 可调用获取审批单流程中的节点信息接口获取审批单流程中的节点ID信息`activityId`参数值。 - 若退回方式为`REVERT_FOR_RESUBMIT` 退回到发起人，则targetActivityId固定传发起节点的ID值：`sid-startevent`
- revertAction (String, required): 退回方式： - **REVERT_FOR_APPROVAL**：退回到审批人 - **REVERT_FOR_RESUBMIT**：退回到发起人
- optional: remark(String)

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-premiumreverttask
updated_at: 2026-06-03 10:12:44
