# 授权下载审批钉盘文件

doc_id: dR8ed9ouC2
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/processInstances/spaces/files/authDownload
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
- userId (String, required): 授权的用户userId。
- fileInfos (Array, required): 授权的钉盘文件信息列表。支持批量授权，最大列表长度为10。
- fileId (String, required): 文件fileId，调用获取单个审批实例详情接口获取`fileId`参数值。 文件id是审批组件中上传的fileId。
- spaceId (Long, required): 审批钉盘空间spaceId，可调用获取审批钉盘空间信息接口获取`spaceId`参数值。

## Returns
- optional: success(Boolean), result(Boolean)

## Limits
- 授权的钉盘文件信息列表。支持批量授权，最大列表长度为10。

source_url: https://open.dingtalk.com/document/development/download-the-approval-nail-file
updated_at: 2026-06-03 10:12:32
