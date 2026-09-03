# 获取子表组件数据

doc_id: kuT4JYxqVw
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/forms/innerTables/{formInstanceId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- formInstanceId (String, required): 要查询的实例的实例ID，可通过获取多个表单实例ID接口获取。

## Query params
- formUuid (String, required): 表单ID。
- appType (String, required): 宜搭应用的唯一编码。
- tableFieldId (String, required): 需要查找的子表单组件ID。
- systemToken (String, required): 应用密钥，在应用数据中获取。
- userId (String, required): 用户的userid。
- optional: pageNumber(Integer), pageSize(Integer), needRowId(Boolean)

## Body
- none

## Returns
- optional: totalCount(Long), pageNumber(Long), data(Array of Object)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-child-table-component-data
updated_at: 2026-06-03 10:11:46
