# 分页查询指定设备的音频文件列表

doc_id: IFBE5Qb3Rr
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/dvi/device/audio/list
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.Device.Audio.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- deviceType (String, required): 设备类型： - 针对A1类型时，需要传递A1。 - 针对B1电子工牌类型时，需要传递B1。
- sn (String, required): 要查询设备的SN编号。
- optional: maxResults(Integer), nextToken(String), startTimestamp(Long), endTimestamp(Long)

## Returns
- optional: result(Array), fileId(String), fileName(String), creatorUserId(String), createTime(Long), duration(Long), fileSize(Long), attributes(Map), nextToken(String), totalCount(Long)

## Limits
- 下一页的查询token，10分钟内有效。

source_url: https://open.dingtalk.com/document/development/api-queryaudiofile
updated_at: 2026-08-06 15:50:55
