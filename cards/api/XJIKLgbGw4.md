# 查询群发消息列表

doc_id: XJIKLgbGw4
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/follow/message/queryMsgSendRecords
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_service_account_message

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- unionid (String, required): 服务号的unionid。
- page_number (Integer, required): 分页页码，从1开始。
- page_size (Integer, required): 分页大小。
- optional: start_time(Long), end_time(Long), status(Integer), msgTypeList(Array of String), msg_source(Integer)

## Returns
- optional: errorcode(String), errmsg(String), result(Object), total_count(Integer), item_count(Integer), items(Array), task_id(String), send_time(Long), create_time(Long), msg_type(String), title(String), operator_user_id(String), msg_source(Integer)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/service-account-query-msgsend-records
updated_at: 2026-06-02 19:12:39
