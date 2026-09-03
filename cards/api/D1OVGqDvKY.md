# 删除业务分组

doc_id: D1OVGqDvKY
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/processCentres/directories
api_version: v2-new
app_types: 第三方企业应用
permissions: Premium.Workflow.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- dirId (String, required): 分组ID。
- operateUserId (String, required): 操作人userId。

## Body
- none

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-premiumdeldir
updated_at: 2026-06-03 10:12:58
