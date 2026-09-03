# 新增发票配置

doc_id: mbnLh3HVLF
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/add
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
- rq (OpenInvoiceModifyAndNewRq, required): 发票信息请求对象，包含完整的发票配置内容。
- corpid (String, required): 企业的corpid，可登录开发者后台查看。
- type (Number, required): 发票类型： - **1**：增值税普通发票 - **2**：增值税专用发票
- title (String, required): 发票抬头。
- tax_no (String, required): 纳税人识别号。
- third_part_id (String, required): 第三方发票id。
- optional: bank_name(String), address(String), tel(String), bank_no(String)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), module(Number), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/new-invoice-configuration
updated_at: 2026-06-08 09:47:21
