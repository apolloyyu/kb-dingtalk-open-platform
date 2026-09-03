# 创建企业智能体应用

doc_id: yciY13Hpzk
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/microApp/agent/create
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
- optional: userid(String), appName(String), robotName(String), desc(String), robotMediaId(String), previewMediaId(String)

## Returns
- optional: agentId(String), robotCode(String), clientId(String), clientSecret(String), unifiedAppId(String)

## Limits
- 一次性完成「建应用 + 建机器人 + 下发凭证」的聚合接口，把开发者从 3 步以上的手工配置降为 1 次 API 调用，默认开启范围仅自己可见。

source_url: https://open.dingtalk.com/document/development/api-createagent
updated_at: 2026-07-24 09:14:11
