# 获取用车订单数据

doc_id: 0OK1r47iEE
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/vehicle/order/search
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
- rq (OpenSearchRq, required): 请求对象。
- corpid (String, required): 企业的corpid。
- optional: start_time(Date), update_end_time(Date), apply_id(Number), page(Number), userid(String), page_size(Number), deptid(String), end_time(Date), update_start_time(Date), all_apply(Boolean), thirdpart_apply_id(String)

## Returns
- optional: errcode(Number), errmsg(String), success(Boolean), vehicle_order_list(OpenVehicleOrderRs[]), id(Number), gmt_create(Date), gmt_modified(Date), passenger_name(String), corpid(String), corp_name(String), user_name(String), userid(String), dept_name(String), deptid(String), apply_show_id(String), apply_id(Number), real_from_city_name(String), real_to_city_name(String), from_address(String), to_address(String), from_city_name(String), to_city_name(String), memo(String), order_status(Number), car_level(String), car_info(String), estimate_price(String), publish_time(Date), taken_time(Date), driver_confirm_time(Date), cancel_time(Date), travel_distance(String), pay_time(Date), service_type(Number), business_category(String), cost_center_id(Number), cost_center_number(String), cost_center_name(String), invoice_id(Number), invoice_title(String), project_code(String), project_title(String), price_info_list(OpenPriceInfo[]), price(String), type(Number), category(String), pay_type(Number), thirdpart_itinerary_id(String), user_affiliate_list(OpenUserAffiliateDo[]), user_confirm(Number), provider(Number), real_from_address(String), real_to_address(String), thirdpart_apply_id(String), btrip_title(String)

## Limits
- 每页数量，默认10，最大50。

source_url: https://open.dingtalk.com/document/development/vehicle-order-query-interface
updated_at: 2026-06-08 09:47:19
