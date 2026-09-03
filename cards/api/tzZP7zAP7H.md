# 创建待办事项

doc_id: tzZP7zAP7H
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/workrecord/task/create
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- request (SaveTaskRequest, required): 请求对象。
- process_instance_id (String, required): 审批实例ID，由创建实例接口获取。
- tasks (TaskTopVo[], required): 待办事项列表。
- userid (String, required): 待办事项执行人的userid。
- url (String, required): 待办事项跳转URL。
- optional: agentid(Number), activity_id(String)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), tasks(TaskTopVo[]), task_id(Number), userid(String)

## Limits
- 调用本接口把待办事项的审批节点信息同步到钉钉待办。一个待办实例下最多创建100个待办事项。

source_url: https://open.dingtalk.com/document/development/create-a-to-do-task
updated_at: 2026-08-25 09:37:58
