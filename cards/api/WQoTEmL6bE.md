# 更新项目任务的自定义字段值

doc_id: WQoTEmL6bE
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/tasks/{taskId}/customFields
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Task.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。
- taskId (String, required): 任务id，调用创建项目任务接口获取的taskId。

## Query params
- none

## Body
- value (Array, required): 自定义字段值列表，最多10个。
- title (String, required): 自定义字段修改后的值。
- optional: customFieldName(String), customFieldId(String)

## Returns
- optional: result(Object), customFields(Array), customFieldId(String), value(Array), title(String)

## Limits
- 自定义字段值列表，最多10个。

source_url: https://open.dingtalk.com/document/development/update-task-custom-field-value
updated_at: 2026-06-04 19:11:43
