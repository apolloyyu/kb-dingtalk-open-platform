# 批量创建表单实例

doc_id: J28uXSUqBQ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/yida/forms/instances/batchSave
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
- formUuid (String, required): 页面编码，获取方式可参考下图所示：
- appType (String, required): 应用编码，获取方式可参考下图所示：
- systemToken (String, required): 应用密钥，获取方式可参考下图所示：
- userId (String, required): 用户userId，可通过获取部门用户userid列表接口获取。
- formDataJsonList (Array of String, required): 表单实例数据，格式参考创建或更新表单数据格式说明。
- optional: noExecuteExpression(Boolean), asynchronousExecution(Boolean), keepRunningAfterException(Boolean), env(String)

## Returns
- optional: result(Array of String)

## Limits
- 是否不触发表单绑定的校验规则、关联业务规则和第三方服务回调。 - **true**：不触发 - **false**：触发 该参数值传true可以降低API的耗时以及获得更大的单次保存数据量上限。

source_url: https://open.dingtalk.com/document/development/create-multiple-form-instances
updated_at: 2026-06-03 10:12:02
