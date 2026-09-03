# 获取服务对话章节摘要

doc_id: y9l0bkqDlu
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/dvi/service/chapters/summary
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
- optional: nextToken(String), totalCount(Integer), result(Array), name(String), content(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getservicechaptersummary
updated_at: 2026-06-24 13:44:37
