# 获取商旅访问地址

doc_id: rwmpVbNl1g
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/address/get
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_ali_business_trip

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- corpid (String, required): 企业的corpid。
- userid (String, required): 用户userid。
- type (Number, required): 类目类型： - 1：机票 - 2：火车票 - 3：酒店 - 4：用车
- action_type (Number, required): 操作类型： - 1：预订 - 2：我的订单列表 - 3：商旅管理后台，如果需要获取该场景的地址，只需提供corpid，userid - 4：商旅h5主页
- optional: request(OpenApiJumpInfoRq), itinerary_id(String), phone(String)

## Returns
- optional: success(Boolean), result(OpenApiJumpInfoRs), url(String), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-business-travel-access-addresses
updated_at: 2026-06-08 09:47:20
