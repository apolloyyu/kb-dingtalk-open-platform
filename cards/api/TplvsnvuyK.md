# 机票城市搜索

doc_id: TplvsnvuyK
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/flight/city/suggest
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
- rq (SuggestRq, required): 请求对象，封装城市搜索所需的参数。
- keyword (String, required): 搜索关键字，表示用户输入的城市名称或拼音，用于模糊匹配。
- userid (String, required): 用户的userid，标识发起请求的用户身份。
- corpid (String, required): 企业ID，用于标识所属企业，确保权限与数据隔离。
- optional: type(Number)

## Returns
- optional: result(SuggestRs), cities(CityVo[]), code(String), name(String), distance(Number), travel_name(String), nearby(Boolean), errmsg(String), errcode(Number), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/air-ticket-city-search
updated_at: 2026-06-08 09:47:02
