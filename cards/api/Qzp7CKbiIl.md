# 更新任务参与者

doc_id: Qzp7CKbiIl
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/tasks/{taskId}/involveMembers
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Task.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。
- taskId (String, required): 任务ID，可通过调用查询项目中的任务接口，获取返回参数`taskId`字段。

## Query params
- none

## Body
- optional: involveMembers(Array of String), addInvolvers(Array of String), delInvolvers(Array of String)

## Returns
- optional: result(Object), involveMembers(Array of String), updated(String)

## Limits
- 更新时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。

source_url: https://open.dingtalk.com/document/development/update-task-participants
updated_at: 2026-06-03 09:26:13
