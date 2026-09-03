# 撤销审批实例

doc_id: I34WyV3qpv
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/instance/terminate
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
- request (TerminateProcessInstanceRequestV2, required): 终止审批请求。
- process_instance_id (String, required): 审批实例ID，调用获取审批实例ID列表接口获取。
- is_system (Boolean, required): 是否通过系统操作： - **true**：由系统直接终止 - **false**：由指定的操作者终止
- optional: remark(String), operating_userid(String)

## Returns
- optional: result(Boolean), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 调用成功，撤销审批实例后，审批状态为“已撤销”。 **[!NOTE]** 审批发起15秒内不能撤销审批流程。

source_url: https://open.dingtalk.com/document/development/terminate-a-workflow-by-using-an-instance-id
updated_at: 2026-08-25 09:37:42
