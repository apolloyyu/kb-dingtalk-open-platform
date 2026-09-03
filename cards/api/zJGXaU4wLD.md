# 获取当前企业所有可管理的表单

doc_id: zJGXaU4wLD
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/template/manage/get
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
- userid (String, required): 用户的userid。 **[!NOTE]** userid对应的人员必须拥有该企业OA审批的权限。

## Returns
- optional: result(ProcessSimpleVO[]), icon_name(String), flow_title(String), process_code(String), gmt_modified(Date), attendance_type(Number), icon_url(String), is_new_process(Boolean), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 调用本接口，获取在当前企业，该用户可以管理的表单。比如，用户可以管理“审批模板测试”，调用该接口，只能获取到“审批模板测试”表单的信息。

source_url: https://open.dingtalk.com/document/development/obtains-the-information-about-all-manageable-templates-of-the-current
updated_at: 2026-08-25 09:37:47
