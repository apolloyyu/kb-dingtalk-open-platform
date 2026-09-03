# 创建协作空间

doc_id: 6CJtEnjAtr
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/teamSphere/users/{userId}/projects
api_version: v2-new
app_types: 第三方企业应用
permissions: TeamSphere.Project.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。

## Query params
- optional: organizationId(String)

## Body
- optional: name(String)

## Returns
- optional: result(Object), id(String), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-createprojectv3
updated_at: 2026-06-02 19:46:13
