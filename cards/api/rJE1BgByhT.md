# 获取jsapiTicket

doc_id: rJE1BgByhT
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/oauth2/jsapiTickets
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- optional: jsapiTicket(String), expireIn(Long)

## Limits
- 企业内部应用是以应用维度获取jsapi_ticket的，所以在使用的时候需要将jsapi_ticket以appKey为维度进行缓存下来（设置缓存过期时间2小时），并不需要每次都通过接口拉取。

source_url: https://open.dingtalk.com/document/development/create-a-jsapi-ticket
updated_at: 2026-04-29 22:27:42
