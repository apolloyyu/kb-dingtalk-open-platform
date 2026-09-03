# 批量复制文件或文件夹

doc_id: ZIxDdNrQW0
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/batchCopy
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 源文件或文件夹所在的空间ID，可调用添加空间接口获取id参数值。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取unionid参数值。

## Body
- targetSpaceId (String, required): 目标文件或文件夹所在的空间ID，可调用添加空间接口获取id参数值。
- targetFolderId (String, required): 目标文件夹ID， 根目录ID值为0，可通过获取文件或文件夹列表接口获取id参数值。
- dentryIds (Array of String, required): 源文件或文件夹的ID列表，最多3个，可调用获取文件或文件夹列表或根据dentryUuid获取spaceId和dentryId接口获取id参数值。
- optional: option(Object), conflictStrategy(String)

## Returns
- optional: resultItems(Array), spaceId(String), dentryId(String), async(Boolean), success(Boolean), errorCode(String), taskId(String), targetSpaceId(String), targetDentryId(String)

## Limits
- 源文件或文件夹的ID列表，最多3个，可调用获取文件或文件夹列表或根据dentryUuid获取spaceId和dentryId接口获取id参数值。

source_url: https://open.dingtalk.com/document/development/copy-files-or-folders-in-bulk
updated_at: 2026-06-02 18:48:55
