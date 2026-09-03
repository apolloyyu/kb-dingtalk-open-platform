# 搜索任务工作流状态

doc_id: oUJsLLP2uK
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/projects/{projectId}/taskflowStatuses/search
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Task.Read.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。
- projectId (String, required): 项目ID，可通过调用根据项目模板创建项目接口，获取返回参数`id`字段值。

## Query params
- optional: query(String), maxResults(Integer), nextToken(String), tfIds(String), tfsIds(String)

## Body
- none

## Returns
- optional: result(Array), taskflowStatusId(String), name(String), pos(Integer), taskflowId(String), rejectStatusIds(Array of String), kind(String), creatorId(String), isDeleted(Boolean), created(String), updated(String), isTaskflowstatusruleexector(Boolean)

## Limits
- 每页返回最大数量。 默认10，最大300。

source_url: https://open.dingtalk.com/document/development/search-task-workflow-status
updated_at: 2026-06-04 19:11:41
