# 获取Teambition项目企业ID

doc_id: 92YBLm9XzG
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/project/teambition/organizations
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_project

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optUserId (String, required): 操作者userId。

## Body
- none

## Returns
- optional: result(Object), tbOrganizationId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-teambition-enterprise-id
updated_at: 2026-06-04 19:11:49
