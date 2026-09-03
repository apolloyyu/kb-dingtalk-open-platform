# 获取行政组织架构部门详情

doc_id: MVdet4sX0C
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/edu/collegeContact/depts/structures/standards
api_version: v2-new
app_types: 企业内部应用
permissions: Edu.College.Contact.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: language(String)

## Body
- none

## Returns
- optional: success(Boolean), result(Object), struId(Long), teacherDeptId(Long), studentDeptId(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getcollegecontactstandardstrudeptdetail
updated_at: 2026-06-04 19:11:31
