# 获取文件或文件夹信息

doc_id: EJ3viBi5oJ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{dentryId}/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.File.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 空间Id，可调用添加空间接口获取id参数值。
- dentryId (String, required): 文件或文件夹Id，可调用获取文件或文件夹列表或根据dentryUuid获取spaceId和dentryId接口获取id参数值。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取unionid参数值。

## Body
- optional: option(Object), appIdsForAppProperties(Array of String), withThumbnail(Boolean)

## Returns
- optional: dentry(Object), id(String), spaceId(String), parentId(String), type(String), name(String), size(Long), path(String), version(Long), status(String), extension(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), properties(Object), readOnly(Boolean), appProperties(Map<String, Array>), value(String), visibility(String), uuid(String), partitionType(String), storageDriver(String), thumbnail(Object), width(Integer), height(Integer), url(String)

## Limits
- 通过指定空间ownerId列表，返回对应的可见属性，最多20个。 - ownerType为APP时，ownerId是应用标识。 - ownerType为USER时，ownerId是创建者unionId。
- 属性可见性： - **PUBLIC**：所有应用都可见 - **PRIVATE**：仅限当前应用可见

source_url: https://open.dingtalk.com/document/development/obtain-file-or-folder-information
updated_at: 2026-06-04 19:09:33
