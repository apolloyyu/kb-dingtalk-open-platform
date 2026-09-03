# 删除发票信息

doc_id: rGk7BDRkLN
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/delete
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
- corpid (String, required): 企业的corpid，可登录开发者后台查看。
- third_part_id (String, required): 第三方发票id，调用查询可用发票列表接口获取。
- optional: request(OpenInvoiceDeleteRq)

## Returns
- optional: success(Boolean), module(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-invoice-information
updated_at: 2026-06-08 09:47:27
