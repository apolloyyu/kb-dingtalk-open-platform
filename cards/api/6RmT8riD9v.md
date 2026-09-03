# 获取企业机票订单数据

doc_id: 6RmT8riD9v
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/flight/order/search
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
- rq (Object, required): 请求对象，封装所有查询条件。
- corpid (String, required): 企业id。
- optional: start_time(String), apply_id(Number), page(Number), userid(String), page_size(Number), deptid(String), end_time(String), update_end_time(String), update_start_time(String), all_apply(Boolean), thirdpart_apply_id(String)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), flight_order_list(Object[]), id(Number), gmt_modified(String), userid(String), corp_name(String), corpid(String), gmt_create(String), user_name(String), deptid(String), dept_name(String), apply_id(String), contact_name(String), dep_city(String), arr_city(String), dep_date(String), ret_date(String), trip_type(Number), passenger_count(Number), cabin_class(String), status(Number), discount(String), flight_no(String), passenger_name(String), dep_airport(String), arr_airport(String), invoice(Object), title(String), cost_center(Object), number(String), name(String), price_info_list(Object[]), price(String), type(Number), category(String), pay_type(Number), tradeId(String), ticket_no(String), original_ticket_no(String), changeFlightNo(String), startTime(String), endTime(String), person_price(String), insureInfo_list(Object[]), insure_no(String), thirdpart_itinerary_id(String), user_affiliate_list(Object[]), thirdpart_apply_id(String), btrip_title(String), project_id(Number), project_code(String), project_title(String), third_part_project_id(String), page_info(Object), page(Number), page_size(Number), total_number(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-enterprise-ticket-order-data
updated_at: 2026-06-08 09:47:15
