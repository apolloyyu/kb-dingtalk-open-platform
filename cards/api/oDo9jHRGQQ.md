# 获取员工花名册字段信息

doc_id: oDo9jHRGQQ
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/list
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端接口的授权凭证，可通过获取企业内部应用的access_token接口获取。

## Body
- userid_list (String, required): 员工userid列表，最大列表长度为50。
- optional: field_filter_list(String)

## Returns
- optional: result(EmpFieldInfoVO[]), userid(String), field_list(EmpFieldVO[]), group_id(String), value(String), field_code(String), field_name(String), label(String), partner(Boolean), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- 员工userid列表，最大列表长度为50。
- 需要获取的花名册字段列表，最大列表长度为20。 **[!NOTE]** 不传入该参数时，企业可获取所有字段信息。

source_url: https://open.dingtalk.com/document/development/obtain-employee-roster-field-information-in-batches
updated_at: 2026-08-25 09:39:06
