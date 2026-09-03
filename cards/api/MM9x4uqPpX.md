# 家庭Feed同步

doc_id: MM9x4uqPpX
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/feed/sync
api_version: v1-oapi
app_types: 第三方企业应用
permissions: qyapi_edu_feed

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取第三方企业的access_token接口获取。

## Body
- feed_medias (IndustrySyncFeedMediaReq[], required): 媒体list，最多可传入999。
- media_url (String, required): 媒体链接。
- fee_type (Number, required): 同步类型。 - **1**：全量同步 - **2**：单个同步
- optional: media_type(Number), thumbnail_url(String), media_uid(String), dept_id(Number), album_id(String), send_uid(String), op_userId(String), send_time(Number), future(String)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String)

## Limits
- 媒体list，最多可传入999。

source_url: https://open.dingtalk.com/document/development/dingtalk-education-family-feed-synchronization
updated_at: 2026-06-08 09:47:56
