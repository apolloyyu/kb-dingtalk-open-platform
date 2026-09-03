# 删除钉钉待办任务

doc_id: luZvsbYUIa
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/todo/users/{unionId}/tasks/{taskId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Todo.Todo.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- unionId (String, required): 当前访问资源所归属用户的unionId，和操作者的unionId保持一致，可调用查询用户详情接口获取。
- taskId (String, required): 待办ID。

## Query params
- optional: operatorId(String)

## Body
- none

## Returns
- optional: result(Boolean), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-dingtalk-to-do-tasks
updated_at: 2026-06-04 19:09:51
