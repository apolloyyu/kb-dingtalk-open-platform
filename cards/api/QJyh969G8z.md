# 查询可用发票列表

doc_id: QJyh969G8z
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/search
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
- rq (OpenInvoiceRq, required): 请求对象。
- userid (String, required): 用户的userid。
- corpid (String, required): 企业的corpid。
- optional: title(String)

## Returns
- optional: invoice(OpenInvoiceDo[]), id(Number), title(String), success(Boolean), errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-available-invoices
updated_at: 2026-06-08 09:47:23
