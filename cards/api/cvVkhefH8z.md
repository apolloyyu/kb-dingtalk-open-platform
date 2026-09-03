# 删除成本中心人员信息

doc_id: cvVkhefH8z
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/entity/delete
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
- rq (OpenCostCenterDeleteEntityRq, required): 请求对象，封装删除操作所需的所有参数。
- thirdpart_id (String, required): 第三方成本中心id。
- entity_id (String, required): 员工/部门/角色id。
- entity_type (String, required): 人员类型： - **1**：员工 - **2**：部门 - **3**：角色
- corpid (String, required): 企业的corpid。
- optional: del_all(Boolean), entity_list(OpenOrgEntityDo[])

## Returns
- optional: result(OpenCostCenterDeleteEntityRs), selected_user_num(Number), remove_num(Number), errmsg(String), errcode(Number), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-the-personnel-information-of-the-cost-center
updated_at: 2026-06-08 09:47:08
