# 更新数据表单实例

doc_id: BN5XCNmHRL
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/dataForms/formInstances
api_version: v2-new
app_types: 企业内部应用
permissions: Premium.Workflow.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- originatorUserId (String, required): 数据表单发起人的userId。
- processCode (String, required): 数据表单模板code。可在数据表单模板编辑页-基础设置-页面底部查看。
- formComponentValueList (Array, required): 表单控件列表。 具体请参照请求示例规范填写。
- name (String, required): 控件名称。
- value (String, required): 控件值。
- optional: id(String), bizAlias(String), extValue(String), componentType(String), details(Array), formInstanceIds(Array of String)

## Returns
- optional: instanceId(String)

## Limits
- 子控件列表，最大列表长度：150。

source_url: https://open.dingtalk.com/document/development/api-premiumupdateforminstance
updated_at: 2026-06-03 10:13:04
