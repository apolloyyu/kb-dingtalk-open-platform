# 解除关联组织

doc_id: PknyHppNIK
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/contact/cooperateCorps/separate
api_version: v2-new
app_types: 第三方企业应用
permissions: Contact.CooperateCorp.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- attachDeptId (Long, required): 伙伴组织在上下游组织内的部门ID，上下游组织通过获取部门列表接口获取dept_id参数值。

## Returns
- optional: result(Boolean)

## Limits
- 调用本接口，解除“测试演示组织”、“体验组织”上下游组织关联，效果同下图产品功能解除上下游组织关联。解除关联关系前”测试演示组织“只有1个关联组织，解除关联后，解除后”体验组织“不在”测试演示组织“的关联组织列表中，关联组织列表为空。

source_url: https://open.dingtalk.com/document/development/disassociate-upstream-and-downstream-organizations
updated_at: 2026-06-02 09:24:47
