# 修改申请单

doc_id: Ze0qcrRObI
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/modify
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
- rq (OpenApiNewApplyRq, required): 请求参数对象，包含完整的申请单修改信息。
- corpid (String, required): 企业的corpid，标识目标企业身份。
- traveler_list (OpenUserInfo[], required): 出行人信息列表，用于指定本次出差的人员详情。
- userid (String, required): 申请人的userid，用于唯一标识操作用户。
- trip_cause (String, required): 出差事由。
- itinerary_list (OpenItineraryInfo[], required): 行程列表。
- arr_date (Date, required): 到达日期。
- dep_date (Date, required): 出发日期。
- invoice_id (Number, required): 发票ID。
- arr_city (String, required): 到达城市。
- dep_city (String, required): 出发城市。
- traffic_type (Number, required): 交通方式： - 0：飞机 - 1：火车, - 2：汽车, - 3：其他
- itinerary_id (String, required): 行程ID。
- trip_way (Number, required): 行程类型： - 0：单程 - 1：往返
- trip_title (String, required): 申请单标题。
- thirdpart_apply_id (String, required): 外部申请单ID。
- optional: thirdpart_business_id(String), status(Number), user_name(String), deptid(String), corp_name(String), dept_name(String), project_code(String), project_title(String), thirdpart_cost_center_id(String), cost_center_id(Number), arr_city_code(String), dep_city_code(String), trip_day(Number)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), module(OpenApiNewApplyRs), apply_id(Number), thirdpart_apply_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/user-modify-approval-form
updated_at: 2026-06-03 09:58:24
