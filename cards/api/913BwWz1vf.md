# 卡片平台模板复制

doc_id: 913BwWz1vf
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/card/templates/copy
api_version: v2-new
app_types: 第三方企业应用
permissions: Card.Template.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，第三方企业应用通过获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- templateId (String, required): 模板id，可通过登录开发者后台 > 卡片平台获取。 image

## Returns
- optional: success(Boolean), data(Object), templateId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-copytemplate
updated_at: 2026-07-14 09:22:15
