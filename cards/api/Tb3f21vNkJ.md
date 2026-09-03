# 根据userId查询人员的标签信息

doc_id: Tb3f21vNkJ
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/exclusive/partners/users/{userId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Partner.Department.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 用户userId，可调用查询用户详情接口获取。

## Query params
- none

## Body
- none

## Returns
- optional: partnerDeptList(Array), title(String), value(String), memberCount(Long), partnerNum(String), partnerLabelModelLevel1(Object), labelId(Long), labelname(String), partnerLabelList(Array), id(Long), name(String), userId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/you-can-call-this-operation-to-retrieve-the-user-tag
updated_at: 2026-06-04 19:09:57
