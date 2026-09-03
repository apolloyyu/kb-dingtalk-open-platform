# 获取组织单元详情

doc_id: fhIjVnofI3
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/edu/collegeContact/depts
api_version: v2-new
app_types: 企业内部应用
permissions: Edu.College.Contact.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- deptId (Long, required): 组织单元ID，根组织单元ID为1。
- optional: language(String)

## Body
- none

## Returns
- optional: success(Boolean), result(Object), deptId(Long), name(String), struId(Long), parentId(Long), sourceIdentifier(String), deptType(String), deptCode(String), createDeptGroup(Boolean), autoAddUser(Boolean), tags(String), fromUnionOrg(Boolean), extension(String), order(Long), deptGroupChatId(String), groupContainSubDept(Boolean), orgDeptOwner(String), deptManagerUseridList(Array of String), outerDept(Boolean), outerPermitDepts(Array of Long), outerPermitUsers(Array of String), userPermits(Array of String), hideDept(Boolean), deptPermits(Array of Long), brief(String), telephone(String), code(String), autoApproveApply(Boolean), empApplyJoinDept(Boolean), hideSceneConfig(Object), chatboxSubtitle(Boolean), nodeList(Boolean), search(Boolean), profile(Boolean), active(Boolean), outerSceneConfig(Object)

## Limits
- 是否本组织单元的员工仅可见员工自己, 为true时，本组织单元员工默认只能看到员工自己。

source_url: https://open.dingtalk.com/document/development/api-getcollegecontactdeptdetail
updated_at: 2026-06-04 14:18:34
