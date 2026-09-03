# 创建直播

doc_id: UkIjWpkYOL
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/live/lives
api_version: v2-new
app_types: 第三方企业应用
permissions: Live.Common.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- unionId (String, required): 发起直播的主播unionId，可调用查询用户详情接口获取unionid参数值。
- title (String, required): 直播标题。
- preStartTime (Long, required): 预计开播时间戳，单位毫秒。 **[!NOTE]** 该字段值需要大于当前的时间戳。
- preEndTime (Long, required): 预计结束时间戳，单位毫秒。 **[!NOTE]** 该字段值需要大于预计开播时间。
- optional: introduction(String), coverUrl(String), publicType(Long), enableLinkMic(Boolean), isLandscape(Boolean)

## Returns
- optional: result(Object), liveId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-live-streaming
updated_at: 2026-06-01 14:35:23
