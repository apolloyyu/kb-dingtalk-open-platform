# 设置伙伴组织在上下游组织内的可见范围

doc_id: NTOntm4lJv
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/contact/cooperateCorps/branchVisibleSettings
api_version: v2-new
app_types: 第三方企业应用
permissions: Contact.CooperateCorp.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 **[!NOTE]** 调用本接口，需要使用上下游组织的访问凭证，不能使用所属组织的访问凭证。

## Path params
- none

## Query params
- none

## Body
- branchCorpId (String, required): 伙伴组织的企业corpId，详情参见CorpId。
- type (Long, required): 设置可见性类型，取值： - **0**：在上下游组织通讯录隐藏伙伴组织，即其它伙伴组织都看不到，额外设置的分支和部门可以看到。 - **1**：仅可见伙伴组织自己，即只能看到自己企业加入的成员，额外设置分支和部门可以被看到。
- open (Boolean, required): 是否开启，取值： - **true**：开启 - **false**：关闭
- optional: visibleBranchCorpIds(Array of String), visibleDeptIds(Array of Long)

## Returns
- none

## Limits
- 设置可见性类型，取值： - **0**：在上下游组织通讯录隐藏伙伴组织，即其它伙伴组织都看不到，额外设置的分支和部门可以看到。 - **1**：仅可见伙伴组织自己，即只能看到自己企业加入的成员，额外设置分支和部门可以被看到。

source_url: https://open.dingtalk.com/document/development/set-the-visible-range-of-the-branch-in-the-group-1
updated_at: 2026-06-01 16:31:55
