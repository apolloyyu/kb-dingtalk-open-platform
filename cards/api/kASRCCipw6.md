# 查询预估价

doc_id: kASRCCipw6
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/price/query
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
- req (OpenApiIntervalPriceRq, required): 请求对象，封装具体的查询条件。
- corpid (String, required): 企业的corpid，可登录开发者后台查看。
- from_where (String, required): 出发地点名称。
- userid (String, required): 发起请求的用户userid。
- start_time (Date, required): 出发时间，格式为`yyyy-MM-dd HH:mm:ss`。
- end_time (Date, required): 返程时间，格式为`yyyy-MM-dd HH:mm:ss`。
- to_where (String, required): 目的地名称。
- category (String, required): 类目： - **flight**：机票 - **hotel**：酒店 - **train**：火车
- optional: itinerary_id(String), query_key(String)

## Returns
- optional: result(Result), success(Boolean), module(Module), hotel_fee_detail(HotelFeeDetail[]), criterion(Number), city(String), traffic_fee(TrafficFee), btrip_routes(BtripRoutes[]), most_expensive(MostExpensive), vehicle_no(String), seat_grade(String), dep_time(String), fee(Number), arr_time(String), cheapest(Cheapest), dest_city(String), org_city(String), err_msg(String), dep_date(Date), query_key(String), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-estimated-price
updated_at: 2026-06-03 09:51:48
