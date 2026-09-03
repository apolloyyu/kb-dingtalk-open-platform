# 查询企业下用户待办列表

doc_id: UqK09TsE5H
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/todo/users/{unionId}/org/tasks/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Todo.Todo.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- unionId (String, required): 用户的unionId，可调用查询用户详情接口获取。

## Query params
- none

## Body
- optional: nextToken(String), isDone(Boolean), roleTypes(Array of Array), todoType(String)

## Returns
- optional: nextToken(String), todoCards(Array), taskId(String), subject(String), dueTime(Long), detailUrl(Object), appUrl(String), pcUrl(String), priority(Integer), createdTime(Long), modifiedTime(Long), creatorId(String), sourceId(String), bizTag(String), isDone(Boolean), todoType(String)

## Limits
- - 接口最多可以获取到180天内已完成状态的待办任务；未完成状态的待办任务无此限制。

source_url: https://open.dingtalk.com/document/development/query-the-to-do-list-of-enterprise-users
updated_at: 2026-06-04 19:09:52
