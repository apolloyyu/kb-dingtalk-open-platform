# 删除成本中心

doc_id: RfT6ww2Pr8
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/delete
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_ali_business_trip_write

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- rq (OpenCostCenterDeleteRq, required): 请求对象，封装删除所需参数。
- optional: thirdpart_id(String), corpid(String)

## Returns
- optional: errmsg(String), errcode(Number), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-cost-center
updated_at: 2026-06-08 09:47:06
