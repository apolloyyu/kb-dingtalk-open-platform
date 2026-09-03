# 获取工作通知消息的发送结果

doc_id: uUgjebUmeZ
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/message/corpconversation/getsendresult
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
- optional: send_result(AsyncSendResult), invalid_user_id_list(String[]), forbidden_user_id_list(String[]), failed_user_id_list(String[]), read_user_id_list(String[]), unread_user_id_list(String[]), invalid_dept_id_list(Number[]), forbidden_list(SendForbiddenModel[]), code(String), count(Number), userid(String), errcode(Number), errmsg(String), request_id(String)

## Limits
- 发送消息时钉钉返回的任务ID，调用发送工作通知接口获取task_id参数值。 **[!NOTE]** 仅支持查询24小时内的任务。
- 因发送消息过于频繁或超量而被流控过滤后实际未发送的userId。 未被限流的接收者仍会被成功发送。 限流规则包括： - 给同一用户发相同内容消息一天仅允许一次。 - 同一个应用给同一个用户发送消息： - 如果是第三方企业接入方式，给同一用户发消息一天不得超过100次。 - 如果是企业接入方式，此上限为500。
- 流控code。 - 143105表示企业自建应用每日推送给用户的消息超过上限。 - 143106表示企业自建应用推送给用户的消息重复。
- > - 调用本接口，只能获取24小时内工作通知消息的发送结果。
- > - 当接收人列表超过100人时，不支持调用本接口，否则系统会返回**调用超时**。

source_url: https://open.dingtalk.com/document/development/gets-the-result-of-sending-messages-asynchronously-to-the-enterprise
updated_at: 2026-07-13 09:45:39
