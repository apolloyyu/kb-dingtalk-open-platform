# 获取文件版本列表

doc_id: VDoksyHHbC
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{dentryId}/versions
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.File.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 空间Id，可调用添加空间接口获取id参数值。
- dentryId (String, required): 文件Id，可调用获取文件或文件夹列表或根据dentryUuid获取spaceId和dentryId接口获取id参数值。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取unionid参数值。
- optional: nextToken(String), maxResults(Integer)

## Body
- none

## Returns
- optional: dentries(Array), id(String), spaceId(String), parentId(String), type(String), name(String), size(Long), path(String), version(Long), status(String), extension(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), properties(Object), readOnly(Boolean), appProperties(Map<String, Array>), value(String), visibility(String), uuid(String), partitionType(String), storageDriver(String), nextToken(String)

## Limits
- 每页条目数，默认100，最大100。

source_url: https://open.dingtalk.com/document/development/obtains-a-list-of-file-versions
updated_at: 2026-06-04 19:09:33
