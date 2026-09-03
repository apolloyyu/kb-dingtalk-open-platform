# 删除文件或文件夹

doc_id: 7L5XgsBmT6
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{dentryId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 空间Id，可调用添加空间接口获取id参数值。
- dentryId (String, required): 需要被删除的文件或文件夹Id，可调用获取文件或文件夹列表或根据dentryUuid获取spaceId和dentryId接口获取id参数值。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取unionid参数值。
- optional: toRecycleBin(Boolean)

## Body
- none

## Returns
- optional: async(Boolean), taskId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-a-file-or-folder
updated_at: 2026-06-02 18:48:58
