# 根据processCode分页获取审批流程数据

doc_id: CRVp7xBqB2
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/processes/pages/instances
api_version: v2-new
app_types: 企业内部应用
permissions: Premium.Workflow.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，企业内部应用可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- maxResults (Long, required): 分页参数，每页大小，最多传20。
- startTimeInMills (Long, required): 审批实例开始时间，Unix时间戳，单位毫秒。 - 例如，获取审批单发起时间在2020.4.10-2020.4.14之间，该值传2020.4.10 00:00:00对应的时间戳1586448000000。 - 针对OA高级版用户，**startTime**时间距当前时间不能超过5年，即最多可支持查询5年内的实例数据。 - 如果只传入**startTime**参数，要求时间距离当前时间不能超过120天，即一次查询最多只能查询120天的数据。
- processCode (String, required): 模板ID。 - 通过调用创建或更新审批表单模板接口获取。 - 通过OA审批概述-名词解释获取。
- optional: nextToken(String), endTimeInMills(Long), appUuid(String)

## Body
- none

## Returns
- optional: result(Object), nextToken(String), hasMore(Boolean), maxResults(Long), list(Array), processInstanceId(String), mainProcessInstanceId(String), finishTime(Long), finishTimeInMills(Long), attachedProcessInstanceIds(String), businessId(String), title(String), originatorDeptId(String), createTime(Long), createTimeInMills(Long), originatorUserid(String), status(String), formComponentValues(Array), name(String), id(String), value(String), extValue(String), operationRecords(Array), timestamp(Long), operationType(String), userId(String), remark(String), attachments(Array), fileName(String), fileSize(String), fileId(String), fileType(String), tasks(Array), createTimestamp(Long), finishTimestamp(Long), taskId(Long), activityId(String)

## Limits
- 分页参数，每页大小，最多传20。
- 审批实例开始时间，Unix时间戳，单位毫秒。 - 例如，获取审批单发起时间在2020.4.10-2020.4.14之间，该值传2020.4.10 00:00:00对应的时间戳1586448000000。 - 针对OA高级版用户，**startTime**时间距当前时间不能超过5年，即最多可支持查询5年内的实例数据。 - 如果只传入**startTime**参数，要求时间距离当前时间不能超过120天，即一次查询最多只能查询120天的数据。
- - 当前接口针对OA高级版客户可支持查询最多5年内的实例数据（即startTime时间距当前时间不能超过5年）。
- - 如果只传入**startTime**参数，要求时间距离当前时间不能超过120天（即一次查询最多只能查询120天的数据），**endTime**不传则默认取当前时间。
- - 如果传入**startTime**参数和**endTime**参数，要求时间范围不能超过120天，同时**startTime**时间距当前时间不能超过5年（即最多可支持查询5年内的实例数据）。
- - 批量获取的实例ID个数（循环获取），最多不能超过10000个，建议分多次获取。

source_url: https://open.dingtalk.com/document/development/api-premiumgetprocessinstances
updated_at: 2026-06-03 10:12:49
