# 获取视频直播观看人员列表

doc_id: 4Y0vREKU5h
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/kac/datav/videolive/viewer/list
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
- request (GroupLiveViewerReq, required): 请求对象。
- openConversationId (String, required): 群标识ID，可以通过获取视频直播明细列表获得。
- cursor (Number, required): 分页游标。首页请使用0，之后直接使用返回结果中的next_cursor。
- live_uuid (String, required): 直播uuid。
- size (Number, required): 分页大小，不超过500。

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(GroupLiveViewerPageResult), data(GroupLiveViewer[]), play_duration(Number), play_duration_min(String), play_record_duration(Number), play_record_duration_min(String), userid(String), has_more(Boolean), next_cursor(Number)

## Limits
- 分页大小，不超过500。
- > 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的数据资产类OpenAPI接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过钉钉数据资产平台获取相应的数据服务。

source_url: https://open.dingtalk.com/document/development/query-users-of-apsaravideo-live
updated_at: 2026-08-27 14:08:20
