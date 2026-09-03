# 更新员工花名册信息

doc_id: NRlzyHXJcI
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/v2/update
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_hrm_manager

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- agentid (Number, required): 应用的AgentId。 - 企业内部应用，应用详情页获取应用 AgentId。 - 第三方企业应用，通过获取企业授权信息接口获取agentid传说中。
- param (EmpUpdateByCustomParam, required): 员工信息。
- userid (String, required): 被更新字段信息的员工userid。 **[!NOTE]** 确保该userId是当前本企业内正确的值，否则接口会报错**系统错误**。
- optional: groups(EmpGroupFieldVo[]), sections(EmpListFieldVo[]), section(EmpFieldVo[]), field_code(String), value(String), old_index(Number), group_id(String)

## Returns
- optional: result(Boolean), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/intelligent-personnel-update-employee-file-information
updated_at: 2026-05-29 09:13:56
