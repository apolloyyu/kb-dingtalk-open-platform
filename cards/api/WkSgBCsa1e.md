# 根据项目模板创建项目

doc_id: WkSgBCsa1e
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/templates/projects
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Project.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。

## Query params
- none

## Body
- name (String, required): 项目名字。
- templateId (String, required): 模板Id，调用搜索企业项目模板接口获取id参数值。

## Returns
- optional: result(Object), id(String), name(String), created(String), logo(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-a-project-from-a-project-template
updated_at: 2026-06-04 19:11:36
