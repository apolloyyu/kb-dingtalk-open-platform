# 更新实例状态

doc_id: DejXpndOhg
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/workflow/processCentres/instances
api_version: v2-new
app_types: 第三方企业应用
permissions: Workflow.Instance.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- processInstanceId (String, required): 审批实例ID，调用创建实例接口获取`processInstanceId`参数值。
- status (String, required): 实例状态。 - **COMPLETED**：结束审批流 - **TERMINATED**：终止审批流
- result (String, required): 实例结果： - 实例状态是COMPLETED，必须设置代表以下含义。 - **agree**：同意 - **refuse**：拒绝 - 实例状态为**TERMINATED**，必须设置代表含义，result取值agree和refuse均代表撤销审批流。
- userId (String, required): 抄送人userId，可通过获取部门用户userid列表接口获取。
- optional: notifiers(Array)

## Returns
- optional: success(Boolean)

## Limits
- 抄送人userId列表，最大值30。

source_url: https://open.dingtalk.com/document/development/update-instance-status
updated_at: 2026-06-03 10:12:39
