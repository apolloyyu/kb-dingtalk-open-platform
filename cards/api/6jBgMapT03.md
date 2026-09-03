# 获取月对账结算数据

doc_id: 6jBgMapT03
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/monthbill/url/get
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
- request (OpenAccountRq, required): 请求对象。
- corpid (String, required): 企业的corpid，可登录开发者后台查看。
- optional: bill_month(String)

## Returns
- optional: success(Boolean), module(OpenAccountRs[]), start_date(String), end_date(String), url(String), errcode(Number), errmsg(String), request_id(String)

## Limits
- json数据下载链接，通过HttpClient 获取，并以GBK格式解析，链接有效期为五分钟。

source_url: https://open.dingtalk.com/document/development/obtain-monthly-reconciliation-settlement-data
updated_at: 2026-06-08 09:47:28
