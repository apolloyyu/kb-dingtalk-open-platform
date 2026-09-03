# 获取子组织单元列表

doc_id: aQxAhLaZtc
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/edu/collegeContact/subDepts
api_version: v2-new
app_types: 企业内部应用
permissions: Edu.College.Contact.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- deptId (Long, required): 父组织单元ID，根组织单元ID为1,只支持查询下一级子组织单元，不支持查询多级子组织单元。
- optional: language(String)

## Body
- none

## Returns
- optional: success(Boolean), result(Array), deptId(Long), name(String), struId(Long), parentId(Long), sourceIdentifier(String), deptType(String), deptCode(String), createDeptGroup(Boolean), autoAddUser(Boolean), tags(String), fromUnionOrg(Boolean), extension(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-listcollegecontactsubdepts
updated_at: 2026-06-04 14:18:33
