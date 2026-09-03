# 初始化文件分片上传

doc_id: psKPRnVdgW
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/files/multiPartUploadInfos/init
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.UploadInfo.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 空间Id，可调用添加空间接口获取id参数值。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取。

## Body
- optional: option(Object), storageDriver(String), preCheckParam(Object), md5(String), size(Long), parentId(String), name(String), preferRegion(String)

## Returns
- optional: uploadKey(String), storageDriver(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/initialize-a-multipart-upload-object
updated_at: 2026-06-04 19:09:38
