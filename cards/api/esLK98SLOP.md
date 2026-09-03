# 搜索企业项目模板

doc_id: esLK98SLOP
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/project/organizations/users/{userId}/templates
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Project.Read.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。

## Query params
- optional: keyword(String)

## Body
- none

## Returns
- optional: result(Array), id(String), description(String), visible(String), isDemo(Boolean), isDeleted(Boolean), name(String), logo(String), created(String), updated(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/search-for-enterprise-custom-templates-by-project-template-name
updated_at: 2026-06-04 19:11:35
