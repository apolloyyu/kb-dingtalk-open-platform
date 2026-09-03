# 获取异步转译任务结果

doc_id: Qd412Y1qzD
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/contact/files/translateResults
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_get_member

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- jobId (String, required): 异步转译任务ID，调用异步转译通讯录ID接口获取jobId参数值。

## Body
- none

## Returns
- optional: status(String), url(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-results-of-an-asynchronous-translation-task
updated_at: 2026-07-02 10:35:54
