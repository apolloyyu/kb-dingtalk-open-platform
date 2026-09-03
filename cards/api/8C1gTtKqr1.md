# 创建培训课程

doc_id: 8C1gTtKqr1
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/planetom/feeds/create
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
- appoint_begin_time (Number, required): 约定开播（未来时间），Unix时间戳，单位毫秒。
- feed_type (Number, required): 课程类型： - **0**：直播
- title (String, required): 课程标题。
- anchor_id (String, required): 主播在组织内的userId。
- open_app_id (Number, required): 开放平台中应用的appId，参考Unified App ID。
- optional: cover_url(String), pic_introduction_url(String), group_ids(String), introduction(String), group_id_type(Number), pre_video_url(String)

## Returns
- optional: result(String), success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-live-courses
updated_at: 2026-08-27 12:32:10
