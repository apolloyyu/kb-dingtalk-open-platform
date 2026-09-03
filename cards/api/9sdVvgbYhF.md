# 通过RowId更新子表单数据

doc_id: 9sdVvgbYhF
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/yida/forms/updateSubTableByRowId
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
- updateSubTableDataJson (String, required): 用于更新子表单实例的数据，输入为数组格式： - **key**：组件标识，宜搭表单编辑页面，高级设置中查看。 - **value**：组件内的值。
- systemToken (String, required): 宜搭应用密钥。
- formInstanceId (String, required): 表单实例id。
- userId (String, required): 用户的userId，可调用获取部门用户基础信息接口获取用户userId。
- appType (String, required): 宜搭应用唯一标识。
- tableFieldId (String, required): 子表ID。
- optional: useLatestFormSchemaVersion(Boolean), useAlias(Boolean), formUuid(String)

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/update-the-subform-data-via-rowid
updated_at: 2026-06-15 10:53:00
