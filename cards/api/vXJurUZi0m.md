# 使用模板发送工作通知消息

doc_id: vXJurUZi0m
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/message/corpconversation/sendbytemplate
api_version: v1-oapi
app_types: 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取第三方企业的access_token接口获取。

## Body
- agent_id (Number, required): 应用的agentid，可调用获取企业授权信息接口获取。
- template_id (String, required): 消息模板ID。 在开发者后台应用的**开发管理**页面查看。
- optional: userid_list(String), dept_id_list(String), data(String)

## Returns
- optional: errmsg(String), errcode(Number), task_id(Number), request_id(String)

## Limits
- 接收者的用户userId列表。最大列表长度为5000。
- 接收者的部门id列表。最大列表长度为500。 **[!IMPORTANT]** **dept_id_list**和**userid_list**不能同时为空。
- - 单次发送人数最大1000。
- - 每分钟接收人数最大5000。
- - 给同一员工，每天只能发送一条内容相同的消息。
- - 每天给每个员工最多可发送100条。

source_url: https://open.dingtalk.com/document/development/work-notification-templating-send-notification-interface
updated_at: 2026-07-13 09:45:40
