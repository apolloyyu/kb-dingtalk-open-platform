# 获取空间下所有文件或文件夹列表

doc_id: suWY8tbJ4a
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/listAll
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.File.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 空间ID，调用添加空间接口获取id参数值。

## Query params
- unionId (String, required): 操作人的unionId，可调用查询用户详情接口获取。

## Body
- optional: option(Object), nextToken(String), maxResults(Integer), order(String), withThumbnail(Boolean)

## Returns
- optional: dentries(Array), id(String), spaceId(String), parentId(String), type(String), name(String), size(Long), path(String), version(Long), status(String), extension(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), properties(Object), readOnly(Boolean), appProperties(Map<String, Array>), value(String), visibility(String), uuid(String), partitionType(String), storageDriver(String), thumbnail(Object), width(Integer), height(Integer), url(String), nextToken(String)

## Limits
- 每页条目数，默认值50，最大值50。
- 属性可见性。 - **PUBLIC**：所有应用都可见 - **PRIVATE**：仅限当前应用可见

source_url: https://open.dingtalk.com/document/development/get-a-list-of-all-files-or-folders-under-a
updated_at: 2026-06-04 10:03:15
