# 下载审批附件

doc_id: rnliDjlvrU
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/processInstances/spaces/files/urls/download
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
- fileId (String, required): 文件fileId，可调用获取单个审批实例详情接口获取 文件id是审批组件中上传的fileId（如下图所示），评论中上传的附件fileId也支持获取下载链接。
- optional: withCommentAttatchment(Boolean)

## Returns
- optional: result(Object), spaceId(Long), fileId(String), downloadUri(String), success(Boolean)

## Limits
- 文件下载地址。 文件下载地址有效期15分钟。

source_url: https://open.dingtalk.com/document/development/api-premiumgrantprocessinstancefordownloadfile
updated_at: 2026-06-03 10:12:52
