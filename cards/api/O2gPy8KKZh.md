# 创建并投放卡片

doc_id: O2gPy8KKZh
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/card/instances/createAndDeliver
api_version: v2-new
app_types: 第三方企业应用
permissions: Card.Instance.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- cardTemplateId (String, required): 卡片内容模板ID，可通过登录开发者后台 > 卡片平台获取。 image
- outTrackId (String, required): 外部卡片实例Id。 - 开发者自己生成并作为入参传递给钉钉的，钉钉只在对应使用到 outTrackId 的场景，帮助开发者对TrackId进行记录 - 一个 outTrackId 唯一标识一张卡片，如果需要使用新的 cardTemplateId 或 cardData 等参数创建一张新的卡片，需要设置全新的 outTrackId，否则更改不会生效。
- cardData (Object, required): 卡片数据，示例： ``` "cardData": { "cardParamMap": { "intParam": "1", // 整数类型属性 "floatParam": "1.2.3", // 浮点类型属性 "trueParam": "true", // 布尔类型属性，对应 TRUE "falseParam": "false" // 布尔类型属性，对应 FALSE } } ```
- openSpaceId (String, required): 表示场域及其场域id，其格式为`dtv1.card//spaceType1.spaceId1;spaceType2.spaceId2_1;spaceType2.spaceId2_2;spaceType3.spaceId3`。
- optional: userId(String), callbackType(String), callbackRouteKey(String), cardParamMap(Map<String, String>), privateData(Map<String, Object>), openDynamicDataConfig(Object), dynamicDataSourceConfigs(Array), dynamicDataSourceId(String), constParams(Map<String, String>), pullConfig(Object), pullStrategy(String), interval(Integer), timeUnit(String), imSingleOpenSpaceModel(Object), supportForward(Boolean), lastMessageI18n(Map<String, String>), searchSupport(Object), searchIcon(String), searchTypeName(String), searchDesc(String), notification(Object), alertContent(String), notificationOff(Boolean), imGroupOpenSpaceModel(Object), imRobotOpenSpaceModel(Object), coFeedOpenSpaceModel(Object), title(String), coolAppCode(String), topOpenSpaceModel(Object), spaceType(String), imSingleOpenDeliverModel(Object), atUserIds(Map<String, String>), extension(Map<String, String>), imGroupOpenDeliverModel(Object), robotCode(String), recipients(Array of String), imRobotOpenDeliverModel(Object), topOpenDeliverModel(Object), expiredTimeMillis(Long), userIds(Array of String), platforms(Array of String), coFeedOpenDeliverModel(Object), bizTag(String), gmtTimeLine(Long), docOpenDeliverModel(Object), userIdType(Integer), cardAtUserIds(Array of String)

## Returns
- optional: success(Boolean), result(Object), outTrackId(String), deliverResults(Array), spaceType(String), spaceId(String), carrierId(String), errorMsg(String)

## Limits
- 卡片模板内容替换参数： - key：参数名（最长不超过100B） - value: 参数值（最长不超过1KB） - 属性字段只支持 String 类型，非 String 类型的属性填写请参考文档：API 卡片数据的填写说明。 - 务必确保属性值的类型与卡片搭建器中所配置的变量类型相匹配，否则可能出现属性不生效，或者在移动端无法显示等问题。
- 用户的私有数据： - key：用户userId信息（最长不超过100B） - value：用户私有数据（最长不超过1KB） 示例： ``` "privateData": { "manager1234": { "cardParamMap": { "attendee": "小明、小王", "image1": "mediaIdXXXXX1" } } } ```
- 供消息展示与搜索的字段。 - 最大限制200个字符，超过存储截断200。
- 通知内容。 若不填写则使用默认文案：如你收到1条新消息。

source_url: https://open.dingtalk.com/document/development/create-and-deliver-cards
updated_at: 2026-07-14 09:22:14
