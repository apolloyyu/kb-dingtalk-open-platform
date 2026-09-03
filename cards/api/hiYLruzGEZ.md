# 更新分支组织在主干组织内的属性信息

doc_id: hiYLruzGEZ
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/contact/cooperateCorps/branchAttributes
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Contact.CooperateCorp.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取企业accessToken(应用商店应用)接口获取。 **[!NOTE]** 调用本接口，需要使用**主干组织**的访问凭证，不能使用所属组织的访问凭证。

## Path params
- none

## Query params
- none

## Body
- branchCorpId (String, required): 分支组织的企业ID，可调用获取分支组织列表接口获取union_corpid参数值。
- unionRootName (String, required): 分支组织在主干组织内的别名。
- linkDeptId (Long, required): 挂载节点部门ID，如果是根部门，需要传-1，主干组织调用获取部门列表接口获取dept_id参数值。

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/updates-the-property-information-of-a-branch-organization-in-a
updated_at: 2026-05-26 09:01:03
