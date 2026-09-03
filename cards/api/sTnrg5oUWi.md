# 同意或拒绝审批任务

doc_id: sTnrg5oUWi
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/processInstances/execute
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
- processInstanceId (String, required): 审批实例ID： - 调用发起审批实例接口获取`InstanceId`参数值。 - 调用调用获取审批实例ID列表接口获取`list`参数值。
- result (String, required): 审批操作，取值： - **agree**：同意 - **refuse**：拒绝
- actionerUserId (String, required): 操作人userId，可通过调用获取单个审批实例详情接口获取`userId`参数值。
- taskId (Long, required): 任务ID，可通过调用获取单个审批实例详情接口获取`taskId`参数值。
- optional: remark(String), file(Object), photos(Array of String), attachments(Array), spaceId(String), fileSize(String), fileId(String), fileName(String), fileType(String)

## Returns
- optional: result(Boolean), success(Boolean)

## Limits
- 审批意见，最大长度1024字符，可为空。
- 图片URL地址，最大长度：1024字符。
- 附件列表，最多元素个数：20。
- 文件ID，最大长度：256字符。 请参见本文接口调用说明。
- 文件名称，最大长度：256字符。 请参见本文接口调用说明。

source_url: https://open.dingtalk.com/document/development/approve-or-reject-the-approval-task
updated_at: 2026-06-03 10:12:33
