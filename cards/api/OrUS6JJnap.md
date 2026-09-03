# 新建审批单

doc_id: OrUS6JJnap
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/new
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
- rq (OpenApiNewApplyRq, required): 请求对象，封装完整的审批单创建参数。
- thirdpart_apply_id (String, required): 外部申请单id。
- trip_title (String, required): 申请单标题。
- itinerary_list (OpenItineraryInfo[], required): 行程列表。
- trip_way (Number, required): 行程类型： - **0**：单程 - **1**：往返
- itinerary_id (String, required): 用户自定义行程ID。
- traffic_type (Number, required): 交通方式： - **0**：飞机 - **1**：火车 - **2**：汽车 - **3**：其他
- dep_city (String, required): 出发城市。
- arr_city (String, required): 到达城市。
- cost_center_id (Number, required): 商旅成本中心id，可通过查询成本中心接口获取。 **[!NOTE]** 若不填则第三方成本中心id必填。
- invoice_id (Number, required): 发票id，可调用查询可用发票列表接口获取。
- dep_date (Date, required): 出发日期。
- arr_date (Date, required): 到达日期。
- trip_cause (String, required): 出差事由。
- userid (String, required): 用户的userid。
- traveler_list (OpenUserInfo[], required): 出行人列表。
- corpid (String, required): 企业的corpid，可登录开发者后台查看。
- optional: trip_day(Number), dep_city_code(String), arr_city_code(String), thirdpart_cost_center_id(String), project_title(String), project_code(String), dept_name(String), corp_name(String), user_name(String), deptid(String), status(Number), thirdpart_business_id(String)

## Returns
- optional: module(OpenApiNewApplyRs), thirdpart_apply_id(String), apply_id(Number), errmsg(String), errcode(Number), success(Boolean), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/user-new-approval-form
updated_at: 2026-06-03 09:58:26
