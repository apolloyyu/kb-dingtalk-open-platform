# 更新钉钉待办任务

doc_id: 7jxhP6sBwc
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/todo/users/{unionId}/tasks/{taskId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Todo.Todo.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- unionId (String, required): 当前访问资源所归属用户的unionId，需要操作者的unionId保持一致，可调用查询用户详情接口获取unionid参数值。
- taskId (String, required): 待办ID。

## Query params
- optional: operatorId(String)

## Body
- optional: subject(String), description(String), dueTime(Long), done(Boolean), executorIds(Array of String), participantIds(Array of String), contentFieldList(Array), fieldKey(String), fieldValue(String)

## Returns
- optional: result(Boolean)

## Limits
- 待办标题，最大长度1024。
- 待办描述，最大长度4096。
- 执行者的unionId列表，可调用查询用户详情接口获取，最大数量1000。
- 参与者的unionId列表，可调用查询用户详情接口获取，最大数量1000。

source_url: https://open.dingtalk.com/document/development/updates-dingtalk-to-do-tasks
updated_at: 2026-06-02 19:09:48
