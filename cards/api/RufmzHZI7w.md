# 新增或更新表单实例

doc_id: RufmzHZI7w
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/yida/forms/instances/insertOrUpdate
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Yida.Form.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- formUuid (String, required): 页面编码，获取方式可参考下图所示：
- searchCondition (String, required): 用于检索表单实例数据的检索条件，格式参考表单筛选组件格式。
- appType (String, required): 应用编码，获取方式可参考下图所示：
- formDataJson (String, required): 用于更新或新增表单实例的数据，格式参考创建或更新表单数据格式。
- systemToken (String, required): 应用密钥，获取方式可参考下图所示：
- userId (String, required): 用户的userId，可通过获取部门用户userid列表接口获取。
- optional: noExecuteExpression(Boolean), useAlias(Boolean), env(String)

## Returns
- optional: result(Array of String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-createorupdateformdata-v2
updated_at: 2026-06-15 10:42:22
