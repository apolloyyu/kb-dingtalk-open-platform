# 获取流程任务用印审批列表

doc_id: sGov9QCMOW
completeness: full
archived: true
method: GET
endpoint: https://api.dingtalk.com/v1.0/esign/seals/approval/list
api_version: v2-new
app_types: 第三方企业应用
permissions: not_stated

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: taskId(String)

## Body
- none

## Returns
- optional: data(Array), approvalName(String), status(String), refuseReason(String), sponsorAccountName(String), startTime(Long), endTime(Long), sealIdImg(String), approvalNodes(Array), approverName(String), approvalTime(Long), code(Integer), message(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-process-task-print-approval-list-1
updated_at: 2026-08-25 09:37:38
