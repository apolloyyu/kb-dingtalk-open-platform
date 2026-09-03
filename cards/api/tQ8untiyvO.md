# 配置发票适用人群

doc_id: tQ8untiyvO
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/rule
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
- request (OpenInvoiceRuleRq, required): 请求对象。
- corpid (String, required): 企业的corpid，可登录开发者后台查看。
- name (String, required): 人员名称。
- id (String, required): 人员id。
- type (Number, required): **1**：员工
- all_employe (Boolean, required): 是否适用所有员工。 - **true**：是 - **false**：否
- third_part_id (String, required): 第三方发票id，调用查询可用发票列表接口获取。
- optional: entities(Entity[])

## Returns
- optional: success(Boolean), module(OpenInvoiceRuleRS), add_num(Number), remove_num(Number), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/configure-invoice-users
updated_at: 2026-06-08 09:47:22
