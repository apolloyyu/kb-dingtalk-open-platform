# 管理员查询指定员工的待处理任务列表

doc_id: iGvGnFyrnC
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/tasks/todoTasks
api_version: v2-new
app_types: 企业内部应用
permissions: Premium.Workflow.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- nextToken (Integer, required): 分页标识，从1开始。
- maxResults (Integer, required): 分页大小，最大值20。
- actionerUserId (String, required): 操作人userId。
- managerUserId (String, required): 管理员userId。

## Body
- none

## Returns
- optional: result(Object), hasMore(Boolean), list(Array), taskId(Long), processCode(String), title(String), businessId(String), processInstanceId(String), userId(String), canRedirect(Boolean), createTime(Long)

## Limits
- 分页大小，最大值20。

source_url: https://open.dingtalk.com/document/development/api-premiumquerytodotasksbymanager
updated_at: 2026-06-03 10:12:56
