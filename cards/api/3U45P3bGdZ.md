# 修改直播属性信息

doc_id: 3U45P3bGdZ
completeness: full
archived: false
method: PUT
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
- liveId (String, required): 直播ID，可调用创建直播接口liveId参数值。
- unionId (String, required): 主播的unionId，可调用查询用户详情接口获取unionid参数值。
- optional: title(String), introduction(String), coverUrl(String), preStartTime(Long), preEndTime(Long)

## Returns
- optional: result(Object), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/modify-live-streaming
updated_at: 2026-06-02 09:10:43
