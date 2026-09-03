# 获取协作空间列表

doc_id: LJj5rKquQ3
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/teamSphere/projects
api_version: v2-new
app_types: 第三方企业应用
permissions: TeamSphere.Project.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- userId (String, required): 操作者userId。
- optional: projectIds(String), name(String), maxResults(Integer), nextToken(String), sourceId(String), includeTemplate(Boolean)

## Body
- none

## Returns
- optional: result(Array), id(String), name(String), logo(String), description(String), organizationId(String), isTemplate(Boolean), creatorId(String), created(String), updated(String), sourceId(String), requestId(String), nextToken(String)

## Limits
- 每页返回最大数量。默认10，最大300。

source_url: https://open.dingtalk.com/document/development/api-searchprojectsv3-1
updated_at: 2026-06-02 19:46:14
