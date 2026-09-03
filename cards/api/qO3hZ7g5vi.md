# 查询员工已获得的组织荣誉

doc_id: qO3hZ7g5vi
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/orgCulture/honors/users/{userId}
api_version: v2-new
app_types: 第三方企业应用
permissions: OrgCulture.Honor.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 员工的userId。

## Query params
- nextToken (String, required): 分页游标值。 - 如果是首次查询，该参数传0。 - 如果是非首次查询，该参数传上次查询时返回的nextToken。
- optional: maxResults(Integer)

## Body
- none

## Returns
- optional: success(Boolean), result(Object), nextToken(String), honors(Array), grantHistory(Array), senderUserid(String), grantTime(Long), honorId(String), honorName(String), honorDesc(String), expirationTime(Long)

## Limits
- 每页返回的最大条目数，默认20， 最大100。
- 荣誉有效期截止时间戳，单位毫秒。 - 如果未返回该字段，代表永久有效。 - 如果该字段有值，代表有有效截止时间戳。

source_url: https://open.dingtalk.com/document/development/check-the-honors-that-an-employee-has-received
updated_at: 2026-06-04 19:10:40
