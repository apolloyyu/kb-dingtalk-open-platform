# 修改用户成员类型

doc_id: OnMrFTEELI
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/edu/collegeContact/empTypes/change
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
- userid (String, required): 员工唯一标识ID（不可修改），企业内必须唯一。
- empType (String, required): 员工的成员类型： - college_teacher：教职工 - college_student：学生

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-updatecollegeuseremptype
updated_at: 2026-06-04 14:18:36
