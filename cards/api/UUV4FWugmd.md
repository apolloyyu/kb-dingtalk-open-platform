# 查询审批中心用户待处理任务列表

doc_id: UUV4FWugmd
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/processCentres/todoTasks
api_version: v2-new
app_types: 企业内部应用
permissions: Premium.Workflow.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- userId (String, required): OA审批任务执行人的用户userId。
- pageSize (Integer, required): 分页大小，从1开始，最大值20。
- pageNumber (Integer, required): 页码，从1开始, 最大限制10。
- optional: createBefore(String)

## Body
- none

## Returns
- optional: result(Object), list(Array), taskId(String), processInstanceId(String), status(String), processCreateTime(String), processEndTime(String), originatorName(String), originatorId(String), originatorPhoto(String), formMassage(String), url(String), title(String), processType(Integer), activityId(String), appType(Integer), success(Boolean), hasMore(Boolean)

## Limits
- 分页大小，从1开始，最大值20。
- 页码，从1开始, 最大限制10。

source_url: https://open.dingtalk.com/document/development/api-premiumgettodotasks
updated_at: 2026-06-03 10:12:53
