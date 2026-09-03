# 获取候选人的面试信息

doc_id: HwlNtBXeui
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/ats/interviews/query
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_recruitment_plugin

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: bizCode(String), nextToken(String), size(Long)

## Body
- startTimeBeginMillis (Long, required): 面试开始的结束时间，单位毫秒。 面试开始时间和面试结束时间跨度最大不能超过30天。
- startTimeEndMillis (Long, required): 面试开始的结束时间，单位毫秒。 面试开始时间和面试结束时间跨度最大不能超过30天。
- candidateId (String, required): 候选人标识，可调用根据手机号获取候选人信息接口获取。

## Returns
- optional: totalCount(Long), hasMore(Boolean), nextToken(String), list(Array), interviewId(String), jobId(String), startTimeMillis(Long), endTimeMillis(Long), cancelled(Boolean), creatorUserId(String), interviewers(Array), userId(String)

## Limits
- 每页条目数，最大值200。
- 面试开始的结束时间，单位毫秒。 面试开始时间和面试结束时间跨度最大不能超过30天。

source_url: https://open.dingtalk.com/document/development/query-the-interview-list
updated_at: 2026-06-04 19:10:33
