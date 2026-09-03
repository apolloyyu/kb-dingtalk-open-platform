# 查询服务号详情

doc_id: y4xC0Wsk6g
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/serviceaccount/get
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_service_account_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- unionid (String, required): 服务号的unionid，可通过查询服务号列表接口获取。

## Returns
- optional: request_id(String), errmsg(String), errcode(Number), service_account(ServiceAccountDTO), status(String), unionid(String), name(String), brief(String), desc(String), avatar_media_id(String), operator_user_id_list(String[]), black_user_id_list(String[]), allow_send_to_all(Boolean), allow_send_user_id_list(String[]), allow_send_dept_id_list(Number[])

## Limits
- 机器人管理列表中的简介，最多60个字符。
- 机器人主页中的服务号功能简介，最多200个字符。

source_url: https://open.dingtalk.com/document/development/inquire-about-service-number-details
updated_at: 2026-06-01 09:15:29
