# 服务商获取第三方应用授权企业的access_token

doc_id: NrZCOOaMBH
completeness: full
archived: true
method: POST
endpoint: https://oapi.dingtalk.com/service/get_corp_token
api_version: v1-oapi
app_types: 企业内部应用（委托产品方案商）, 第三方企业应用
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- optional: expires_in(Number), access_token(String), errmsg(String), errcode(Number)

## Limits
- - access_token的有效期为7200秒（2小时），有效期内重复获取会返回新的access_token。

source_url: https://open.dingtalk.com/document/development/obtain-isvapp-token
updated_at: 2026-08-25 09:36:30
