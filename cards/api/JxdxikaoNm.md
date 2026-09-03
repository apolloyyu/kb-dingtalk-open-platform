# 恢复文件历史版本

doc_id: JxdxikaoNm
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{dentryId}/versions/{version}/revert
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 空间Id，可调用添加空间接口获取id参数值。
- dentryId (String, required): 文件Id，可调用获取文件或文件夹列表或根据dentryUuid获取spaceId和dentryId接口获取id参数值。
- version (Long, required): 需要恢复的文件版本号，最小值0。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取unionid参数值。

## Body
- none

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/restore-previous-versions-of-files
updated_at: 2026-06-02 18:49:00
