# 火车票城市搜索

doc_id: CGaQhr0EYP
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/train/city/suggest
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
- rq (SuggestRq, required): 请求对象。
- keyword (String, required): 搜索关键字，用于匹配城市名称或城市码。
- userid (String, required): 当前操作用户的ID，用于上下文识别与权限校验。
- corpid (String, required): 企业标识ID，用于确定所属企业数据范围。

## Returns
- optional: result(SuggestRs), cities(CityVo[]), name(String), code(String), errmsg(String), errcode(Number), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/train-ticket-city-search
updated_at: 2026-06-08 09:47:03
