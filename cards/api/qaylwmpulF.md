# 更新组织单元

doc_id: qaylwmpulF
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/edu/collegeContact/depts
api_version: v2-new
app_types: 企业内部应用
permissions: Edu.College.Contact.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- deptId (Long, required): 组织单元ID。
- optional: parentId(Long), deptType(String), deptCode(String), outerDept(Boolean), hideDept(Boolean), createDeptGroup(Boolean), order(Long), name(String), sourceIdentifier(String), deptPermits(Array of Long), userPermits(Array of String), outerPermitUsers(Array of String), outerPermitDepts(Array of Long), outerDeptOnlySelf(Boolean), autoApproveApply(Boolean), empApplyJoinDept(Boolean), brief(String), telephone(String), code(String), hideSceneConfig(Object), active(Boolean), profile(Boolean), search(Boolean), nodeList(Boolean), chatboxSubtitle(Boolean), outerSceneConfig(Object), extension(Map<String, String>), language(String), autoAddUser(Boolean), deptManagerUseridList(Array of String), groupContainSubDept(Boolean), groupContainOuterDept(Boolean), groupContainHiddenDept(Boolean), orgDeptOwner(String), forceUpdateFields(Array of String)

## Returns
- optional: success(Boolean)

## Limits
- 限制本组织单元成员查看通讯录，限制开启后，本组织单元成员只能看到限定范围内的通讯录。true 表示限制开启。
- 组织单元名称，长度限制为1~100个字符，不允许包含字符‘-’‘，’以及‘,’。
- 是否只能看到所在组织单元及下级组织单元通讯录。

source_url: https://open.dingtalk.com/document/development/api-updatecollegecontactdept
updated_at: 2026-06-04 14:18:34
