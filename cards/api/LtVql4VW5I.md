# 搜索第三方机票超标审批单

doc_id: LtVql4VW5I
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/alitrip/exceedapply/getFlight
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_ali_business_trip

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- corpId (String, required): 第三方企业的corpId。
- applyId (String, required): 商旅超标审批单ID。

## Body
- none

## Returns
- optional: corpId(String), applyId(Long), status(Integer), btripCause(String), exceedType(Integer), exceedReason(String), originStandard(String), submitTime(String), userId(String), applyIntentionInfoDO(Object), arrCity(String), arrCityName(String), arrTime(String), cabin(String), cabinClass(Integer), cabinClassStr(String), depCity(String), depCityName(String), depTime(String), discount(double), flightNo(String), price(Long), type(Integer), thirdpartApplyId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/dingtalk-oapi-alitrip-btrip-exceedapply-flight
updated_at: 2026-06-02 19:51:50
