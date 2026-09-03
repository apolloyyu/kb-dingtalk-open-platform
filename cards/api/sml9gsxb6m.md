# 更新实例状态

doc_id: sml9gsxb6m
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/workrecord/update
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
- process_instance_id (String, required): 审批实例ID，由创建实例接口返回。
- status (String, required): 实例状态： - **COMPLETED**：结束审批流 - **TERMINATED**：终止审批流
- result (String, required): 实例结果： - 实例状态是**COMPLETED**，必须设置代表以下含义。 - **agree**：同意 - **refuse**：拒绝 - 实例状态为**TERMINATED，**必须设置代表含义，result取值**agree**和**refuse**均代表撤销审批流。
- optional: request(UpdateProcessInstanceRequest), agentid(Number), cancel_running_task(Boolean)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/to-do-instance-status
updated_at: 2026-08-25 09:37:56
