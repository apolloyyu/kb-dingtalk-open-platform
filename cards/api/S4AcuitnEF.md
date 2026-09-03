# 添加审批评论

doc_id: S4AcuitnEF
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/processInstances/comments
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
- processInstanceId (String, required): 审批实例ID： - 调用发起审批实例接口获取`InstanceId`参数值。 - 调用获取单个审批实例详情接口获取`list`参数值。
- text (String, required): 评论的内容，最大长度1024字符。
- commentUserId (String, required): 评论人的userId。
- optional: file(Object), photos(Array of String), attachments(Array), spaceId(String), fileSize(String), fileId(String), fileName(String), fileType(String)

## Returns
- optional: result(Boolean), success(Boolean)

## Limits
- 评论的内容，最大长度1024字符。
- 附件列表，最大列表元素个数：20。
- 文件ID，最大长度256字符。 请参见本文接口调用说明。
- 文件名称，最大长度256字符。 请参见本文接口调用说明。

source_url: https://open.dingtalk.com/document/development/official-approval-adds-approval-comments
updated_at: 2026-06-03 10:12:28
