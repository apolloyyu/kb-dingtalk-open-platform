# 查询用车结算记账记录

doc_id: t9useW0Cqi
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/alitrip/billSettlements/cars
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_ali_business_trip

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: corpId(String), category(Long), pageSize(Long), periodStart(String), periodEnd(String), pageNumber(Long)

## Body
- none

## Returns
- optional: resultMsg(String), module(Object), category(Long), corpId(String), dataList(Array), alipayTradeNo(String), applyId(String), arrCity(String), arrDate(String), arrLocation(String), arrTime(String), bookTime(String), bookerId(String), bookerName(String), businessCategory(String), capitalDirection(String), carLevel(String), cascadeDepartment(String), costCenter(String), costCenterNumber(String), coupon(double), couponPrice(double), department(String), departmentId(String), deptCity(String), deptDate(String), deptLocation(String), deptTime(String), estimateDriveDistance(String), estimatePrice(double), feeType(String), index(String), invoiceTitle(String), memo(String), orderId(String), orderPrice(double), overApplyId(String), personSettleFee(double), primaryId(String), projectCode(String), projectName(String), providerName(String), realDriveDistance(String), realFromAddr(String), realToAddr(String), serviceFee(String), settlementFee(double), settlementTime(String), settlementType(String), specialOrder(String), specialReason(String), status(Long), travelerId(String), travelerName(String), userConfirmDesc(String), bookerJobNo(String), travelerJobNo(String), voucherType(Long), subOrderId(String), billRecordTime(String), settlementGrantFee(double), remark(String), periodEnd(String), periodStart(String), totalNum(Long), success(Boolean), resultCode(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-interface-for-vehicle-settlement-and-bookkeeping
updated_at: 2026-06-22 14:00:41
