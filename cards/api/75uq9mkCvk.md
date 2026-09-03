# 查询群消息已读人员列表

doc_id: 75uq9mkCvk
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/chat/getReadList
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，可通过获取企业内部应用的access_token接口获取。
- messageId (String, required): 发送消息到企业群接口返回的加密消息id。 **[!IMPORTANT]** 消息id中包含url特殊字符时需要encode后再使用。
- cursor (Number, required): 分页查询的游标，第一次可以传0，后续传返回结果中的next_cursor的值。 当返回结果中，没有next_cursor时，表示没有后续的数据了，可以结束调用。
- size (Number, required): 分页查询的大小，最大可以传100，且不能超过群的总人数。

## Body
- none

## Returns
- optional: errcode(Number), errmsg(String), next_cursor(Number), readUserIdList(String[])

## Limits
- 分页查询的大小，最大可以传100，且不能超过群的总人数。

source_url: https://open.dingtalk.com/document/development/queries-the-list-of-people-who-have-read-a-group
updated_at: 2026-08-25 09:37:20
