# 删除任务

doc_id: 9dhiHrqqJ2
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/tasks/{taskId}
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
- none

## Returns
- optional: result(Map<String, String>)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-task
updated_at: 2026-06-04 19:11:38
