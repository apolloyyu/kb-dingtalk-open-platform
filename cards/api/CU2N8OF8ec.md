# 查询用户任务信息列表

doc_id: CU2N8OF8ec
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/tasks/search
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Task.Read.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。

## Query params
- roleTypes (String, required): 用户的任务角色。 **[!NOTE]** `creator`、`executor`、`involveMember` 中的一个或多个，多个以英文逗号拼接。例如：`creator,executor`。
- optional: tql(String), nextToken(String), maxResults(Integer)

## Body
- none

## Returns
- optional: result(Array), taskId(String), content(String), note(String), projectId(String), ancestorIds(Array of String), parentTaskId(String), taskflowStatusId(String), taskListId(String), taskStageId(String), tagIds(Array of String), creatorId(String), executorId(String), involveMembers(Array of String), priority(Integer), storyPoint(String), recurrence(Array of String), isDone(Boolean), isArchived(Boolean), visible(String), uniqueId(String), startDate(String), dueDate(String), accomplishTime(String), created(String), updated(String), scenarioFieldConfigId(String), sprintId(String), customFields(Array), customFieldId(String), type(String), value(Array), customFieldValueId(String), title(String), metaString(String), requestId(String), nextToken(String)

## Limits
- 每页返回最大数量。 **[!NOTE]** 默认10，最大100。
- 任务开始时间(UTC)，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。
- 任务截止时间(UTC)，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。
- 任务完成时间(UTC)，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。
- 创建时间(UTC)，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。
- 更新时间(UTC)，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。

source_url: https://open.dingtalk.com/document/development/querying-user-tasks
updated_at: 2026-06-03 09:26:07
