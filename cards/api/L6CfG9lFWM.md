# 获取关注服务窗用户信息

doc_id: L6CfG9lFWM
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/link/followers/infos
api_version: v2-new
app_types: 企业内部应用
permissions: OfficialAccount.Contact.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: userId(String), unionId(String), accountId(String)

## Body
- none

## Returns
- optional: requestId(String), result(Object), user(Object), userId(String), name(String), timestamp(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-the-follower-information-of-the-service-window
updated_at: 2026-06-05 15:36:42
