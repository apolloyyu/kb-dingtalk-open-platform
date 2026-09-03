# 查询商旅火车票结算记账数据

doc_id: 1l2gk0XvGo
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/alitrip/billSettlements/btripTrains
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
- optional: resultMsg(String), module(Object), category(Long), corpId(String), dataList(Array), alipayTradeNo(String), applyId(String), arrDate(String), arrStation(String), arrTime(String), bookTime(String), bookerId(String), bookerName(String), capitalDirection(String), cascadeDepartment(String), changeFee(double), costCenter(String), costCenterNumber(String), coupon(double), department(String), departmentId(String), deptDate(String), deptStation(String), deptTime(String), feeType(String), index(String), invoiceTitle(String), orderId(String), orderPrice(double), overApplyId(String), primaryId(Long), projectCode(String), projectName(String), refundFee(double), runTime(String), seatNo(String), seatType(String), serviceFee(double), settlementFee(double), settlementTime(String), settlementType(String), status(Long), ticketNo(String), ticketPrice(double), trainNo(String), trainType(String), travelerId(String), travelerName(String), bookerJobNo(String), travelerJobNo(String), voucherType(Long), billRecordTime(String), settlementGrantFee(double), remark(String), periodEnd(String), periodStart(String), totalNum(Long), success(Boolean), resultCode(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/business-travel-train-ticket-settlement-bookkeeping-query-interface
updated_at: 2026-06-03 15:45:28
