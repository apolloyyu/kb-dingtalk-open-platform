# 查询ASR转写结果

doc_id: WDfu3TWxLL
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/dvi/asr/transcriptions
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.Audio.Analysis.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- taskId (String, required): ASR离线转写任务ID，通过创建ASR离线转写任务接口返回。
- optional: maxResults(Integer), nextToken(String)

## Body
- none

## Returns
- optional: result(Object), taskId(String), bizKey(String), taskStatus(String), resultInfo(Object), paragraphList(Array), speakerId(String), startTime(Long), endTime(Long), paragraph(String), nextToken(String)

## Limits
- 返回的数据条数，最大50。

source_url: https://open.dingtalk.com/document/development/api-getasrtranscription
updated_at: 2026-06-03 09:33:03
