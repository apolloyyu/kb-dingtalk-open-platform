# 授权预览审批附件

doc_id: 9ZLTIljbjq
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/processInstances/spaces/authPreview
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
- userId (String, required): 授权允许预览附件的用户userId。
- processInstanceId (String, required): 审批实例ID。 - 调用发起审批实例接口获取`InstanceId`参数值。 - 调用获取审批实例ID列表接口获取`list`参数值。
- fileId (String, required): 审批附件ID。 fileId必须与发起审批实例中附件组件中的文件fileId保持一致，否则出现无权限错误信息。
- optional: agentId(Long), fileIdList(Array of String), withCommentAttatchment(Boolean)

## Returns
- optional: result(Object), spaceId(Long), success(Boolean)

## Limits
- 附件ID列表，支持批量授权，最大列表长度为20。

source_url: https://open.dingtalk.com/document/development/official-authorized-preview-approval-attachment
updated_at: 2026-06-03 10:12:31
