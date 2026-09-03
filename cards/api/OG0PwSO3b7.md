# 解除关联组织

doc_id: OG0PwSO3b7
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/contact/cooperateCorps/separate
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Contact.CooperateCorp.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取企业accessToken(应用商店应用)接口获取。

## Path params
- none

## Query params
- none

## Body
- attachDeptId (Long, required): 伙伴组织在上下游组织内的部门ID，上下游组织通过获取部门列表接口获取dept_id参数值。

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/disassociate-an-organization
updated_at: 2026-06-08 09:30:55
