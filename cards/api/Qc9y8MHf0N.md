# 创建钉钉个人待办任务

doc_id: Qc9y8MHf0N
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/todo/users/me/personalTasks
api_version: v2-new
app_types: 第三方企业应用
permissions: Todo.PersonalTodo.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 接口调用凭证，调用获取用户token接口获取。

## Path params
- none

## Query params
- none

## Body
- subject (String, required): 待办标题，最大长度1024字节。
- executorIds (Array of String, required): 执行者列表，需传用户的unionId，可调用查询用户详情接口获取，最大数量100。
- optional: description(String), dueTime(Long), participantIds(Array of String), notifyConfigs(Object), dingNotify(String), reminderTimeStamp(Long)

## Returns
- optional: taskId(String), createdTime(Long)

## Limits
- 待办标题，最大长度1024字节。
- 待办备注，最大长度4096字节。
- 执行者列表，需传用户的unionId，可调用查询用户详情接口获取，最大数量100。
- 参与者列表，需传用户的unionId，可调用查询用户详情接口获取，最大长度100。
- 待办任务的提醒时间，Unix时间戳，单位毫秒。要求必须大于当前时间，推荐设置为早于待办截止时间的5～10分钟。

source_url: https://open.dingtalk.com/document/development/api-createpersonaltodotask
updated_at: 2026-06-04 19:09:50
