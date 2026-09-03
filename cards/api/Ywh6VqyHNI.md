# 获取用户服务窗关注状态

doc_id: Ywh6VqyHNI
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/link/followers/statuses
api_version: v2-new
app_types: 企业内部应用
permissions: OfficialAccount.Contact.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用本接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: userId(String), unionId(String), accountId(String)

## Body
- none

## Returns
- optional: result(Object), status(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-attention-status-of-the-user-service-window
updated_at: 2026-06-04 19:12:02
