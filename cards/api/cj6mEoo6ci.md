# 分页查询设备列表

doc_id: cj6mEoo6ci
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/dvi/devices
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.Device.Audio.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可通过获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: maxResults(Integer), nextToken(String), userId(String), teamCode(String), sn(String)

## Body
- none

## Returns
- optional: nextToken(String), totalCount(Integer), result(Array), sn(String), teamCode(String), userId(String), bindTimestamp(Long)

## Limits
- 每页返回的数据量，最多20条。

source_url: https://open.dingtalk.com/document/development/api-listdevice
updated_at: 2026-08-06 15:50:47
