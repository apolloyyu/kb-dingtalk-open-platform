# 获取表单组件定义列表

doc_id: mxuXJv0Ogw
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/forms/definitions/{appType}/{formUuid}
api_version: v2-new
app_types: 第三方企业应用
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
- optional: result(Array), label(String), componentName(String), fieldId(String), parentId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-a-list-of-form-component-definitions
updated_at: 2026-06-03 10:11:44
