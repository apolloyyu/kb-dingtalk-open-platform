# 查询当前企业下可颁发的荣誉列表

doc_id: 0TbFdQelVe
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/orgCulture/organizations/honors
api_version: v2-new
app_types: 第三方企业应用
permissions: OrgCulture.Honor.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- nextToken (String, required): 分页游标。 - 如果是首次调用，该参数传0。 - 如果是非首次调用，该参数传上次调用时接口返回的nextToken值。
- optional: maxResults(Integer)

## Body
- none

## Returns
- optional: success(Boolean), result(Object), nextToken(String), openHonors(Array), honorId(Long), honorImgUrl(String), honorPendantImgUrl(String), honorName(String), honorDesc(String)

## Limits
- 每页最大条目数，默认值20， 最大值100。

source_url: https://open.dingtalk.com/document/development/query-the-list-of-honors-that-can-be-issued-under
updated_at: 2026-06-04 19:10:40
