# 转交OA审批任务

doc_id: jq1XaQ0vhT
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/tasks/redirect
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
- taskId (Long, required): OA审批任务ID，调用获取单个审批实例详情接口获取的taskId参数值。
- toUserId (String, required): OA审批任务被转交对象的用户userId。
- operateUserId (String, required): 操作人userId，需要跟任务的当前执行人保持一致，否则无法通过校验。
- optional: remark(String), actionName(String), file(Object), photos(Array of String), attachments(Array), spaceId(String), fileSize(String), fileId(String), fileName(String), fileType(String)

## Returns
- optional: result(Boolean)

## Limits
- 转交备注信息，最大长度：256字符。
- 操作节点名，最大长度：128字符。
- 图片URL地址，最大长度：1024字符。
- 附件列表，最多元素个数：20。
- 文件ID，最大长度：256字符。 请参见本文接口调用说明。
- 文件名称，最大长度：256字符。 请参见本文接口调用说明。

source_url: https://open.dingtalk.com/document/development/transfer-the-oa-approval-task
updated_at: 2026-06-03 10:12:34
