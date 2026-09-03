# 删除模板

doc_id: Zaxj7b8xmW
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/workflow/processCentres/schemas
api_version: v2-new
app_types: 第三方企业应用
permissions: Workflow.Form.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- processCode (String, required): 模板code。 - 企业内部应用，通过调用获取模板code接口获取。
- optional: cleanRunningTask(Boolean)

## Body
- none

## Returns
- optional: result(Object), processCode(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/self-owned-approval-deletion-template
updated_at: 2026-06-03 10:12:37
