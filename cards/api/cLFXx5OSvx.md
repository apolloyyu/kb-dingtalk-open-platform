# 创建并开启互动卡片吊顶

doc_id: cLFXx5OSvx
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/im/topBoxes
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
- cardTemplateId (String, required): 互动卡片的消息模板ID，调用创建并投放卡片接口获取模板ID。
- outTrackId (String, required): 一张卡片的外部ID，最大长度64，与创建卡片/创建并投放卡片中的 outTrackId 保持一致。也可在对应模板的**卡片实例管理**中获取： image - 需保存`outTrackId`，否则无法进行关闭互动卡片吊顶。 - 一般情况下，若使用了新的 cardTemplateId 或 cardData 等参数，则需要重新生成全新的 outTrackId，否则更改不会生效。
- cardData (Object, required): 卡片数据。
- conversationType (Integer, required): 会话类型： - **1**：群聊 - **2**：单聊助手
- optional: callbackRouteKey(String), cardParamMap(Map<String, String>), userIdPrivateDataMap(Map<String, Object>), unionIdPrivateDataMap(Map<String, Object>), cardSettings(Object), pullStrategy(Boolean), openConversationId(String), userId(String), unionId(String), robotCode(String), coolAppCode(String), groupTemplateId(String), receiverUserIdList(Array of String), receiverUnionIdList(Array of String), expiredTime(Long), platforms(String)

## Returns
- optional: success(Boolean)

## Limits
- 一张卡片的外部ID，最大长度64，与创建卡片/创建并投放卡片中的 outTrackId 保持一致。也可在对应模板的**卡片实例管理**中获取： image - 需保存`outTrackId`，否则无法进行关闭互动卡片吊顶。 - 一般情况下，若使用了新的 cardTemplateId 或 cardData 等参数，则需要重新生成全新的 outTrackId，否则更改不会生效。
- 吊顶可见者userId，最多100个，可通过获取部门用户userid列表或查询用户详情接口获取。 - 群聊： - 若不传入`receiverUserIdList`和`receiverUnionIdList`，则默认吊顶对会话内所有人可见。 - 传入参数`receiverUserIdList`或`receiverUnionIdList`，则吊顶仅对对应用户可见。 - 单聊助手：不需要传入此参数。
- 吊顶可见者unionId，最多100个，可通过查询用户详情接口获取。 群聊： - 若不传入receiverUserIdList和receiverUnionIdList，则默认吊顶对会话内所有人可见。 - 传入参数receiverUserIdList或receiverUnionIdList，则吊顶仅对对应用户可见。 单聊助手：不需要传入此参数。
- - 单个会话中最多可开启10个吊顶。若会话内已经存在10个未关闭的吊顶，需要关闭已开启的吊顶，然后再开启新的吊顶。

source_url: https://open.dingtalk.com/document/development/send-group-helper-message
updated_at: 2026-07-14 09:29:43
