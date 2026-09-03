# 重命名文件或文件夹

doc_id: lVOfF7g6mE
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{dentryId}/rename
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 空间Id，可调用添加空间接口获取id参数值。
- dentryId (String, required): 文件或文件夹Id，可调用获取文件或文件夹列表或根据dentryUuid获取spaceId和dentryId接口获取id参数值。 **[!NOTE]** 存储空间根目录不支持重命名，因此该参数不支持传0。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取unionid参数值。

## Body
- newName (String, required): 文件或文件夹的新名称，命名规则如下： - 头尾不能包含空格，否则会自动去除 - 不能包含特殊字符，包括：制表符、\*、"、<、>、

## Returns
- optional: dentry(Object), id(String), spaceId(String), parentId(String), type(String), name(String), size(Long), path(String), version(Long), status(String), extension(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), properties(Object), readOnly(Boolean), appProperties(Map<String, Array>), value(String), visibility(String), uuid(String), partitionType(String), storageDriver(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/rename-a-file-or-folder
updated_at: 2026-06-02 18:48:57
