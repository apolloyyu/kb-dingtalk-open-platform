# 获取用户待审批数量

doc_id: qXRYtE7dlo
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/processes/todoTasks/numbers
api_version: v2-new
app_types: 企业内部应用
permissions: Workflow.Instance.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- userId (String, required): 要查询的用户userId。

## Body
- none

## Returns
- optional: result(Integer)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-the-number-of-requests-to-be-approved-by-users
updated_at: 2026-06-03 10:12:35
