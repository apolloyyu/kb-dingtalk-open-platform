# 更新工作通知状态栏

doc_id: pqDHKIzFIJ
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/message/corpconversation/status_bar/update
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- agent_id (Number, required): 发送消息时使用的微应用的AgentID。 - 企业内部应用，可在开发者后台的应用详情页面查看。image - 第三方企业应用可调用获取企业授权信息接口获取。
- task_id (Number, required): 工作通知任务ID，调用发送工作通知接口获取task_id参数值。
- status_value (String, required): 状态栏值。
- optional: status_bg(String)

## Returns
- optional: request_id(String), errmsg(String), errcode(Number)

## Limits
- - 调用本接口，只能更新7天内发出的工作通知状态栏。

source_url: https://open.dingtalk.com/document/development/update-work-notification-status-bar
updated_at: 2026-07-13 09:43:54
