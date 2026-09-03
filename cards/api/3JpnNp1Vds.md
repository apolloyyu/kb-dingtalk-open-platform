# 获取企业火车票订单数据

doc_id: 3JpnNp1Vds
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/train/order/search
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
- optional: start_time(Date), apply_id(Number), page(Number), userid(String), page_size(Number), deptid(String), end_time(Date), update_end_time(Date), update_start_time(Date), all_apply(Boolean), thirdpart_apply_id(String)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), train_order_list(OpenTrainOrderRs[]), id(Number), gmt_create(Date), gmt_modified(Date), corpid(String), corp_name(String), userid(String), user_name(String), deptid(String), dept_name(String), apply_id(Number), contact_name(String), dep_station(String), arr_station(String), dep_time(Date), arr_time(Date), train_number(String), train_type(String), seat_type(String), run_time(String), ticket_no_12306(String), dep_city(String), arr_city(String), rider_name(String), ticket_count(Number), status(Number), invoice(OpenInvoiceDo), title(String), cost_center(OpenCostCenterDo), number(String), name(String), price_info_list(OpenPriceInfo[]), price(String), type(Number), category(String), pay_type(Number), passenger_name(String), thirdpart_itinerary_id(String), user_affiliate_list(OpenUserAffiliateDo[]), thirdpart_apply_id(String), btrip_title(String)

## Limits
- 每页返回数量，默认10，最大50。

source_url: https://open.dingtalk.com/document/development/obtains-the-enterprise-train-ticket-order-data
updated_at: 2026-06-08 09:47:17
