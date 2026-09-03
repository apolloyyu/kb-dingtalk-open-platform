# 获取公告分类列表

doc_id: WIp5wUmkUZ
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/blackboard/category/list
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_blackboard_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- operation_userid (String, required): 操作人userId，必须是公告管理员。

## Returns
- optional: result(BlackboardCategoryVo[]), id(String), name(String), success(Boolean), errcode(Number), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-list-of-categories-not-deleted-for-enterprise-announcements
updated_at: 2026-05-29 09:13:33
