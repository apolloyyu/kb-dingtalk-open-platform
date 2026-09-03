# 获取组织单元支持的部门类型

doc_id: QI199g9bIH
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/edu/collegeContact/configs/deptTypes
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
- optional: success(Boolean), result(Array), deptType(String), name(String), userDef(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-listcollegecontactdepttypeconfig
updated_at: 2026-06-04 14:18:32
