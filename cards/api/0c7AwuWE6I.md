# 批量获取关注服务窗用户信息

doc_id: 0c7AwuWE6I
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/link/followers
api_version: v2-new
app_types: 企业内部应用
permissions: OfficialAccount.Contact.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: nextToken(String), maxResults(Integer), accountId(String)

## Body
- none

## Returns
- optional: requestId(String), result(Object), nextToken(String), userList(Array), userId(String), name(String), timestamp(Long)

## Limits
- 每页最大条目数，最大值100。

source_url: https://open.dingtalk.com/document/development/obtains-the-follower-information-from-the-service-window
updated_at: 2026-06-03 17:51:19
