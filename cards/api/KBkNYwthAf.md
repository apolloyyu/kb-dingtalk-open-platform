# 删除项目成员

doc_id: KBkNYwthAf
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/projects/{projectId}/members/remove
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Project.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。
- projectId (String, required): 项目ID，可通过查询项目接口，获取返回参数`projectId`字段。

## Query params
- none

## Body
- userIds (Array of String, required): 用户userId。

## Returns
- optional: result(Array of String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-project-members
updated_at: 2026-06-03 09:19:55
