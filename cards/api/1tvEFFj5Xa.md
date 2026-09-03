# 获取申请单列表

doc_id: 1tvEFFj5Xa
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/apply/search
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
- optional: gmt_modified(Date), page_size(Number), end_time(Date), start_time(Date), page(Number), userid(String), deptid(String), all_apply(Boolean), only_shang_lv_apply(Boolean)

## Returns
- optional: module(OpenApplyRs[]), id(Number), apply_show_id(String), gmt_create(Date), gmt_modified(Date), thirdpart_id(String), corpid(String), userid(String), deptid(String), corp_name(String), user_name(String), dept_name(String), trip_day(Number), trip_cause(String), trip_title(String), status(Number), status_desc(String), itinerary_list(OpenItineraryInfo[]), trip_way(Number), itinerary_id(String), traffic_type(Number), dep_city(String), arr_city(String), cost_center_name(String), invoice_name(String), dep_date(Date), arr_date(Date), project_code(String), project_title(String), traveler_list(OpenUserInfo[]), approver_list(OpenApproverInfo[]), order(Number), note(String), operate_time(Date), flow_code(String), errmsg(String), errcode(Number), success(Boolean)

## Limits
- 每页返回数量，默认10，最多50。

source_url: https://open.dingtalk.com/document/development/search-enterprise-approval-form-data
updated_at: 2026-06-08 09:47:13
