# 应用内购商品核销

doc_id: ReZ3ovkC4C
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/appstore/internal/order/consume
api_version: v1-oapi
app_types: 第三方企业应用
permissions: qyapi_appstore_internal

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用本接口的访问凭证，通过调用服务商获取第三方应用授权企业的access_token接口获取。

## Body
- biz_order_id (Number, required): 内购商品订单号。
- request_id (String, required): 核销请求ID，由ISV生成，用于请求幂等。
- quantity (Number, required): 订购商品核销数量。
- userid (String, required): 员工在当前企业内的唯一标识，也称staffId。

## Returns
- optional: errmsg(String), errcode(Number)

## Limits
- 通过本接口可在应用内购流程中对订购商品进行核销操作，适用于第三方SaaS服务商根据客户实际使用情况（如开通人数、使用时长等）定期核销已使用的订购额度的业务场景。每次成功调用将记录一条核销流水，确保订单使用状态可追溯。

source_url: https://open.dingtalk.com/document/development/application-of-in-house-purchase-verification
updated_at: 2026-06-08 09:43:55
