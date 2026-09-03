# 覆写文档（个人授权）

doc_id: SSu4t5hgp9
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/doc/me/suites/documents/{docKey}/overwriteContent
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Document.Document.Write

## Request headers
- none

## Path params
- docKey (String, required): 文档id（doc_key or dentryUuid）。

## Query params
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过 获取用户token 接口获取

## Body
- content (String, required): 内容正文。
- optional: dataType(String)

## Returns
- optional: data(Map<String, Any>)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-docupdatecontent
updated_at: 2026-06-15 10:20:44
