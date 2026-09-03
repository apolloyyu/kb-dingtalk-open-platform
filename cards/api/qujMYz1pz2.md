# 获取空间列表

doc_id: qujMYz1pz2
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/drive/spaces
api_version: v2-new
app_types: 第三方企业应用
permissions: Drive.Space.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- unionId (String, required): 用户unionId，可调用查询用户详情接口获取。
- spaceType (String, required): 空间类型。 - **org**：企业空间
- maxResults (Integer, required): 分页大小。
- optional: nextToken(String)

## Body
- none

## Returns
- optional: spaces(Array), spaceId(String), spaceName(String), spaceType(String), quota(Long), usedQuota(Long), permissionMode(String), createTime(String), modifyTime(String), nextToken(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-a-space-list
updated_at: 2026-06-04 19:09:26
