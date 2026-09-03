# 查询市内用车申请单

doc_id: PLQcEvXTMi
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/alitrip/cityCarApprovals
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_ali_business_trip

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- corpId (String, required): 企业的CorpId。
- optional: createdEndAt(String), createdStartAt(String), pageNumber(Long), pageSize(Long), thirdPartApplyId(String), userId(String)

## Body
- none

## Returns
- optional: applyList(Array), approverList(Array), note(String), operateTime(String), order(Long), status(Long), statusDesc(String), userId(String), userName(String), departId(String), departName(String), gmtCreate(String), gmtModified(String), itineraryList(Array), arrCity(String), arrCityCode(String), arrDate(String), costCenterId(Long), costCenterName(String), depCity(String), depCityCode(String), depDate(String), invoiceId(Long), invoiceName(String), itineraryId(String), projectCode(String), projectTitle(String), trafficType(Long), thirdPartApplyId(String), tripCause(String), tripTitle(String), total(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-the-application-form-for-third-party-vehicles-in-the-city
updated_at: 2026-06-02 19:54:25
