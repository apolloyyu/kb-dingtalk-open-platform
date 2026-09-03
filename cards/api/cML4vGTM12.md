# 获取员工花名册字段信息

doc_id: cML4vGTM12
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/v2/list
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- userid_list (String, required): 员工的userid列表，多个userid之间使用逗号分隔，一次最多支持传100个值。
- agentid (Number, required): 应用的AgentId。 - 企业内部应用，应用详情页获取应用 AgentId。 - 第三方企业应用可以调用获取企业授权信息接口获取agentid参数值。
- optional: field_filter_list(String)

## Returns
- optional: result(EmpRosterFieldVo[]), corp_id(String), field_data_list(EmpFieldDataVo[]), field_name(String), field_code(String), group_id(String), field_value_list(FieldValueVo[]), item_index(Number), label(String), value(String), userid(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 员工的userid列表，多个userid之间使用逗号分隔，一次最多支持传100个值。
- 需要获取的花名册字段field_code值列表，多个字段之间使用逗号分隔，一次最多支持传100个值。 **[!NOTE]** - 该参数不传时，获取全部字段信息。 - 查询字段越少，RT越低，建议按需查询。 - 企业内部应用： - 查看花名册自定义字段业务code中field_code字段。 - 调用获取花名册元数据接口获取field_code参数值。 - 第三方企业应用，调用查询花名册中有权限的字段列表接口获取field_code参数值。

source_url: https://open.dingtalk.com/document/development/intelligent-personnel-obtain-employee-roster-information
updated_at: 2026-08-25 09:39:08
