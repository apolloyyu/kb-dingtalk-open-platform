# 修改伙伴类型可见性

doc_id: 8k4drbM4IP
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/exclusive/partnerDepartments/visibilityPartners
api_version: v2-new
app_types: 第三方企业应用
permissions: Partner.Department.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- labelId (Long, required): 标签ID。
- optional: deptIds(Array of Long), userIds(Array of String)

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/modify-partner-type-visibility
updated_at: 2026-06-04 19:09:56
