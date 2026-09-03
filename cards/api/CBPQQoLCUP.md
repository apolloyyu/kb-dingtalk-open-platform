# 更新项目所在的分组

doc_id: CBPQQoLCUP
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/projects/{projectId}/groups
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
- optional: addProjectGroupIds(Array of String), delProjectGroupIds(Array of String)

## Returns
- optional: result(Object), ok(Boolean)

## Limits
- 将项目添加到的目标项目分组Id列表，最大值5，调用查询员工可见的项目分组接口获取id参数值。
- 移除该项目的项目分组Id列表，最大值5，调用查询员工可见的项目分组接口获取id参数值。

source_url: https://open.dingtalk.com/document/development/update-project-grouping
updated_at: 2026-06-04 19:11:37
