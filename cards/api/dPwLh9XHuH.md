# 查询直播信息

doc_id: dPwLh9XHuH
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/live/lives
api_version: v2-new
app_types: 第三方企业应用
permissions: Live.Common.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- liveId (String, required): 直播ID，可调用创建直播接口获取liveId参数值。
- unionId (String, required): 操作者的unionId，可调用查询用户详情接口获取unionid参数值。

## Body
- none

## Returns
- optional: result(Object), liveInfo(Object), liveId(String), unionId(String), title(String), coverUrl(String), startTime(Long), endTime(Long), introduction(String), liveStatus(Integer), duration(Long), subscribeCount(Integer), uv(Integer), livePlayUrl(String), playbackDuration(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-the-live-streaming-information
updated_at: 2026-06-02 09:10:44
