# 添加企业待入职员工

doc_id: blLz1gQGVQ
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/addpreentry
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
- param (PreEntryEmployeeAddParam, required): 添加待入职人员。
- name (String, required): 待入职员工姓名。
- mobile (String, required): 待入职员工手机号。 **[!NOTE]** 本接口只能添加非本企业员工（手机号为准），否则报错系统繁忙。
- optional: pre_entry_time(Date), extend_info(String), op_userid(String)

## Returns
- optional: userid(String), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- 待入职员工手机号。 **[!NOTE]** 本接口只能添加非本企业员工（手机号为准），否则报错系统繁忙。
- - 本接口只能添加非本企业员工（手机号为准），否则会提示系统繁忙。

source_url: https://open.dingtalk.com/document/development/add-employees-to-be-hired-through-intelligent-personnel
updated_at: 2026-06-01 09:15:24
