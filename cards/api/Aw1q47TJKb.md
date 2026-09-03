# 查询成本中心

doc_id: Aw1q47TJKb
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/query
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
- rq (OpenCostCenterQueryRq, required): 请求对象。
- corpid (String, required): 企业的corpid。
- optional: title(String), thirdpart_id(String), userid(String), need_org_entity(Boolean)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), cost_center_list(OpenCostCenterQueryRs[]), id(Number), corpid(String), title(String), number(String), thirdpart_id(String), scope(Number), alipay_no(String), entity_list(OpenOrgEntityDo[]), entity_type(String), entity_id(String), name(String), user_num(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-cost-center
updated_at: 2026-06-03 09:58:23
