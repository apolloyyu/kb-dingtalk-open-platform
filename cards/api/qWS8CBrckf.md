# 撤回工作通知消息

doc_id: qWS8CBrckf
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/message/corpconversation/recall
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
- msg_task_id (Number, required): 发送消息时钉钉返回的任务ID，调用发送工作通知接口获取task_id参数值。 **[!NOTE]** 仅支持撤回24小时内的工作消息通知。

## Returns
- optional: errmsg(String), errcode(Number)

## Limits
- 发送消息时钉钉返回的任务ID，调用发送工作通知接口获取task_id参数值。 **[!NOTE]** 仅支持撤回24小时内的工作消息通知。

source_url: https://open.dingtalk.com/document/development/notification-of-work-withdrawal
updated_at: 2026-07-14 09:22:12
