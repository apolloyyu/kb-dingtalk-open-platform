# 批量获取文件或文件夹信息

doc_id: QJopbaOGJh
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.File.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 空间Id，可调用添加空间接口获取id参数值。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取unionid参数值。

## Body
- dentryIds (Array of String, required): 文件或文件夹的ID列表，最多30个，可调用获取文件或文件夹列表或根据dentryUuid获取spaceId和dentryId接口获取id参数值。
- optional: option(Object), appIdsForAppProperties(Array of String), withThumbnail(Boolean)

## Returns
- optional: resultItems(Array), spaceId(String), dentryId(String), success(Boolean), errorCode(String), dentry(Object), id(String), parentId(String), type(String), name(String), size(Long), path(String), version(Long), status(String), extension(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), properties(Object), readOnly(Boolean), appProperties(Map<String, Array>), value(String), visibility(String), uuid(String), partitionType(String), storageDriver(String), thumbnail(Object), width(Integer), height(Integer), url(String)

## Limits
- 文件或文件夹的ID列表，最多30个，可调用获取文件或文件夹列表或根据dentryUuid获取spaceId和dentryId接口获取id参数值。
- 指定应用ID列表，最多20个，可通过获取空间信息接口获取ownerId参数值。 - 如果传该参数，会返回该文件或文件夹对应应用的属性。 - 如果不传该参数，会返回该文件或文件夹的所有应用的属性。
- 属性可见性。 - **PUBLIC**：所有应用都可见 - **PRIVATE**：仅限当前应用可见

source_url: https://open.dingtalk.com/document/development/get-file-or-folder-information-in-bulk
updated_at: 2026-06-04 19:09:34
