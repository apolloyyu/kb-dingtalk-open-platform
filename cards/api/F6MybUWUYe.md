# 获取用户创建的填表模板列表

doc_id: F6MybUWUYe
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/swform/users/forms
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_swapp_collection_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- maxResults (Integer, required): 每页最大条目数，最大值200。
- nextToken (Long, required): 分页游标。 - 如果是首次查询，该参数传0。 - 如果是非首次查询，该参数传上次调用时返回的nextToken值。
- optional: bizType(Integer), creator(String)

## Body
- none

## Returns
- optional: success(Boolean), result(Object), hasMore(Boolean), nextToken(Long), list(Array), creator(String), formCode(String), name(String), memo(String), setting(Object), bizType(Integer), createTime(String), formType(Integer), stop(Boolean), loopTime(String), loopDays(Array of Integer), endTime(String)

## Limits
- 每页最大条目数，最大值200。

source_url: https://open.dingtalk.com/document/development/new-obtains-the-template-that-a-user-creates
updated_at: 2026-06-04 19:10:37
