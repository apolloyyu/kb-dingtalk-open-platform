# 获取用户加入的项目

doc_id: emScPgy3gC
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/joinProjects
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Project.Read.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。

## Query params
- optional: maxResults(Integer), nextToken(String)

## Body
- none

## Returns
- optional: result(Array of String), nextToken(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-projects-joined-by-users
updated_at: 2026-06-03 09:19:56
