# 添加项目成员

doc_id: nJYUNe45kN
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/projects/{projectId}/members
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Project.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。
- projectId (String, required): 项目Id，调用根据项目模板创建项目接口获取id参数值。

## Query params
- none

## Body
- userIds (Array of String, required): 被添加的用户userId列表，建议一次不超过10个。

## Returns
- optional: result(Array), nickname(String), joined(String)

## Limits
- 被添加的用户userId列表，建议一次不超过10个。

source_url: https://open.dingtalk.com/document/development/add-project-members
updated_at: 2026-06-04 19:11:34
