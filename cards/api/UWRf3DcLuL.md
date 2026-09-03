# 上传文件块

doc_id: UWRf3DcLuL
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/file/upload/chunk
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。
- upload_id (String, required): 上传事务ID。
- agent_id (String, required): 应用的AgentId。 - 企业内部应用可以在开发者后台的应用详情页获取。 - 第三方企业应用可以调用获取企业授权信息接口获取。
- chunk_sequence (Long, required): 文件块号，从1开始计数。 **[!NOTE]** 开启分块上传事务接口中，将文件分为几块，就循环调用本接口几次，直到最后一块文件上传成功后，再调用提交文件上传事务接口，获取media_id。

## Body
- file (FileItem, required): 文件内容。

## Returns
- optional: media_id(String), errmsg(String), errcode(Number)

## Limits
- 本接口为文件分块上传中间环节，传输文件块，除最后一块外每块的大小不得小于100KB，最大不超过超过8M。

source_url: https://open.dingtalk.com/document/development/upload-file-blocks
updated_at: 2026-08-25 09:38:40
