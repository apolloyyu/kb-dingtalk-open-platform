# 获取文件详情

doc_id: Vi47eNWF8K
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/esign/files/{fileId}
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Esign.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。
- optional: serviceGroup(String)

## Path params
- fileId (String, required): 文件ID，填写获取文件上传地址接口返回的fileId。

## Query params
- none

## Body
- none

## Returns
- optional: fileId(String), name(String), downloadUrl(String), size(Long), status(Long), pdfTotalPages(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/gets-the-file-details
updated_at: 2026-06-23 18:15:59
