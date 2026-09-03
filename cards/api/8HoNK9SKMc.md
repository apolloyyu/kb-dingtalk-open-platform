# 清理OA审批数据

doc_id: 8HoNK9SKMc
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/processes/clean
api_version: v2-new
app_types: 第三方企业应用
permissions: Workflow.Data.Clean

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用本接口的访问凭证，通过调用获取第三方企业应用的suiteAccessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- processCode (String, required): 模板唯一码，通过创建或更新审批模板接口获取。
- corpId (String, required): 授权企业的corpId。

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/clear-oa-approval-data
updated_at: 2026-06-03 10:12:41
