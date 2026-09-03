# 审批市内用车申请单

doc_id: zYuWEesjM9
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/alitrip/cityCarApprovals
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_ali_business_trip_write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- corpId (String, required): 第三方企业的corpid。
- status (Long, required): 审批结果： - **1**：同意 - **2**：拒绝
- thirdPartApplyId (String, required): 第三方审批单ID。
- userId (String, required): 审批的第三方员工ID。
- optional: operateTime(String), remark(String)

## Returns
- optional: approveResult(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/approval-of-third-party-city-car-application-form
updated_at: 2026-06-04 19:10:48
