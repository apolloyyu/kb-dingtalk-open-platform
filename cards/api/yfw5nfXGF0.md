# 通过表单实例数据批量更新表单实例

doc_id: yfw5nfXGF0
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/yida/forms/instances/datas
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
- appType (String, required): 宜搭应用编码，该参数从宜搭应用中获取。
- systemToken (String, required): 宜搭应用密钥，该参数从宜搭应用中获取。
- updateFormDataJsonMap (Map, required): 用于更新表单实例的数据，格式为json字符串，能解析成Map结构，解析得到的Map的键为表单实例id，值为表单实例更新值，详情参考创建或更新表单数据格式说明。
- userId (String, required): 用户userid，可通过查询用户详情或获取部门用户userid列表接口获取。
- optional: noExecuteExpression(Boolean), asynchronousExecution(Boolean), ignoreEmpty(Boolean), useLatestFormSchemaVersion(Boolean)

## Returns
- optional: result(Array of String)

## Limits
- 是否不触发表单绑定的校验规则、关联业务规则和第三方服务回调。 - **true**：不触发 - **false**：触发 该参数值传true可以降低API的耗时以及获得更大的单次更新数据量上限。

source_url: https://open.dingtalk.com/document/development/update-multiple-form-instances-with-the-form-instance-data
updated_at: 2026-06-03 10:11:51
