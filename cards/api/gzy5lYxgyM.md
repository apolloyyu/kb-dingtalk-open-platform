# 获取文件下载信息

doc_id: gzy5lYxgyM
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{dentryId}/downloadInfos/query
api_version: v2-new
app_types: 企业内部应用
permissions: Storage.DownloadInfo.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- spaceId (String, required): 空间Id，可调用添加空间接口获取id参数值。
- dentryId (String, required): 文件Id，调用获取文件或文件夹列表或根据 dentryUuid 获取 spaceId接口获取id参数值。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取。

## Body
- optional: option(Object), version(Long), preferIntranet(Boolean)

## Returns
- optional: protocol(String), headerSignatureInfo(Object), resourceUrls(Array of String), headers(Map<String, String>), expirationSeconds(Integer), region(String), internalResourceUrls(Array of String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-download-information-about-a-file
updated_at: 2026-06-08 12:02:08
