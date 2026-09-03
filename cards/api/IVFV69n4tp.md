# 获取组件别名列表

doc_id: IVFV69n4tp
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/yida/forms/component/alias/{appType}/{formUuid}
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Yida.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- appType (String, required): 应用编码。
- formUuid (String, required): 表单ID。

## Query params
- systemToken (String, required): 应用密钥。
- userId (String, required): 用户的userid。
- optional: language(String), version(Long)

## Body
- none

## Returns
- optional: result(Array), fieldId(String), alias(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getformcomponentaliaslist
updated_at: 2026-06-15 10:44:18
