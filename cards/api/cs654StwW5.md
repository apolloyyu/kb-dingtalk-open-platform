# 搜索第三方火车票超标审批单

doc_id: cs654StwW5
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/alitrip/exceedapply/getTrain
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_ali_business_trip

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- corpId (String, required): 第三方企业的`corpId`。
- applyId (String, required): 商旅审批单ID，用于唯一标识一条审批记录。

## Body
- none

## Returns
- optional: corpId(String), applyId(Long), status(Integer), btripCause(String), exceedType(Integer), exceedReason(String), originStandard(String), submitTime(String), userId(String), applyIntentionInfoDO(Object), price(Long), depCityName(String), arrCityName(String), depCity(String), arrCity(String), depTime(String), arrTime(String), arrStation(String), depStation(String), trainNo(String), trainTypeDesc(String), seatName(String), thirdpartApplyId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/dingtalk-oapi-alitrip-btrip-exceedapply-train-get
updated_at: 2026-06-02 19:51:49
