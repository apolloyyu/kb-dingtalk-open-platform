# 查询表单的变更记录

doc_id: tEooXo9scE
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/yida/forms/operationsLogs/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- formUuid (String, required): 表单编码。 该参数从宜搭应用中获取。
- appType (String, required): 宜搭应用编码。 该参数从宜搭应用中获取。
- systemToken (String, required): 宜搭应用密钥。 该参数从宜搭应用中获取。
- userId (String, required): 用户userId。
- optional: formInstanceIdList(Array of String)

## Returns
- optional: operationLogMap(Map)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/change-records-of-query-forms
updated_at: 2026-06-03 10:11:47
