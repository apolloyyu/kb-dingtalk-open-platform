# DING服务

doc_id: rQ0CAeBIdF
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/appDings/send
api_version: v2-new
app_types: 企业内部应用
permissions: Custom.Ding.Send

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userids (Array of String, required): 接收DING消息的用户userid列表。
- content (String, required): 消息内容。

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/send-in-application-ding
updated_at: 2026-06-04 19:09:57
