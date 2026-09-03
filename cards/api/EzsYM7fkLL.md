# 获取审批实例ID列表

doc_id: EzsYM7fkLL
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/processes/instanceIds/query
api_version: v2-new
app_types: 企业内部应用
permissions: Workflow.Instance.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- processCode (String, required): 审批流的唯一码。 - 调用创建或更新审批表单模板接口获取`processCode`参数值。 - 通过名词解释-processCode获取。
- startTime (Long, required): 审批实例开始时间，Unix时间戳，单位毫秒。 例如，获取审批单发起时间在2020.4.10-2020.4.14之间，该值传2020.4.10 00:00:00对应的时间戳1586448000000。
- nextToken (Long, required): 分页游标。 - 如果是首次调用，该参数传0。 - 如果是非首次调用，该参数传上次调用时返回的nextToken。
- maxResults (Long, required): 分页参数，每页大小，最多传20。
- optional: endTime(Long), userIds(Array of String), statuses(Array of String)

## Returns
- optional: result(Object), list(Array of String), nextToken(String), success(Boolean)

## Limits
- 分页参数，每页大小，最多传20。
- 发起人userId列表，最大列表长度为10，可通过获取部门用户userid列表接口获取。
- 当前接口针对OA高级版客户可支持查询最多5年内的实例数据（即startTime时间距当前时间不能超过5年），升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景，查看全部专享OpenAPI。
- - 如果只传入**startTime**参数，要求时间距离当前时间不能超过120天，**endTime**不传则默认取当前时间。
- - 如果传入**startTime**参数和**endTime**参数，要求时间范围不能超过120天，同时**startTime**时间距当前时间不能超过365天。
- - 批量获取的实例ID个数（循环获取），最多不能超过10000个。

source_url: https://open.dingtalk.com/document/development/obtain-an-approval-list-of-instance-ids
updated_at: 2026-06-03 10:12:29
