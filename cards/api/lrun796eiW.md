# 查询单条服务记录

doc_id: lrun796eiW
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/dvi/service-record
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.Sale.Service.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- id (String, required): 服务记录ID，可通过分页获取企业下的服务记录信息接口获取。

## Body
- none

## Returns
- optional: result(Object), recordId(String), user(Object), name(String), userId(String), deviceSn(String), startTimestamp(Long), endTimestamp(Long), duration(String), customerId(String), team(Object), code(String), valid(Boolean), outBizData(String), qualityInspectionScore(Integer), sceneInfo(Object)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getservicerecord
updated_at: 2026-07-20 09:22:20
