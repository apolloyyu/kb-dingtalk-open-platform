# 获取流程签署详细信息

doc_id: PUvb0m4cd0
completeness: full
archived: true
method: GET
endpoint: https://api.dingtalk.com/v1.0/esign/flows/sign/detail
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
- optional: data(Object), businessSense(String), flowStatus(Integer), signers(Array), signerName(String), signStatus(Integer), code(Integer), message(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-process-sign-off-details
updated_at: 2026-08-25 09:37:40
