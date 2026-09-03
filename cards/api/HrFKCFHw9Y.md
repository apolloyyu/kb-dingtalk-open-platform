# 获取用户参与项目

doc_id: HrFKCFHw9Y
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/teamSphere/users/{userId}/projects/userJoined
api_version: v2-new
app_types: 第三方企业应用
permissions: TeamSphere.Project.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。

## Query params
- optional: projectIds(String), projectRoleLevels(String), sortBy(String), maxResults(Integer), nextToken(String)

## Body
- none

## Returns
- optional: result(Array of String), requestId(String), nextToken(String)

## Limits
- 每页返回最大数量。默认10，最大300。

source_url: https://open.dingtalk.com/document/development/api-getuserjoinedprojectsv3
updated_at: 2026-06-02 19:46:15
