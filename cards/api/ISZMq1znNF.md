# 获取流程任务合同列表

doc_id: ISZMq1znNF
completeness: full
archived: true
method: GET
endpoint: https://api.dingtalk.com/v1.0/esign/flows/docs
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
- optional: data(Array), fileId(String), fileName(String), fileUrl(String), code(Integer), message(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-process-task-contract-list
updated_at: 2026-08-25 09:37:39
