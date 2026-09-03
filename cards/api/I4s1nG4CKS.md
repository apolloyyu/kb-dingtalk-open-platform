# 提交创建企业自建Agent

doc_id: I4s1nG4CKS
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/microApp/enterpriseAgent/submit
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_microapp_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- optional: taskId(String), status(String), expiresIn(String), interval(String), retryCount(String)

## Limits
- 任务结果缓存有效期，单位秒。

source_url: https://open.dingtalk.com/document/development/api-submitcreateenterpriseagent
updated_at: 2026-07-24 09:14:12
