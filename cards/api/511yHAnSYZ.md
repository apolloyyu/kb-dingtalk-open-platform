# 获取审批钉盘空间信息

doc_id: 511yHAnSYZ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/processInstances/spaces/infos/query
api_version: v2-new
app_types: 企业内部应用
permissions: Workflow.Instance.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可通过获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 用户的userId。
- optional: agentId(Long)

## Returns
- optional: result(Object), spaceId(Long), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-information-about-approval-nail-disk
updated_at: 2026-06-03 10:12:30
