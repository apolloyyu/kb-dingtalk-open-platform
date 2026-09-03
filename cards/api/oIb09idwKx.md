# 获取文件上传信息

doc_id: oIb09idwKx
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/storage/spaces/files/{parentDentryUuid}/uploadInfos/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.UploadInfo.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- parentDentryUuid (String, required): 父节点dentryUuid，可调用搜索文件或获取 dentryUuid 信息接口，获取返回参数`dentryUuid`字段。 如果是空间根目录, 填空间根目录的dentryUuid。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取。

## Body
- protocol (String, required): 通过指定上传协议返回不同协议上传所需要的信息。 - **HEADER_SIGNATURE**：Header加签
- optional: option(Object), storageDriver(String), preCheckParam(Object), size(Long), name(String), preferRegion(String), preferIntranet(Boolean)

## Returns
- optional: uploadKey(String), storageDriver(String), protocol(String), headerSignatureInfo(Object), resourceUrls(Array of String), headers(Map<String, String>), expirationSeconds(Integer), region(String), internalResourceUrls(Array of String)

## Limits
- 请求头，最大size：20。

source_url: https://open.dingtalk.com/document/development/obtain-file-upload-informations
updated_at: 2026-06-04 19:09:36
