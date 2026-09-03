# 更新自由任务状态

doc_id: nVkG5ZpRg3
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/project/organizations/users/{userId}/tasks/{taskId}/states
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Task.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- taskId (String, required): 任务id，调用创建自由任务接口获取的id值。
- userId (String, required): 操作者userId。

## Query params
- none

## Body
- isDone (Boolean, required): 自由任务状态。 - **true**：完成 - **false**： 未完成
- optional: disableActivity(Boolean), disableNotification(Boolean)

## Returns
- optional: result(Object), isDone(Boolean), updateTime(String)

## Limits
- 更新任务状态的时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。

source_url: https://open.dingtalk.com/document/development/change-free-task-status
updated_at: 2026-06-04 19:11:46
