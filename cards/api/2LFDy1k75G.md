# 投放卡片

doc_id: 2LFDy1k75G
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/card/instances/deliver
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
- outTrackId (String, required): 外部卡片实例Id。 - 由开发者自己生成并作为入参传递给钉钉的，钉钉只在对应使用到outTrackId的场景，帮助开发者对TrackId进行记录。 - 一个 outTrackId 唯一标识一张卡片。
- openSpaceId (String, required): 表示场域及其场域id，其格式为`dtv1.card//spaceType1.spaceId1;spaceType2.spaceId2_1;spaceType2.spaceId2_2;spaceType3.spaceId3`。
- optional: imSingleOpenDeliverModel(Object), atUserIds(Map<String, String>), extension(Map<String, String>), imRobotOpenDeliverModel(Object), spaceType(String), robotCode(String), imGroupOpenDeliverModel(Object), recipients(Array of String), topOpenDeliverModel(Object), expiredTimeMillis(Long), userIds(Array of String), platforms(Array of String), coFeedOpenDeliverModel(Object), bizTag(String), gmtTimeLine(Long), docOpenDeliverModel(Object), userId(String), userIdType(Integer)

## Returns
- optional: success(Boolean), result(Array), spaceType(String), spaceId(String), carrierId(String), errorMsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delivery-card-interface
updated_at: 2026-06-04 19:12:21
