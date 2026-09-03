# 查询审批中心用户已收到的实例列表

doc_id: cuJ0T3F4vB
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/processCentres/noticedInstances
api_version: v2-new
app_types: 企业内部应用
permissions: Premium.Workflow.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- userId (String, required): 实例抄送人的用户userId。
- pageSize (Integer, required): 分页大小，从1开始，最大值20。
- pageNumber (Integer, required): 页码，从1开始, 最大限制10。

## Body
- none

## Returns
- optional: result(Object), list(Array), processInstanceId(String), status(String), processCreateTime(String), processEndTime(String), originatorName(String), originatorId(String), originatorPhoto(String), formMassage(String), url(String), title(String), processType(Integer), hasMore(Boolean), success(Boolean)

## Limits
- 分页大小，从1开始，最大值20。
- 页码，从1开始, 最大限制10。

source_url: https://open.dingtalk.com/document/development/api-premiumgetnoticedinstances
updated_at: 2026-06-03 10:12:48
