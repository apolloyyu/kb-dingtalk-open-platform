# 获取专属存储文件路径

doc_id: 9UqpCLY83d
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/privateStores/filePaths/query
api_version: v2-new
app_types: 企业内部应用
permissions: Custom.PrivateFile.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- spaceId (Long, required): 文件spaceId
- dentryId (Long, required): 文件dentryId

## Returns
- optional: filePath(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getprivatestorefilepath
updated_at: 2026-06-02 19:17:34
