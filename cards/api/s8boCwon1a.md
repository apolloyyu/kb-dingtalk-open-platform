# 获取单个审批实例详情

doc_id: s8boCwon1a
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/processinstance/get
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- process_instance_id (String, required): 审批实例ID - 企业内部应用可通过获取审批实例ID列表接口获取。 - 钉钉三方企业应用可以通过推送的审批事件中获取，参考biz_type=22。

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), process_instance(ProcessInstanceTopVo), title(String), create_time(Date), finish_time(Date), originator_userid(String), originator_dept_id(String), status(String), approver_userids(String[]), cc_userids(String[]), result(String), business_id(String), operation_records(OperationRecordsVo[]), userid(String), date(Date), operation_type(String), operation_result(String), remark(String), attachments(Attachment[]), file_name(String), file_size(String), file_id(String), file_type(String), tasks(TaskTopVo[]), task_status(String), task_result(String), taskid(String), url(String), originator_dept_name(String), biz_action(String), attached_process_instance_ids(String[]), form_component_values(FormComponentValueVo[]), name(String), value(String), ext_value(String), id(String), component_type(String), main_process_instance_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-details-single-approval-instance
updated_at: 2026-08-25 09:37:41
