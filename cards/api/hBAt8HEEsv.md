# 知识库下载文件

doc_id: hBAt8HEEsv
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
- spaceId (String, required): 空间Id，可通过获取节点列表接口获取知识库节点的 `dentryUuid`，再调用根据 dentryUuid 获取 spaceId接口获取 `spaceId`。
- dentryId (String, required): 文件Id，可通过获取节点列表接口获取知识库节点的 `dentryUuid`，再调用根据 dentryUuid 获取 spaceId接口获取 `dentryId`。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取。

## Body
- optional: option(Object), version(Long), preferIntranet(Boolean)

## Returns
- optional: protocol(String), headerSignatureInfo(Object), resourceUrls(Array of String), headers(Map<String, String>), expirationSeconds(Integer), region(String), internalResourceUrls(Array of String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/knowledge-base-download-file
updated_at: 2026-06-03 09:48:34
