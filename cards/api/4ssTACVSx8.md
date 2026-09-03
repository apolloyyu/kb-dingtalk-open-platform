# 关联单号查询相关订单信息列表

doc_id: 4ssTACVSx8
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/alitrip/unionOrders
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_ali_business_trip

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- corpId (String, required): 第三方企业corpId。
- optional: thirdPartApplyId(String), unionNo(String)

## Body
- none

## Returns
- optional: flightList(Array), flightOrderId(Long), flightOrderStatus(Long), corpId(String), trainList(Array), trainOrderId(Long), trainOrderstatus(Long), hotelList(Array), hotelOrderId(Long), hotelOrderStatus(Long), vehicleList(Array), vehicleOrderId(Long), vehicleOrderStatus(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/related-order-information
updated_at: 2026-06-02 19:53:11
