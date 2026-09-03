# 根据spaceId获取指定空间信息

doc_id: 7LfWf0G09M
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/drive/managements/spaces/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Drive.SpaceManage.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可通过以下方式获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- spaceIds (Array of String, required): 空间ID列表，最多允许传入30个，可调用获取空间列表接口获取。
- unionId (String, required): 用户unionId，可调用查询用户详情接口获取。

## Returns
- optional: spaces(Array), spaceId(String), spaceName(String), spaceType(String), quota(Long), usedQuota(Long), permissionMode(String), createTime(String), modifyTime(String)

## Limits
- 空间ID列表，最多允许传入30个，可调用获取空间列表接口获取。

source_url: https://open.dingtalk.com/document/development/retrieves-the-space-list-on-the-management-side
updated_at: 2026-06-02 18:46:45
