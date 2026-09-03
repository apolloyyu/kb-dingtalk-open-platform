# 获取文件详情

doc_id: iekB8uM9ae
completeness: full
archived: true
method: GET
endpoint: https://api.dingtalk.com/v1.0/esign/files/{fileId}
api_version: v2-new
app_types: 第三方企业应用
permissions: not_stated

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- optional: fileId(String)

## Query params
- none

## Body
- none

## Returns
- optional: data(Object), fileId(String), name(String), downloadUrl(String), size(Long), status(Integer), pdfTotalPages(Integer), code(Integer), message(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-file-details
updated_at: 2026-08-25 09:37:35
