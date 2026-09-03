# 同意或拒绝审批任务

doc_id: uC2iCBdMvY
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/instance/execute
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，可通过获取企业内部应用的access_token接口获取。

## Body
- process_instance_id (String, required): 审批实例id，调用获取审批实例ID列表接口获取。
- result (String, required): 审批操作，取值。 - **agree**：同意 - **refuse**：拒绝
- actioner_userid (String, required): 操作人userid，调用获取单个审批实例详情接口获取。
- task_id (Number, required): 任务节点id，调用获取单个审批实例详情接口获取。
- optional: request(ExecuteTaskRequest), remark(String), file(File), attachments(Attachment[]), space_id(String), file_size(String), file_id(String), file_name(String), file_type(String), photos(String[])

## Returns
- optional: result(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/execute-approval-operation-with-attachment
updated_at: 2026-08-25 09:37:51
