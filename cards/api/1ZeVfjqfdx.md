# 获取培训观看数据

doc_id: 1ZeVfjqfdx
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/planetom/feeds/watchdata/get
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- chat_id (String, required): 直播绑定的群列表ID。 - 小程序通过选择会话方法获取。 - 微应用通过根据corpid选择会话方法获取。
- feed_id (String, required): 课程ID，调用创建培训课程接口返回的课程ID。
- anchor_id (String, required): 主播在组织内的userid。
- optional: page_size(Number), index(Number)

## Returns
- optional: result(OpenFeedWatchDetailRspModel), viewer_watch_details(OpenFeedWatchDetailModel[]), play_record_duration(Number), play_live_duration(Number), userid(String), has_finish(Number), success(Boolean), errcode(Number), errmsg(String)

## Limits
- 分页起始位置，不传默认获取前10个。

source_url: https://open.dingtalk.com/document/development/obtains-the-playback-data-of-a-live-stream
updated_at: 2026-08-27 12:32:14
