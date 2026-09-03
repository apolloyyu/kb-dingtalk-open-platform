# 删除直播

doc_id: br1fA8j01z
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/live/lives
api_version: v2-new
app_types: 第三方企业应用
permissions: Live.Common.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- liveId (String, required): 直播ID，可调用创建直播接口获取liveId参数值。
- unionId (String, required): 用户unionId，可调用查询用户详情接口获取unionid参数值。

## Body
- none

## Returns
- optional: result(Object), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-live-streaming
updated_at: 2026-06-01 14:33:38
