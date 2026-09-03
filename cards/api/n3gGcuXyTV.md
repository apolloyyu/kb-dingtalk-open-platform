# 管理员批量转交指定员工的待处理任务

doc_id: n3gGcuXyTV
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/tasks/batchRedirect
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
- transfereeUserId (String, required): 原操作人 userId，支持在职人员和已离职人员。
- handoverUserId (String, required): 新处理人 userId（被转交人，仅支持在职人员）。
- managerUserId (String, required): 管理员userId。
- taskIds (Array of Long, required): 转交的任务Id，即taskId。

## Returns
- optional: result(Object), failCount(Long), totalCount(Long), redirectResults(Array), taskId(Long), success(Boolean), errorMsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-premiumredirecttasksbymanager
updated_at: 2026-06-03 10:12:57
