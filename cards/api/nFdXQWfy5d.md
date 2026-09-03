# 单步文件上传

doc_id: nFdXQWfy5d
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/file/upload/single
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。
- file_size (Number, required): 文件大小，单位byte。 **[!NOTE]** 文件大小不得超过8M。
- agent_id (String, required): 应用的AgentId。 - 企业内部应用可以在开发者后台的应用详情页获取。 - 第三方企业应用可以调用获取企业授权信息接口获取。

## Body
- file (FileItem, required): 文件内容。

## Returns
- optional: media_id(String), errmsg(String), errcode(Number)

## Limits
- 分块上传支持将文件分片上传，并由commit步骤完成数据提交，可实现较大文件的上传，最多支持8M \* 10000。

source_url: https://open.dingtalk.com/document/development/single-step-file-upload
updated_at: 2026-08-25 09:38:38
