# 获取内购商品SKU页面地址

doc_id: BgwBOGE2Wa
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/appstore/internal/skupage/get
api_version: v1-oapi
app_types: 第三方企业应用
permissions: qyapi_appstore_internal

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用本接口的访问凭证，通过调用获服务商获取第三方应用授权企业的access_token接口获取。

## Body
- goods_code (String, required): 内购商品码。iShot2022-09-20 11
- optional: callback_page(String), extend_param(String)

## Returns
- optional: result(String), errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-address-of-the-product-sku-details-page
updated_at: 2026-06-08 09:43:52
