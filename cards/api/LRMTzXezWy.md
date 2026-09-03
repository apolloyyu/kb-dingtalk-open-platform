# 查询员工可见的项目分组

doc_id: LRMTzXezWy
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/project/organizations/users/{userId}/groups
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Project.Read.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- optional: userId(String)

## Query params
- optional: viewerId(String), pageSize(Integer)

## Body
- none

## Returns
- optional: result(Array), id(String), visible(String), name(String), created(String), updated(String)

## Limits
- 分页大小。从1开始，默认值10，最大值1000。

source_url: https://open.dingtalk.com/document/development/query-available-project-groups
updated_at: 2026-06-04 19:11:36
