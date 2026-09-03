# 删除文件或文件夹的应用属性

doc_id: xeeBp3VRYK
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{dentryId}/appProperties/remove
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (Long, required): 空间Id，调用添加空间接口获取id参数值。
- dentryId (Long, required): 文件或文件夹的id，可调用获取文件或文件夹列表或根据dentryUuid获取spaceId和dentryId接口获取id参数值。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取unionid参数值。

## Body
- propertyNames (Array of String, required): 文件或文件夹的应用属性名称列表，最大值3。

## Returns
- optional: success(Boolean)

## Limits
- 文件或文件夹的应用属性名称列表，最大值3。

source_url: https://open.dingtalk.com/document/development/delete-file-app-attribute
updated_at: 2026-06-04 19:09:35
