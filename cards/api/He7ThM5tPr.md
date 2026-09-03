# 更新待办状态

doc_id: He7ThM5tPr
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/workrecord/task/update
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
- request (UpdateTaskRequest, required): 请求对象。
- agentid (Number, required): 应用标识。可在开发者后台的应用详情页获取。
- process_instance_id (String, required): 实例ID，由创建实例接口获取。
- tasks (TaskTopVo[], required): 待办任务列表。
- task_id (Number, required): 待办任务ID，需要在调用查询待办列表接口时，主动设置该值。
- status (String, required): 任务状态： - **CANCELED**：取消 例如一个或签节点，同时有多个任务，其中一个审批人完成审批后，剩余的审批任务可以置为CANCELED状态。 - **COMPLETED**：完成 COMPLETED表示任务被完成，此时需要传**result**参数，分别表示审批通过（agree）和审批拒绝（refuse）。
- result (String, required): 当status为COMPLETED时，必须指定任务结果： - **AGREE**：同意 - **REFUSE**：拒绝 **[!NOTE]** 当status为**CANCELED**时，不需要传result。

## Returns
- optional: errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/update-to-do-task-status
updated_at: 2026-08-25 09:37:59
