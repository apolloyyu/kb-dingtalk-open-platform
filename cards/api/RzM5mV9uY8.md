# 获取审计协议签署人员信息

doc_id: RzM5mV9uY8
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/exclusive/audits/users
api_version: v2-new
app_types: 第三方企业应用
permissions: Custom.Audit.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- pageNumber (Long, required): 页码，首次传1。
- signStatus (Long, required): 签署状态。 - 0：未签署 - 1：已签署
- pageSize (Long, required): 每页数量，最大值2000。

## Body
- none

## Returns
- optional: auditSignedDetailDTOList(Array), name(String), staffId(String), title(String), phone(String), email(String), deptName(String), roles(String), currentPage(Long), pageSize(Long), total(Long)

## Limits
- 每页数量，最大值2000。

source_url: https://open.dingtalk.com/document/development/obtains-the-information-about-the-persons-who-sign-the-audit-1
updated_at: 2026-06-04 19:09:53
