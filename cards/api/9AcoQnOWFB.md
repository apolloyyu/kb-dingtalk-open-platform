# 获取服务表现数据

doc_id: 9AcoQnOWFB
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/dvi/service/quality-inspections
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.Sale.Service.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- recordId (String, required): 服务记录ID，可通过分页获取企业下的服务记录信息接口获取。

## Body
- none

## Returns
- optional: result(Object), score(Integer), summary(String), groupList(Array), name(String), itemList(Array), flowName(String), isHit(String), reason(String), script(String), highlights(String), citations(Array), content(String), time(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getservicequalityinspection
updated_at: 2026-08-06 09:39:08
