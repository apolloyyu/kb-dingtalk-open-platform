# 根据听记ID获取A1音频文件信息

doc_id: 9L6rHiVdWY
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/dvi/audios/minutes
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.Device.Audio.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- minutesId (String, required): 听记ID，可通过获取音频文件信息接口获取。

## Body
- none

## Returns
- optional: result(Object), fileId(String), fileName(String), creatorUserId(String), createTime(Long), duration(Long), fileSize(Long), attributes(Map)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-queryfileinfobyminutesid
updated_at: 2026-08-06 15:50:53
