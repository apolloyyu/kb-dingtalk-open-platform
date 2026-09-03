# 获取企业视频直播统计数据

doc_id: d2BDDoDaIZ
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/kac/datav/videolive/get
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- param_video_live_summary_request (VideoLiveSummaryRequest, required): 请求参数对象。
- data_id (String, required): 日期标识。

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(VideoLiveSummaryResponse), live_launch_succ5min_cnt(Number), live_launch_succ_cnt(Number), live_play_cnt(Number), live_play_user_cnt(Number), live_succ_time_len(String), max_user_cnt(Number), watch_group_live_user_cnt(Number)

## Limits
- 成功发起5分钟直播次数。
- 观看人数最多直播的观看人数。
- > 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的数据资产类OpenAPI接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过钉钉数据资产平台获取相应的数据服务。

source_url: https://open.dingtalk.com/document/development/query-live-streaming-statistics
updated_at: 2026-08-27 14:08:15
