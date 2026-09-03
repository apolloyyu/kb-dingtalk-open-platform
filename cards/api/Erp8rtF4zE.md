# 获取上下级组织分支授权的数据

doc_id: Erp8rtF4zE
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/contact/branchAuthDatas/search
api_version: v2-new
app_types: 企业内部应用
permissions: Contact.UnionBranchData.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- branchCorpId (String, required): 分支组织的corpId，可通过获取分支组织列表接口获取union_corpid参数值。
- code (String, required): 子类数据编码，详情可参考授权数据编码及入参条件概览。

## Body
- none

## Returns
- optional: result(Array), fieldCode(String), fieldName(String), fieldValue(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/data-authorized-by-a-branch-of-an-associated-organization
updated_at: 2026-06-02 09:24:48
