# 获取用户可见的企业应用列表

doc_id: 6c54nD3SkA
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/microApp/users/{userId}/apps
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_get_microapp_list

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- optional: userId(String)

## Query params
- none

## Body
- none

## Returns
- optional: appList(Array), agentId(Long), name(String), desc(String), icon(String), homepageLink(String), pcHomepageLink(String), ompLink(String), appId(Long), appStatus(Integer), developType(Integer), unifiedAppId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-list-of-enterprise-applications-visible-to-a-user
updated_at: 2026-06-03 11:49:37
