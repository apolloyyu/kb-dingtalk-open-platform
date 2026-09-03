# 创建项目

doc_id: 6FMB2W9mJ4
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/projects
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
- optional: name(String)

## Returns
- optional: result(Object), projectId(String), name(String), creatorId(String), logo(String), visibility(String), uniqueIdPrefix(String), created(String), updated(String), isArchived(Boolean), isSuspended(Boolean), normalType(String), rootCollectionId(String), sourceId(String), defaultCollectionId(String), isTemplate(Boolean), customFields(Array), customFieldId(String), type(String), value(Array), customFieldValueId(String), title(String), metaString(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-project
updated_at: 2026-06-04 19:11:33
