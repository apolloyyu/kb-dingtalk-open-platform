# 获取未处理的已支付订单

doc_id: T7YyaWfMgi
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/appstore/internal/unfinishedorder/list
api_version: v1-oapi
app_types: 第三方企业应用
permissions: isvapi_appstore_internal

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端接口的授权凭证，可调用获取第三方企业应用的suite_access_token接口获得。

## Body
- page (Number, required): 分页查询页码，起始页码为1。
- page_size (Number, required): 分页查询每页大小，最大限制100。
- optional: item_code(String)

## Returns
- optional: result(PageModel), total(Number), items(InAppGoodsOrderVO[]), create_timestamp(Number), paid_timestamp(Number), quantity(Number), status(Number), total_actual_pay_fee(Number), item_code(String), corp_id(String), biz_order_id(Number), goods_code(String), errcode(Number), errmsg(String)

## Limits
- 分页查询每页大小，最大限制100。

source_url: https://open.dingtalk.com/document/development/obtaining-isv-unfinished-processing-order
updated_at: 2026-06-08 09:43:56
