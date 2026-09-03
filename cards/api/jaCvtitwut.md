# 商旅成本中心转换为外部成本中心

doc_id: jaCvtitwut
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/transfer
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
- rq (OpenCostCenterTransferRq, required): 请求对象。
- thirdpart_id (String, required): 第三方成本中心id。
- cost_center_id (Number, required): 商旅成本中心id。
- corpid (String, required): 企业的corpid。

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/business-travel-cost-center-converted-to-external-cost-center
updated_at: 2026-06-08 09:47:09
