# 获取任务列表

doc_id: KqksNa2CjI
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/projects/{projectId}/taskStages/search
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Task.Read.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。
- projectId (String, required): 项目ID，可通过查询项目接口，获取返回参数`projectId`字段。

## Query params
- optional: taskListId(String), query(String), maxResults(Integer), nextToken(String), taskStageIds(String)

## Body
- none

## Returns
- optional: result(Array), taskStageId(String), name(String), description(String), projectId(String), taskListId(String), creatorId(String), created(String), updated(String), nextToken(String)

## Limits
- 每页返回最大数量。 **[!NOTE]** 默认10，最大300。
- 创建时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。
- 更新时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。

source_url: https://open.dingtalk.com/document/development/get-task-list
updated_at: 2026-06-03 09:26:06
