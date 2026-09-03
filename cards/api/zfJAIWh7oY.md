# 查询机票结算记账数据

doc_id: zfJAIWh7oY
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/alitrip/billSettlements/flights
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
- optional: resultMsg(String), module(Object), category(Long), corpId(String), dataList(Array), advanceDay(Long), airlineCorpCode(String), airlineCorpName(String), alipayTradeNo(String), applyId(String), arrAirportCode(String), arrCity(String), arrDate(String), arrStation(String), arrTime(String), bookTime(String), bookerId(String), bookerName(String), btripCouponFee(double), buildFee(double), cabin(String), cabinClass(String), capitalDirection(String), cascadeDepartment(String), changeFee(double), corpPayOrderFee(double), costCenter(String), costCenterNumber(String), coupon(double), depAirportCode(String), department(String), departmentId(String), deptCity(String), deptDate(String), deptStation(String), deptTime(String), discount(String), feeType(String), flightNo(String), index(String), insuranceFee(double), invoiceTitle(String), itineraryNum(String), itineraryPrice(double), mostDifferenceDeptTime(String), mostDifferenceDiscount(String), mostDifferenceFlightNo(String), mostDifferencePrice(double), mostDifferenceReason(String), mostPrice(double), negotiationCouponFee(double), oilFee(double), orderId(String), overApplyId(String), primaryId(Long), projectCode(String), projectName(String), refundFee(double), refundUpgradeCost(double), repeatRefund(String), sealPrice(double), serviceFee(double), settlementFee(double), settlementTime(String), settlementType(String), status(Long), ticketId(String), travelerId(String), travelerName(String), upgradeCost(double), bookerJobNo(String), travelerJobNo(String), voucherType(Long), billRecordTime(String), settlementGrantFee(double), remark(String), periodEnd(String), periodStart(String), totalNum(Long), success(Boolean), resultCode(Long)

## Limits
- 分页参数，每页数据量。默认值100，最大值500。

source_url: https://open.dingtalk.com/document/development/ticket-settlement-bookkeeping-query-interface
updated_at: 2026-06-02 19:57:41
