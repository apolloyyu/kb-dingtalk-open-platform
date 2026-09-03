# 修改项目

doc_id: tRmAvxxwhp
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/project/modify
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
- request (OpenProjectRs, required): 请求对象，包含项目修改的具体参数。
- corpid (String, required): 企业的corpid，标识目标企业。
- project_name (String, required): 项目名称，用于展示和识别。
- third_part_id (String, required): 第三方项目ID。
- optional: third_part_invoice_id(String), third_part_cost_center_id(String), code(String)

## Returns
- optional: success(Boolean), module(String), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/project-change
updated_at: 2026-06-08 09:47:11
