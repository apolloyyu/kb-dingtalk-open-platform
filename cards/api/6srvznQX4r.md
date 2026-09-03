# 查询创建企业自建Agent任务进度

doc_id: 6srvznQX4r
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/microApp/agent/create/query
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
- optional: taskId(String), status(String), agentId(String), robotCode(String), clientId(String), clientSecret(String), errorCode(String), errorMsg(String), expiresIn(Long), interval(Long), retryCount(Long), gmtCreate(Long), gmtModified(Long), unifiedAppId(String)

## Limits
- 任务有效期，单位秒。

source_url: https://open.dingtalk.com/document/development/api-querycreateenterpriseagent
updated_at: 2026-07-22 17:11:42
