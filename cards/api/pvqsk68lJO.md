# 获取文件上传地址

doc_id: pvqsk68lJO
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/esign/files/uploadUrls
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Esign.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。
- optional: serviceGroup(String)

## Path params
- none

## Query params
- none

## Body
- optional: contentMd5(String), contentType(String), fileName(String), fileSize(Long), convert2Pdf(Boolean)

## Returns
- optional: fileId(String), uploadUrl(String)

## Limits
- 文件直传地址, 可以重复使用，但是只能传相同的文件，有效期一小时。

source_url: https://open.dingtalk.com/document/development/obtain-the-upload-url-of-a-file-1
updated_at: 2026-06-23 18:15:58
