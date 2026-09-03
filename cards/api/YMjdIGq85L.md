# 创建公告

doc_id: YMjdIGq85L
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/blackboard/create
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
- create_request (OapiCreateBlackboardVo, required): 请求对象。
- operation_userid (String, required): 操作人的userId，必须是公告管理员。
- blackboard_receiver (BlackboardReceiverOpenVo, required): 公告接收人。
- title (String, required): 公告标题。
- content (String, required): 公告内容。
- optional: author(String), private_level(Number), ding(Boolean), deptid_list(Number[]), userid_list(String[]), push_top(Boolean), category_id(String), coverpic_mediaid(String)

## Returns
- optional: result(Boolean), success(Boolean), errcode(Number), request_id(String)

## Limits
- 接收部门ID列表，最大的列表长度为20。 **[!NOTE]** 如果传-1，代表根部门，会给组织全员发送公告。
- 接收人userId列表，最大的列表长度为1000。

source_url: https://open.dingtalk.com/document/development/create-an-enterprise-announcement
updated_at: 2026-07-14 09:21:48
