# 查询酒店结算记账数据

doc_id: S1rPapKtqq
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/alitrip/billSettlements/hotels
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_ali_business_trip

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: corpId(String), category(Long), pageSize(Long), periodStart(String), pageNumber(Long), periodEnd(String)

## Body
- none

## Returns
- optional: resultMsg(String), module(Object), category(Long), corpId(String), dataList(Array), alipayTradeNo(String), applyId(String), bookTime(String), bookerId(String), bookerName(String), capitalDirection(String), cascadeDepartment(String), checkInDate(String), checkoutDate(String), city(String), cityCode(String), corpRefundFee(double), corpTotalFee(double), costCenter(String), costCenterNumber(String), department(String), departmentId(String), feeType(String), fees(double), fuPointFee(double), hotelName(String), index(String), invoiceTitle(String), isNegotiation(Boolean), isShareStr(String), nights(Long), orderId(String), orderPrice(double), orderType(String), overApplyId(String), personRefundFee(double), personSettlePrice(double), primaryId(Long), projectCode(String), projectName(String), promotionFee(double), roomNumber(Long), roomPrice(double), roomType(String), serviceFee(double), settlementFee(double), settlementTime(String), settlementType(String), status(Long), totalNights(Long), travelerId(String), travelerName(String), bookerJobNo(String), travelerJobNo(String), voucherType(Long), billRecordTime(String), settlementGrantFee(double), remark(String), periodEnd(String), periodStart(String), totalNum(Long), success(Boolean), resultCode(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/hotel-settlement-bookkeeping-query-interface
updated_at: 2026-06-04 19:10:49
