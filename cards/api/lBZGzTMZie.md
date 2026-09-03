# 批量获取表单模板schema（包含表单和流程配置信息）

doc_id: lBZGzTMZie
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/processes/schemas/batchQuery
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
- processCodes (Array of String, required): 模板code。

## Returns
- optional: result(Array), processCode(String), formUuid(String), bizCategoryId(String), processId(Long), appUuid(String), name(String), memo(String), icon(String), status(String), creatorUserId(String), modifierUserId(String), createTime(Long), modifyTime(Long), schemaContent(String), processConfig(String), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-premiumqueryschemaandprocessbycodelist
updated_at: 2026-06-03 10:12:42
