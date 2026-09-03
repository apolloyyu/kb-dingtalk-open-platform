# 获取推送失败的事件列表

doc_id: yD3p7TGT2j
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/call_back/get_call_back_failed_result
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- none

## Returns
- optional: failed_list(Failed[]), call_back_tag(String), event_time(Number), bpms_instance_change(Json), errcode(Number), errmsg(String), has_more(Boolean), corpid(String), bpmsCallBackData(callbackData)

## Limits
- 推送失败的事件列表，一次最多200个。

source_url: https://open.dingtalk.com/document/development/list-of-events-where-historical-push-notifications-failed
updated_at: 2026-09-02 18:13:39
