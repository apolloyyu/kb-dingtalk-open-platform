# 更新部门

doc_id: D1kZuS555D
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/department/update
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
- id (Number, required): 部门ID，可调用获取部门列表接口获取。
- optional: orgDeptOwner(String), outerPermitUsers(String), outerPermitDepts(String), outerDept(Boolean), deptHiding(Boolean), deptManagerUseridList(String), createDeptGroup(Boolean), autoAddUser(Boolean), autoApproveApply(Boolean), order(String), parentid(String), lang(String), name(String), sourceIdentifier(String), userPermits(String), deptPermits(String), outerDeptOnlySelf(Boolean), groupContainSubDept(Boolean), groupContainOuterDept(Boolean), groupContainHiddenDept(Boolean), ext(String)

## Returns
- optional: errcode(Number), errmsg(String), id(Number)

## Limits
- 是否限制本部门成员查看通讯录： - **true**：开启限制，开启后本部门成员只能看到限定范围内的通讯录 - **false**：不限制
- 部门名称。 长度限制为1~64个字符，不允许包含字符"-"","以及","。
- 是否只能看到所在部门及下级部门通讯录： - **true**：表示只能看到所在部门及下级部门通讯录 - **false**：不能查看所在部门及下级部门通讯录 **[!NOTE]** outerDept为true时，可以配置该字段。

source_url: https://open.dingtalk.com/document/development/update-a-department
updated_at: 2026-08-25 09:37:04
