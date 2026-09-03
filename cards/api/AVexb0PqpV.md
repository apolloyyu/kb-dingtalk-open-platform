# 分页获取企业下的服务记录信息

doc_id: AVexb0PqpV
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/dvi/service-records
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.Sale.Service.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: maxResults(Integer), nextToken(String), endTime(Long), startTime(Long), userId(String), teamCode(String), customerId(String)

## Body
- none

## Returns
- optional: nextToken(String), totalCount(Integer), result(Array), recordId(String), user(Object), name(String), userId(String), deviceSn(String), startTimestamp(Long), endTimestamp(Long), duration(String), customerId(String), team(Object), code(String), valid(Boolean), outBizData(String), qualityInspectionScore(Integer), sceneInfo(Object)

## Limits
- 每页返回的数据量，最多20条。

source_url: https://open.dingtalk.com/document/development/api-listservicerecord
updated_at: 2026-07-15 17:03:04
