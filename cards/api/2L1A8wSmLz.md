# 查询项目状态

doc_id: 2L1A8wSmLz
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/projects/{projectId}/statuses
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Project.Read.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。
- projectId (String, required): 项目ID，可通过调用查询项目接口获取。

## Query params
- none

## Body
- none

## Returns
- optional: result(Array), projectId(String), name(String), content(String), degree(String), creatorId(String), created(String)

## Limits
- 创建时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。

source_url: https://open.dingtalk.com/document/development/query-project-status
updated_at: 2026-06-04 19:11:34
