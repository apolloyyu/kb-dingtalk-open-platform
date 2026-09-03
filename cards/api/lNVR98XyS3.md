# 获取文件分片上传信息

doc_id: lNVR98XyS3
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/files/multiPartUploadInfos/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.UploadInfo.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取。

## Body
- uploadKey (String, required): 上传唯一标识，调用初始化文件分片上传接口，获取上传标识uploadKey。
- partNumbers (Array of Integer, required): 每片文件的Id，文件的分片数量最大值10000，每片文件大小限制范围是100KB~5GB，最多传30。 每片文件的Id，由开发者指定，本接口会返回每片文件的上传地址和headers等信息。 示例：[1,2,3,4,5]
- optional: option(Object), preferIntranet(Boolean)

## Returns
- optional: multipartHeaderSignatureInfos(Array), partNumber(Integer), headerSignatureInfo(Object), resourceUrls(Array of String), headers(Map<String, String>), expirationSeconds(Integer), region(String), internalResourceUrls(Array of String)

## Limits
- 每片文件的Id，文件的分片数量最大值10000，每片文件大小限制范围是100KB~5GB，最多传30。 每片文件的Id，由开发者指定，本接口会返回每片文件的上传地址和headers等信息。 示例：[1,2,3,4,5]
- 多个上传URL，最大值10，前面的url优先。

source_url: https://open.dingtalk.com/document/development/obtains-the-information-about-multipart-uploads-of-an-object
updated_at: 2026-06-04 19:09:38
