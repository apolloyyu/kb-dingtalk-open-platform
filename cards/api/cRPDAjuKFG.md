# 撤销审批实例

doc_id: cRPDAjuKFG
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/processInstances/terminate
api_version: v2-new
app_types: 企业内部应用
permissions: Workflow.Instance.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- processInstanceId (String, required): 审批实例ID。 - 调用发起审批实例接口获取`InstanceId`参数值。 - 调用获取审批实例ID列表接口获取`list`参数值。
- optional: isSystem(Boolean), remark(String), operatingUserId(String)

## Returns
- optional: result(Boolean), success(Boolean)

## Limits
- 终止说明，最大长度1024字符。
- - 审批发起15秒内不能撤销审批流程。
- - 本接口只能撤销流程中的审批实例，不能撤销已审批完成的审批实例。

source_url: https://open.dingtalk.com/document/development/revoke-an-approval-instance
updated_at: 2026-06-03 10:12:27
