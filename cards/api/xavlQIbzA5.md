# 内购商品订单处理完成

doc_id: xavlQIbzA5
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/appstore/internal/order/finish
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
- biz_order_id (Number, required): 内购订单号。

## Returns
- optional: errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/internal-purchase-order-processing-completed
updated_at: 2026-06-08 09:43:53
