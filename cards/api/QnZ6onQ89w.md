# 创建ASR离线转写任务

doc_id: QnZ6onQ89w
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/dvi/asr/transcriptions
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.Audio.Analysis.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- url (String, required): 音频文件URL，要求可以无身份信息访问。
- optional: bizKey(String), phrases(Array of String)

## Returns
- optional: result(Object), taskId(String)

## Limits
- 热词，不超过10个字符。

source_url: https://open.dingtalk.com/document/development/api-createasrtranscription
updated_at: 2026-06-03 09:33:02
