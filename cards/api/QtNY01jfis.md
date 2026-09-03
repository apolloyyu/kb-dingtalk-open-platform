# 关闭互动卡片吊顶

doc_id: QtNY01jfis
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/im/topBoxes/close
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_chat_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- outTrackId (String, required): 卡片的外部ID，最大长度64，与创建卡片/创建并投放卡片中的 outTrackId 保持一致。也可在对应模板的**卡片实例管理**中获取： image
- conversationType (Integer, required): 会话类型： - **1**：群聊 - **2**：单聊助手
- optional: openConversationId(String), userId(String), unoinId(String), robotCode(String), coolAppCode(String), groupTemplateId(String)

## Returns
- optional: success(Boolean)

## Limits
- 卡片的外部ID，最大长度64，与创建卡片/创建并投放卡片中的 outTrackId 保持一致。也可在对应模板的**卡片实例管理**中获取： image

source_url: https://open.dingtalk.com/document/development/close-interactive-card-ceiling
updated_at: 2026-07-14 09:29:44
