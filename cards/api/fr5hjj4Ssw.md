# 获取培训课程的基本信息

doc_id: fr5hjj4Ssw
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/planetom/feeds/statistic/get
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
- feed_id (String, required): 课程ID，可通过创建培训课程接口获取。
- anchor_id (String, required): 主播在对应组织的userid。

## Returns
- optional: result(OpenFeedInfoModel), status(Number), introduction(String), title(String), cover_url(String), feed_id(String), feed_type(Number), start_time(Date), anchor_id(String), chat_ids(String[]), sub_status(Number), jump_url(String), end_time(Date), has_play_back(Boolean), replay_url(String), edit_replay_url(String), duration(Number), success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-basic-information-about-the-course
updated_at: 2026-08-27 12:32:16
