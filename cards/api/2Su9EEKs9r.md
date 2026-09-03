# 设置成本中心人员信息

doc_id: 2Su9EEKs9r
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/entity/set
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
- rq (OpenCostCenterSetEntityRq, required): 请求对象，包含成本中心及人员列表信息。
- thirdpart_id (String, required): 第三方成本中心id。
- entity_list (OpenOrgEntityDo[], required): 人员信息列表。
- entity_id (String, required): 员工/部门/角色id。
- entity_type (String, required): 人员类型： - **1**：员工 - **2**：部门 - **3**：角色
- corpid (String, required): 企业的corpid。

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), result(OpenCostCenterSetEntityRs), add_num(Number), remove_num(Number), selected_user_num(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/set-up-cost-center-personnel-information
updated_at: 2026-06-03 09:58:29
