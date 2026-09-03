# 获取推送失败的事件列表

doc_id: IWvcsmVAaV
completeness: full
archived: false
method: GET
endpoint: https://oapi.dingtalk.com/call_back/get_call_back_failed_result
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方应用授权企业的access_token接口获取。

## Body
- none

## Returns
- optional: failed_list(Failed[]), call_back_tag(String), event_time(Number), bpms_instance_change(Json), errcode(Number), errmsg(String), has_more(Boolean), corpid(String), bpmsCallBackData(callbackData)

## Limits
- 推送失败的事件列表，一次最多200个。
- 例如：事件第一次推送失败后，经过10秒，进行第一次重试，直至第 2 次重试失败后，可在3～5分钟内通过本接口获取推送失败的事件列表。

source_url: https://open.dingtalk.com/document/development/obtain-the-event-list-of-failed-push-messages
updated_at: 2026-05-08 17:50:33
