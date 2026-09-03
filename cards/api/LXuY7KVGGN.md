# 提交文件上传事务

doc_id: LXuY7KVGGN
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
- file_size (Integer, required): 文件大小，单位byte。分块最小需大于100KB，最大不超过8M
- agent_id (String, required): 应用的AgentId。 - 企业内部应用可以在开发者后台的应用详情页获取。 - 第三方企业应用可以调用获取企业授权信息接口获取。
- chunk_numbers (Integer, required): 文件总块数。
- upload_id (String, required): 上传事务ID。

## Body
- none

## Returns
- optional: media_id(String), errmsg(String), errcode(Number)

## Limits
- 文件大小，单位byte。分块最小需大于100KB，最大不超过8M
- 本接口为文件分块上传最后一步，提交本次分块上传事务，默认情况下，系统会删除超过 24 小时没有提交的分块文件上传事务。

source_url: https://open.dingtalk.com/document/development/submit-a-file-upload-transaction
updated_at: 2026-08-25 09:38:41
