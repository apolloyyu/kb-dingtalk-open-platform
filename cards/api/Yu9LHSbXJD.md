# 批量通过伙伴组织的加入申请

doc_id: Yu9LHSbXJD
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/contact/cooperateCorps/unionApplications/approve
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
- optional: branchCorpId(String), unionRootName(String), linkDeptId(Long)

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/apply-for-batch-addition-through-upstream-and-downstream-organizations
updated_at: 2026-06-01 16:31:54
