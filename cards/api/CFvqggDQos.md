# 获取申请单详情

doc_id: CFvqggDQos
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/apply/get
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
- rq (OpenSearchRq, required): 请求对象，包含用于查询申请单的标识信息。
- corpid (String, required): 企业的corpid，用于标识所属企业。
- optional: thirdpart_apply_id(String), apply_id(Number), apply_show_id(String)

## Returns
- optional: module(OpenApplyRs), id(Number), apply_show_id(String), gmt_create(Date), gmt_modified(Date), thirdpart_id(String), corpid(String), corp_name(String), userid(String), user_name(String), deptid(String), trip_day(Number), dept_name(String), trip_cause(String), trip_title(String), status(Number), status_desc(String), itinerary_list(OpenItineraryInfo[]), trip_way(Number), itinerary_id(String), traffic_type(Number), dep_city(String), arr_city(String), dep_date(Date), cost_center_name(String), arr_date(Date), invoice_name(String), project_title(String), project_code(String), traveler_list(OpenUserInfo[]), approver_list(OpenApproverInfo[]), order(Number), note(String), operate_time(Date), errmsg(String), errcode(Number), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-detailed-data-of-a-single-request
updated_at: 2026-06-03 09:58:28
