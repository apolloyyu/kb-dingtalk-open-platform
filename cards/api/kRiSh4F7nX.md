# 撤销员工获得的荣誉勋章

doc_id: kRiSh4F7nX
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/orgCulture/honors/{honorId}/recall
api_version: v2-new
app_types: 第三方企业应用
permissions: OrgCulture.Honor.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- honorId (String, required): 荣誉勋章id，可通过调用查询员工已获得的组织荣誉接口，获取荣誉勋章`honorId`字段。

## Query params
- none

## Body
- userId (String, required): 撤销荣誉勋章的员工userId。

## Returns
- optional: success(Boolean), result(Object), honorId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/revoke-an-employee-s-medal-of-honor
updated_at: 2026-06-02 19:43:43
