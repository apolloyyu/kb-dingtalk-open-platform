# 获取文件转写的概要信息

doc_id: 3NZ13zqrPO
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/dvi/transcripts/summary
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.Audio.Analysis.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可通过获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- fileId (String, required): 文件ID，通过分页查询指定设备的音频文件列表接口返回的文件ID。
- deviceType (String, required): 文件设备类型： - 针对A1类型时，需要传递A1。 - 针对B1电子工牌类型时，需要传递B1。

## Body
- none

## Returns
- optional: result(Object), content(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-gettranscriptsummary
updated_at: 2026-08-05 16:46:34
