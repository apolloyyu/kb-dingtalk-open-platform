# 创建自由任务

doc_id: F5BpXQdBIL
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/teamSphere/organizations/users/{userId}/tasks
api_version: v2-new
app_types: 第三方企业应用
permissions: TeamSphere.Project.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作人userId。

## Query params
- none

## Body
- content (String, required): 任务标题。
- visible (String, required): 任务可见性。involves：仅参与者可见。
- optional: note(String), involveMembers(Array of String), executorId(String), dueDate(String), disableNotification(Boolean), disableActivity(Boolean)

## Returns
- optional: result(Object), dueDate(String), executor(Object), avatarUrl(String), name(String), userId(String), id(String), visible(String), created(String), involvers(Array), updated(String), note(String), hasReminder(Boolean), creatorId(String), content(String), attachmentsCount(Integer), isDeleted(Boolean), ancestorIds(Array of String), creator(Object), executorId(String), involveMembers(Array of String), isDone(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-createorganizationtask
updated_at: 2026-06-04 14:24:31
