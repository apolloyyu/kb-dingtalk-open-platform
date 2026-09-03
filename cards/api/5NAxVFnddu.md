# 获取企业商旅酒店订单数据

doc_id: 5NAxVFnddu
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/hotel/order/search
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
- rq (OpenSearchRq, required): 请求对象，封装查询条件。
- corpid (String, required): 企业的corpid，用于唯一标识目标企业。
- optional: start_time(Date), apply_id(Number), page(Number), userid(String), page_size(Number), deptid(String), end_time(Date), update_end_time(Date), update_start_time(Date), all_apply(Boolean), thirdpart_apply_id(String)

## Returns
- optional: success(Boolean), errmsg(String), errcode(Number), module(OpenHotelOrderRs[]), id(Number), gmt_create(Date), gmt_modified(Date), corpid(String), corp_name(String), userid(String), user_name(String), deptid(String), dept_name(String), apply_id(Number), contact_name(String), city(String), hotel_name(String), check_in(Date), check_out(Date), room_type(String), room_num(Number), night(Number), guest(String), order_type_desc(String), order_status_desc(String), cost_center(OpenCostCenterDo), number(String), name(String), invoice(OpenInvoiceDo), title(String), price_info_list(OpenPriceInfo[]), price(String), type(Number), category(String), pay_type(Number), passenger_name(String), thirdpart_itinerary_id(String), order_status(Number), order_type(Number), user_affiliate_list(OpenUserAffiliateDo[]), thirdpart_apply_id(String), btrip_title(String)

## Limits
- 每页数量，默认10，最大50

source_url: https://open.dingtalk.com/document/development/enterprises-obtain-order-data-for-business-hotels
updated_at: 2026-06-08 09:47:16
