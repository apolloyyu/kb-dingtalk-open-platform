# 删除公告

doc_id: jkWUFTslgi
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/blackboard/delete
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
- blackboard_id (String, required): 公告ID，可以通过获取公告ID列表接口获取result参数值。
- operation_userid (String, required): 操作人userId，必须是公告管理员。

## Returns
- optional: result(Boolean), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-announcements-based-on-the-announcement-id
updated_at: 2026-05-27 17:06:32
