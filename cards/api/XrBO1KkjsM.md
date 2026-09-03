# 创建协作空间任务

doc_id: XrBO1KkjsM
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/teamSphere/users/{userId}/tasks
api_version: v2-new
app_types: 第三方企业应用
permissions: TeamSphere.Project.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 用户userId。

## Query params
- none

## Body
- projectId (String, required): 协作空间id。
- content (String, required): 任务标题。
- optional: executorId(String), dueDate(String), note(String), customfields(Array), customfieldName(String), customfieldId(String), value(Array), title(String), id(String), thumbUrl(String), disableNotification(Boolean), disableActivity(Boolean)

## Returns
- optional: result(Object), taskId(String), content(String), involveMembers(Array of String), projectId(String), executorId(String), creatorId(String), created(String), updated(String), note(String), dueDate(String), priority(Integer), customfields(Array), customfieldId(String), value(Array), title(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-createtask
updated_at: 2026-06-04 14:25:10
