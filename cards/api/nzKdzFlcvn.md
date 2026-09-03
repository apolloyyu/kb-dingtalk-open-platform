# 获取Agoal用户管理员列表

doc_id: nzKdzFlcvn
completeness: full
archived: false
method: GET
endpoint: https://oapi.dingtalk.com/v1.0/agoal/administrators/lists
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: Agoal.UserAdmin.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- optional: requestId(String), success(Boolean), content(Array), OpenUserAdminDTO(OpenUserAdminDTO)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-agoaluseradminlist
updated_at: 2026-06-15 10:38:55
