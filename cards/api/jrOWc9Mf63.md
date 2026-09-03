# 更新钉钉待办执行者状态

doc_id: jrOWc9Mf63
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/todo/users/{unionId}/tasks/{taskId}/executorStatus
api_version: v2-new
app_types: 第三方企业应用
permissions: Todo.Todo.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- unionId (String, required): 当前访问的资源所归属用户的unionId，可调用查询用户详情接口获取。
- taskId (String, required): 待办ID。

## Query params
- optional: operatorId(String)

## Body
- optional: executorStatusList(Array), id(String), isDone(Boolean)

## Returns
- optional: result(Boolean)

## Limits
- 执行者状态列表，id需传用户的unionId，调用查询用户详情接口获取unionid参数值，最大数量1000。

source_url: https://open.dingtalk.com/document/development/update-dingtalk-to-do-status
updated_at: 2026-06-04 19:09:52
