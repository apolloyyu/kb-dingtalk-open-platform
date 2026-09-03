# 钉工牌通知消息

doc_id: oNh5Q8FhiJ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/badge/notices
api_version: v2-new
app_types: 第三方企业应用
permissions: Badge.Common.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证。 - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 用户userId。
- msgId (String, required): 消息传入，调用方传入，唯一标识消息。
- msgType (String, required): 消息类型，取值： - **DING_BADGE_NOTIFY**：钉工牌通知场景
- content (String, required): 通知内容。 钉工牌场景必传字段： - **title**：标题 - **subTitle**：备注 - **imageUrl**：图片地址 - **url**：跳转地址 示例： ``` { "title":"标题", "subTitle":"备注", "imageUrl":"ds7868av787Url", "url":"ds7868av787Url" } ```

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/dingtalk-badge-notification-message
updated_at: 2026-06-04 19:11:54
