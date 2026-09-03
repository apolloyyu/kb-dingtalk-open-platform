# 删除数据表单实例

doc_id: 7hDYZO7W3z
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/dataForms/formInstances/remove
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
- processCode (String, required): 数据表单模板code。可在数据表单模板编辑页-基础设置-页面底部查看。
- optional: formInstanceIds(Array of String), userId(String)

## Returns
- optional: success(String)

## Limits
- 用户userId，仅限以管理员身份调用。
- - 本接口仅限以管理员身份调用。

source_url: https://open.dingtalk.com/document/development/api-premiumdeleteforminstance
updated_at: 2026-06-03 10:13:05
