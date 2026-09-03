# 获取智能招聘文件上传信息

doc_id: vUbq1ngLWv
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/ats/files/uploadInfos
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_recruitment_plugin

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- fileName (String, required): 文件名称。
- fileSize (Long, required): 文件大小，单位字节。 主要用于预检查钉盘剩余空间。
- md5 (String, required): 文件MD5摘要，示例：`DigestUtils.md5Hex(new FileInputStream("/Users/xxxx/Desktop/111.doc")`
- optional: bizCode(String), opUserId(String)

## Body
- none

## Returns
- optional: bucket(String), endPoint(String), accessKeyId(String), accessKeySecret(String), accessToken(String), accessTokenExpirationMillis(Long), mediaId(String)

## Limits
- accessToken有效期截止时间戳，单位毫秒。 需要在此时间之前使用OSS功能完成文件上传。

source_url: https://open.dingtalk.com/document/development/obtain-information-about-the-dingtalk-disk-upload-file
updated_at: 2026-06-04 19:10:36
