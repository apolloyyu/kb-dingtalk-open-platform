# 回传第三方超标审批结果

doc_id: XHJlaFVhmJ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/alitrip/exceedapply/sync
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_ali_business_trip

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- remark (String, required): 审批意见。
- applyId (String, required): 商旅超标审批单号。
- corpId (String, required): 企业的corpId。
- thirdpartyFlowId (String, required): 第三方流程实例ID。
- userId (String, required): 员工的userid。
- status (Integer, required): 审批单状态，取值： - **1**：同意 - **2**：拒绝

## Body
- none

## Returns
- optional: module(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/dingtalk-oapi-alitrip-btrip-exceedapply-sync
updated_at: 2026-06-04 19:10:46
