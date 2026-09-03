# 新增或者更新卡片的场域信息

doc_id: lFCU7AkePM
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/card/instances/spaces
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
- outTrackId (String, required): 外部卡片实例Id。 由开发者自己生成并作为入参传递给钉钉的，钉钉只在对应使用到outTrackId的场景，帮助开发者对TrackId进行记录。
- optional: imGroupOpenSpaceModel(Object), supportForward(Boolean), lastMessageI18n(Map<String, String>), searchSupport(Object), searchIcon(String), searchTypeName(String), searchDesc(String), notification(Object), alertContent(String), notificationOff(Boolean), imRobotOpenSpaceModel(Object), topOpenSpaceModel(Object), spaceType(String), coFeedOpenSpaceModel(Object), title(String)

## Returns
- optional: success(Boolean), result(Boolean)

## Limits
- 供消息展示与搜索的字段。 最大限制200个字符，超过存储截断200。
- 通知内容。 若不填写则使用默认文案：如你收到1条新消息

source_url: https://open.dingtalk.com/document/development/add-field-interface
updated_at: 2026-06-04 19:12:23
