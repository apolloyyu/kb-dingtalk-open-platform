# 批量获取文件缩略图

doc_id: mS8pSXRxNj
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/thumbnails/query
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Storage.File.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 空间ID，调用添加空间接口获取id参数值。

## Query params
- unionId (String, required): 操作人的unionId，可调用查询用户详情接口获取。

## Body
- dentryIds (Array of String, required): 文件ID，最大值30，调用获取文件或文件夹列表接口获取id参数值。

## Returns
- optional: resultItems(Array), spaceId(String), dentryId(String), success(Boolean), errorCode(String), thumbnail(Object), width(Integer), height(Integer), url(String)

## Limits
- 文件ID，最大值30，调用获取文件或文件夹列表接口获取id参数值。

source_url: https://open.dingtalk.com/document/development/get-file-thumbnails-in-bulk
updated_at: 2026-06-15 11:26:25
