# 获取审批钉盘空间信息

doc_id: zmtwIMbtVf
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/processInstances/spaces/infos/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Premium.Workflow.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 用户的userId，支持离职人员。
- optional: agentId(Long)

## Returns
- optional: result(Object), spaceId(Long), success(Boolean)

## Limits
- > - 本接口有授权上传权限的作用。每次调用上传附件API接口前，建议使用上传操作人userId再调用一次本接口。

source_url: https://open.dingtalk.com/document/development/api-premiumgetattachmentspace
updated_at: 2026-06-03 10:12:50
