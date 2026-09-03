# 获取企业职务列表

doc_id: WXTBvHIiX3
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/hrm/jobs
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_hrm_read_user

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- nextToken (Integer, required): 分页游标。 - 首次调用，该参数传0。 - 非首次调用，该参数传上次调用本接口返回的nextToken。
- maxResults (Integer, required): 每页最大条目数，最大值100。
- optional: jobName(String)

## Body
- none

## Returns
- optional: nextToken(Long), hasMore(Boolean), list(Array), jobId(String), jobName(String), jobDescription(String)

## Limits
- 每页最大条目数，最大值100。

source_url: https://open.dingtalk.com/document/development/obtain-enterprise-title-information
updated_at: 2026-07-14 09:22:32
