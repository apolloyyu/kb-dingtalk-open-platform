# 提交差旅出差申请单

doc_id: tEgqHNObcH
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/trip/approvals
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Trip.MainData.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: userId(String), reason(String), processCode(String), itineraries(Array), vehicle(String), singleOrReturn(String), placeOfDeparture(String), placeOfDepartureDetail(String), destination(String), destinationDetail(String), departureTime(String), returnTime(String)

## Returns
- optional: instanceId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-submittripapprovalprocess
updated_at: 2026-08-07 11:40:59
