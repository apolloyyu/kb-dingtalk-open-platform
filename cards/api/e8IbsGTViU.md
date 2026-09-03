# 创建或更新项目概览中自定义字段值

doc_id: e8IbsGTViU
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/projects/{projectId}/customfields
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Project.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。
- projectId (String, required): 项目ID，可通过调用查询项目接口获取 。

## Query params
- none

## Body
- value (Array, required): 字段值集合。
- optional: customFieldId(String), customFieldName(String), customFieldInstanceId(String), customFieldValueId(String), title(String), metaString(String)

## Returns
- optional: result(Object), customFieldId(String), originalId(String), name(String), type(String), advancedCustomFieldObjectType(String), value(Array), customFieldValueId(String), title(String), metaString(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-or-update-field-values-project-overview
updated_at: 2026-06-04 19:11:38
