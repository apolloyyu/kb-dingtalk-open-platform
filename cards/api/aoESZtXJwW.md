# 移动文件或文件夹

doc_id: aoESZtXJwW
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{dentryId}/move
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 文件或文件夹所在的源空间Id，可调用添加空间接口获取id参数值。
- dentryId (String, required): 需要被移动的文件或文件夹Id，可调用获取文件或文件夹列表或根据dentryUuid获取spaceId和dentryId接口获取id参数值。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取unionid参数值。

## Body
- targetSpaceId (String, required): 需要存放的目标空间Id，可调用添加空间接口获取id参数值。
- targetFolderId (String, required): 需要存放的位置父目录Id，可通过获取文件或文件夹列表接口获取id参数值。 **[!NOTE]** 根目录时，该参数为0。
- optional: option(Object), conflictStrategy(String), presevePermissions(Boolean)

## Returns
- optional: dentry(Object), id(String), spaceId(String), parentId(String), type(String), name(String), size(Long), path(String), version(Long), status(String), extension(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), properties(Object), readOnly(Boolean), appProperties(Map<String, Array>), value(String), visibility(String), uuid(String), partitionType(String), storageDriver(String), async(Boolean), taskId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/move-a-file-or-folder
updated_at: 2026-06-02 18:48:55
