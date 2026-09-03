# ASR 一句话语音识别

doc_id: YstbF7DMD7
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/asr/voice/translate
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- media_id (String, required): 音频的mediaId，调用上传媒体文件接口获取media_id参数值。 **[!IMPORTANT]** 目前只接受 ogg 或 amr 格式的音频。

## Returns
- optional: errmsg(String), errcode(Number), result(String)

## Limits
- 调用本接口，可根据音频的media_id识别一段60秒内的语音。

source_url: https://open.dingtalk.com/document/development/asr-short-sentence-recognition
updated_at: 2026-08-27 14:14:50
