# 终止流程实例

doc_id: dDXOJYFU6e
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/yida/processes/instances/terminate
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Process.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- appType (String, required): 应用ID。
- systemToken (String, required): 应用密钥。
- userId (String, required): 用户的userid。
- processInstanceId (String, required): 流程实例ID，可通过调用发起宜搭审批流程接口获取。
- optional: language(String)

## Body
- none

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/terminate-a-process-instance
updated_at: 2026-06-03 10:11:40
