# 获取用户所在的行业角色信息

doc_id: xQoGxEOxs7
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/resident/users/industryRoles
api_version: v2-new
app_types: 第三方企业应用
permissions: Village.Contact.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- userId (String, required): 用户userId，可通过调用获取部门用户userid列表接口获取。

## Body
- none

## Returns
- optional: roleList(Array), roleId(Long), roleName(String), tagCode(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-industry-role-information-of-the-user
updated_at: 2026-06-05 15:32:42
