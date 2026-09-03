# 批量更新表单实例内的组件值

doc_id: SA3Vzd0gfn
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/yida/forms/instances/components
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Form.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- formUuid (String, required): 表单的页面编码，该参数从宜搭应用中获取。
- updateFormDataJson (String, required): 用于更新表单实例的数据，格式参考创建或更新表单数据格式说明。
- appType (String, required): 宜搭应用编码，该参数从宜搭应用中获取。
- systemToken (String, required): 宜搭应用密钥，该参数从宜搭应用中获取。
- formInstanceIdList (Array of String, required): 表单实例Id，调用获取实例ID列表接口或者获取多个表单实例ID接口获取。
- userId (String, required): 用户userid，可通过查询用户详情或获取部门用户userid列表接口获取。
- optional: noExecuteExpression(Boolean), ignoreEmpty(Boolean), useLatestFormSchemaVersion(Boolean), asynchronousExecution(Boolean), env(String)

## Returns
- optional: result(Array of String)

## Limits
- 是否不触发表单绑定的校验规则、关联业务规则和第三方服务回调。 - **true**：不触发 - **false**：触发 该参数值传true可以降低API的耗时以及获得更大的单次更新数据量上限。

source_url: https://open.dingtalk.com/document/development/batch-update-of-component-values-in-form-instances
updated_at: 2026-06-03 10:11:49
