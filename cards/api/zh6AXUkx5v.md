# 批量删除表单实例

doc_id: zh6AXUkx5v
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/yida/forms/instances/batchRemove
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
- formUuid (String, required): 页面编码，获取方式如下所示：
- appType (String, required): 应用编码，获取方式可参考下图所示：
- systemToken (String, required): 应用密钥，获取方式可参考下图所示：
- formInstanceIdList (Array of String, required): 宜搭表单实例Id，调用获取实例ID列表接口或者获取多个表单实例ID接口获取。
- userId (String, required): 用户的userId，可通过获取部门用户userid列表接口获取。
- optional: asynchronousExecution(Boolean), executeExpression(Boolean)

## Returns
- none

## Limits
- 是否需要触发表单绑定的校验规则、关联业务规则和第三方服务回调。 - **true**：需要。 - **false**：不需要 该参数值传false可以降低API的耗时以及获得更大的单次删除数据量上限。

source_url: https://open.dingtalk.com/document/development/delete-multiple-form-instances
updated_at: 2026-06-03 10:11:49
