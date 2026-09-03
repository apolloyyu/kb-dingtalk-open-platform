# 获取流程任务用印审批列表

doc_id: Wy6EaQrCBr
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/esign/approvals/{taskId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Esign.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证。 - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。
- optional: serviceGroup(String)

## Path params
- taskId (String, required): 签署返回的任务ID。

## Query params
- none

## Body
- none

## Returns
- optional: data(Array), approvalName(String), status(String), refuseReason(String), sponsorAccountName(String), startTime(Float), endTime(Float), sealIdImg(String), approvalNodes(Array), approverName(String), approvalTime(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-print-approval-list-for-process-tasks
updated_at: 2026-06-04 19:11:15
