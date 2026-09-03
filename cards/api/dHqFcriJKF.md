# 关闭吊顶卡片

doc_id: dHqFcriJKF
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/card/tops/close
api_version: v2-new
app_types: 第三方企业应用
permissions: Card.Instance.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- outTrackId (String, required): 外部卡片实例Id，与创建卡片/创建并投放卡片中的 outTrackId 保持一致。也可在对应模板的**卡片实例管理**中获取： image 由开发者自己生成并作为入参传递给钉钉的，钉钉只在对应使用到outTrackId的场景，帮助开发者对TrackId进行记录。
- openConversationId (String, required): 会话 id： - **群聊**（此参数必传）： - 基于群模板创建的群，调用创建场景群接口获取`open_conversation_id`参数值。 - 安装群聊酷应用的群，通过感知群变化（事件订阅）获取回调参数`OpenConversationId`参数值。 - **单聊助手**：不传入此参数。

## Body
- none

## Returns
- optional: success(Boolean), result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-closetopcard
updated_at: 2026-07-14 09:22:15
