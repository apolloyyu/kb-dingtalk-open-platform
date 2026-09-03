# 开启分块上传事务

doc_id: TCADTwQzsj
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/file/upload/transaction
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。
- file_size (Integer, required): 文件大小，单位byte。分块最小需大于100KB，最大不超过8M。
- agent_id (String, required): 应用的AgentId。 - 企业内部应用可以在开发者后台的应用详情页获取。 - 第三方企业应用可以调用获取企业授权信息接口获取。
- chunk_numbers (Integer, required): 文件总块数。

## Body
- none

## Returns
- optional: upload_id(String), errmsg(String), errcode(Number)

## Limits
- 文件大小，单位byte。分块最小需大于100KB，最大不超过8M。
- 本接口为文件分块上传第一步，开启上传事务，该接口返回upload_id，钉盘服务器以upload_id唯一标识一个上传任务。分块最小需大于100KB，最大不超过8M，最多支持10000块。

source_url: https://open.dingtalk.com/document/development/enable-upload-transaction
updated_at: 2026-08-25 09:38:39
