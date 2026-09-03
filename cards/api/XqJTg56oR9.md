# 更新伙伴组织在上下游组织内的属性信息

doc_id: XqJTg56oR9
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/contact/cooperateCorps/branchAttributes
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
- branchCorpId (String, required): 伙伴组织的企业ID，可调用获取已加入或正在申请加入上下游组织的组织和个人信息获取dept_id参数值。
- unionRootName (String, required): 伙伴组织在上下游组织内的别名。
- linkDeptId (Long, required): 挂载节点部门ID，如果是根部门，需要传-1，可调用获取已加入或正在申请加入上下游组织的组织和个人信息获取dept_id参数值。

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/update-properties-of-branches-in-alibaba-group-1
updated_at: 2026-06-01 16:31:54
