# 查询项目中的任务

doc_id: XFxugf87aR
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/projectIds/{projectId}/tasks
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Task.Read.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。
- projectId (String, required): 项目ID。 目前需要从项目链接中获取该参数值，获取步骤：进入**项目** > 右上角单击**菜单** > **复制链接**。 得到的项目链接示例：`https://www.teambition.com/project/62c794xxxxx` ，project下一级路径的值就是项目ID。

## Query params
- optional: nextToken(String), maxResults(Integer), query(String)

## Body
- none

## Returns
- optional: totalCount(Integer), nextToken(String), result(Array), taskId(String), content(String), involveMembers(Array of String), projectId(String), executorId(String), creatorId(String), isDeleted(Boolean), labels(String), created(String), updated(String), scenariofieldconfigId(String), customfields(Array of String), note(String), startDate(String), dueDate(String), priority(Long), taskflowstatusId(String), isDone(Boolean), isArchived(Boolean), visible(String), tagIds(String), stageId(String), sprintId(String), accomplished(String), storyPoint(Integer), progress(Integer), ancestorIds(Array of String)

## Limits
- 每页返回最大数量。默认10，最大500。

source_url: https://open.dingtalk.com/document/development/query-tasks-in-a-project
updated_at: 2026-06-04 19:11:40
