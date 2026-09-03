# 授权下载审批钉盘文件

doc_id: iAoDjlJr0o
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/processInstances/spaces/files/authDownload
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
- userId (String, required): 授权的用户userid，支持离职人员。
- fileInfos (Array, required): 授权的钉盘文件信息列表。支持批量授权，最大列表长度：10。
- fileId (String, required): 文件fileId，可调用获取单个审批实例详情接口获取。 文件id是审批组件或审批评论中上传的fileId。
- spaceId (Long, required): 审批钉盘空间spaceId，可调用获取审批钉盘空间信息接口获取`spaceId`参数值。

## Returns
- optional: success(Boolean), result(Boolean)

## Limits
- 授权的钉盘文件信息列表。支持批量授权，最大列表长度：10。

source_url: https://open.dingtalk.com/document/development/api-premiumaddapprovedentryauth
updated_at: 2026-06-03 10:12:52
