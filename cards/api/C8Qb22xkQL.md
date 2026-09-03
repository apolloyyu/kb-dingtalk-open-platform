# 查询通过流程中心集成的OA审批任务

doc_id: C8Qb22xkQL
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/processCentres/todoTasks
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_aflow

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- userId (String, required): 任务执行人的用户userId，可通过获取部门用户userid列表接口获取。
- pageSize (Integer, required): 分页大小，从1开始，最大值40。
- pageNumber (Integer, required): 页码，从1开始。
- optional: createBefore(Long)

## Body
- none

## Returns
- optional: requestId(String), taskPage(Object), hasMore(Boolean), list(Array), taskId(Long), activityId(String), userId(String), status(String), result(String), createTime(Long), finishTime(String), processInstanceId(String)

## Limits
- 分页大小，从1开始，最大值40。
- - 本接口只能查询一年内的待办任务数据。

source_url: https://open.dingtalk.com/document/development/query-oa-approval-tasks-integrated-through-process-center
updated_at: 2026-06-03 10:12:40
