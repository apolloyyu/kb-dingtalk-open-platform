# 设置分支组织在主干组织内的可见范围

doc_id: 64QvR2dfZK
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/contact/cooperateCorps/branchVisibleSettings
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Contact.CooperateCorp.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取企业accessToken(应用商店应用)接口获取。 **[!NOTE]** 调用本接口，需要使用**主干组织**的访问凭证，不能使用分支组织的访问凭证。

## Path params
- none

## Query params
- none

## Body
- branchCorpId (String, required): 伙伴组织的企业corpId，详情参见基础概念。
- type (Long, required): 设置可见性类型，取值： - **0**：在主干组织通讯录隐藏分支组织。 - **1**：仅可见分支组织自己。
- open (Boolean, required): 是否开启，取值： - **true**：开启 - **false**：关闭
- optional: visibleBranchCorpIds(Array of String), visibleDeptIds(Array of Long)

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/sets-the-visible-range-of-branch-organizations-within-the-group
updated_at: 2026-05-26 09:01:03
