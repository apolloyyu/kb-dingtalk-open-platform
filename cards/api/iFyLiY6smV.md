# 获取表单内的组件信息

doc_id: iFyLiY6smV
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/forms/formFields
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- appType (String, required): 应用编码，获取方式可参考下图所示：
- systemToken (String, required): 应用密钥，获取方式可参考下图所示：
- formUuid (String, required): 表单唯一标识，可通过以下方式获取： - 调用获取指定应用下的表单列表接口获取formUuid参数值。 - 通过应用获取：
- userId (String, required): 操作人userId，可通过获取部门用户userid列表接口获取。

## Body
- none

## Returns
- optional: success(Boolean), result(Array), componentName(String), fieldId(String), behavior(String), label(Any), props(Any), children(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-form-field-information-based-on-form-uuid
updated_at: 2026-06-03 10:11:43
