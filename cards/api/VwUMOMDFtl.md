# 获取企业所有应用列表

doc_id: VwUMOMDFtl
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/microApp/allApps
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_get_microapp_list

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- optional: appList(Array), agentId(Long), name(String), desc(String), icon(String), homepageLink(String), pcHomepageLink(String), ompLink(String), appId(Long), appStatus(Integer), developType(Integer)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-a-list-of-all-enterprise-applications
updated_at: 2026-06-04 19:10:06
