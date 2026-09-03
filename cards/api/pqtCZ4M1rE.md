# 获取流程的签署详情

doc_id: pqtCZ4M1rE
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/esign/signTasks/{taskId}
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
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
- optional: businessScene(String), flowStatus(Float), signers(Array), signStatus(Float), signerName(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-the-details-of-process-signing
updated_at: 2026-06-04 19:11:14
