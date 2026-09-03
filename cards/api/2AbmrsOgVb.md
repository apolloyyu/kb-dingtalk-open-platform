# 查询任务详情

doc_id: 2AbmrsOgVb
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/teamSphere/users/{userId}/tasks/query
api_version: v2-new
app_types: 第三方企业应用
permissions: TeamSphere.Project.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。

## Query params
- taskId (String, required): 任务ID集合,使用逗号分隔。

## Body
- none

## Returns
- optional: result(Array), id(String), taskId(String), content(String), note(String), projectId(String), ancestorIds(Array of String), parentTaskId(String), tfsId(String), tasklistId(String), stageId(String), tagIds(Array of String), creatorId(String), executorId(String), involveMembers(Array of String), priority(Integer), isDone(Boolean), isArchived(Boolean), visible(String), uniqueId(String), startDate(String), dueDate(String), accomplishTime(String), created(String), updated(String), sfcId(String), customfields(Array), cfId(String), type(String), value(Array), title(String), metaString(String), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-queryalltask
updated_at: 2026-06-02 19:46:15
