# 获取部门详情

doc_id: 2X9se7Ed9v
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/department/get
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。
- id (String, required): 部门ID，可调用获取部门列表接口获取。
- optional: lang(String)

## Body
- none

## Returns
- optional: errcode(Number), errmsg(String), id(Number), name(String), order(Number), parentid(Number), sourceIdentifier(String), createDeptGroup(Boolean), autoAddUser(Boolean), autoApproveApply(Boolean), groupContainSubDept(Boolean), orgDeptOwner(String), deptGroupChatId(String), deptManagerUseridList(String), outerDept(Boolean), outerPermitUsers(String), outerPermitDepts(String), deptHiding(Boolean), deptPermits(String), userPermits(String)

## Limits
- 是否限制本部门成员查看通讯录： - **true**：开启限制，开启后本部门成员只能看到限定范围内的通讯录 - **false**：不限制
- 当**outerDept**为**true**时（即开启本部门成员只能看到限定范围内的通讯录），配置的部门员工可见部门列表。

source_url: https://open.dingtalk.com/document/development/queries-department-details
updated_at: 2026-08-25 09:36:58
