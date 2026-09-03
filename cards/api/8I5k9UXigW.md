# 添加项目

doc_id: 8I5k9UXigW
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/project/add
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
- request (OpenProjectRs, required): 请求对象。
- corpid (String, required): 企业的corpid。
- project_name (String, required): 项目名称。
- third_part_id (String, required): 第三方项目ID。
- optional: third_part_invoice_id(String), third_part_cost_center_id(String), code(String)

## Returns
- optional: success(Boolean), module(String), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-a-project
updated_at: 2026-06-08 09:47:10
