# 创建并投放 AI 卡片

doc_id: 49U7yLEq0J
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/card/ai/instances/createAndDeliver
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: AICard.Instance.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- outTrackId (String, required): 应用和企业范围内的业务卡片标识，非空，长度限制与普通卡片一致。
- openSpaceId (String, required): 仅一个 `im_group` 或 `im_robot` 目标，不支持分号分隔多个目标。
- robotCode (String, required): 机器人 code，群聊必填。
- flowStatus (String, required): 卡片流状态，使用枚举名，不使用内部数字码。
- a2uiMessages (Array of String, required): A2UI JSON 字符串列表，必填且非空，按顺序执行。 **[!NOTE]** 最多 100 条，总计不超过 256 KiB（UTF-8），由服务端校验。
- surfaceId (String, required): Surface 标识。
- componentId (String, required): 组件标识。
- type (String, required): 标注类型，目前仅 `artifact`。
- optional: userId(String), userIdType(Integer), imGroupOpenSpaceModel(Object), supportForward(Boolean), lastMessageI18n(Map<String, String>), searchSupport(Object), searchIcon(String), searchTypeName(String), searchDesc(String), notification(Object), alertContent(String), notificationOff(Boolean), imRobotOpenSpaceModel(Object), imGroupOpenDeliverModel(Object), atUserIds(Map<String, String>), recipients(Array of String), extension(Map<String, String>), imRobotOpenDeliverModel(Object), protocolVersion(String), a2uiAnnotations(Array), summary(String), callbackType(String), callbackRouteKey(String), bizContext(Map<String, String>), cardAtUserIds(Array of String), atAll(Boolean)

## Returns
- optional: success(Boolean), result(Object), outTrackId(String), deliverResults(Array), spaceType(String), spaceId(String), carrierId(String), errorMsg(String)

## Limits
- 消息 @ 人：用户 ID 到展示名，最多 100 项。 **[!NOTE]** JSON 总大小不超过 16 KiB（UTF-8），由服务端校验。
- 指定接收者 staffId，最多 100 个，始终按 staffId 解释。
- 消息 Extension，最多 64 项。 **[!NOTE]** JSON 总大小不超过 16 KiB（UTF-8），沿用普通消息扩展授权规则。
- A2UI JSON 字符串列表，必填且非空，按顺序执行。 **[!NOTE]** 最多 100 条，总计不超过 256 KiB（UTF-8），由服务端校验。
- 组件语义标注，最多 100 项，不传或空列表表示不新增标注。
- 降级摘要纯文本，编码为 `fallbackText.summary`。 **[!NOTE]** 开放层不额外校验非空和2048字节限制。
- 创建后不可变的回调业务关联信息，最多 32 项。 **[!NOTE]** JSON 总计 4096 字节（UTF-8）；key 禁用 `__`、`sys.`、`dingtalk.` 前缀。

source_url: https://open.dingtalk.com/document/development/api-createanddeliveraicard
updated_at: 2026-10-26 09:07:38
