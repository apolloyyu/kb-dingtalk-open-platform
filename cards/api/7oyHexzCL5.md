# 消息撤回

doc_id: 7oyHexzCL5
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/message/mass/recall
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_service_account_message

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- unionid (String, required): 服务号的unionid，可以通过查询服务号详情接口获取。
- task_id (String, required): 消息发送任务id，可以通过消息群发接口获取。

## Returns
- optional: errmsg(String), errcode(Number), request_id(String)

## Limits
- 调用本接口，根据消息发送的任务id撤回24小时内的消息。
- 发送超过24小时的消息，不支持通过本接口进行撤回。

source_url: https://open.dingtalk.com/document/development/service-number-message-withdrawal
updated_at: 2026-06-01 09:15:37
