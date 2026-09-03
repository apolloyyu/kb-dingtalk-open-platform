# 查询计件报工数据

doc_id: AbzyyyJBWS
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/manufacturing/users/jobs/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Manufacture.JobBook.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: productName(String), pageSize(Integer), qualifiedQuantity(String), manufactureDay(String), instNo(String), userName(String), productCode(String), productSpecification(String), unitPrice(String), uuid(String), currentPage(Integer), userId(String), mesAppKey(String)

## Returns
- optional: httpCode(String), content(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/riqing-monthly-settlement-query-interface-for-piece-rate-reporting
updated_at: 2026-06-04 19:11:19
