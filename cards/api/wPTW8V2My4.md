# 获取工作通知消息的发送进度

doc_id: wPTW8V2My4
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/message/corpconversation/getsendprogress
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
- task_id (Number, required): 发送消息时钉钉返回的任务ID，调用发送工作通知接口获取task_id参数值。 **[!NOTE]** 仅支持查询24小时内的任务。

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), progress(AsyncSendProgress), progress_in_percent(Number), status(Number)

## Limits
- 发送消息时钉钉返回的任务ID，调用发送工作通知接口获取task_id参数值。 **[!NOTE]** 仅支持查询24小时内的任务。
- 调用本接口，只能获取7天内工作通知消息的发送进度。

source_url: https://open.dingtalk.com/document/development/obtain-the-sending-progress-of-asynchronous-sending-of-enterprise-session
updated_at: 2026-07-13 09:45:38
