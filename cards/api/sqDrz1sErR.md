# 更新公告

doc_id: sqDrz1sErR
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/blackboard/update
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_blackboard_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- update_request (OapiUpdateBlackboardVo, required): 请求对象。
- blackboard_id (String, required): 公告ID。
- title (String, required): 公告标题。
- content (String, required): 公告内容。
- operation_userid (String, required): 操作人userid，必须是公告管理员。
- optional: author(String), ding(Boolean), category_id(String), notify(Boolean), coverpic_mediaid(String)

## Returns
- optional: result(Boolean), success(Boolean), errcode(Number), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/modify-the-announcement-according-to-the-announcement-id
updated_at: 2026-05-27 17:06:33
