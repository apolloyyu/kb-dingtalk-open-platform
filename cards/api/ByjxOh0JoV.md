# 下载审批附件

doc_id: ByjxOh0JoV
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/processinstance/file/url/get
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，可通过获取企业内部应用的access_token接口获取。

## Body
- request (GrantCspaceRequest, required): 请求信息。
- process_instance_id (String, required): 审批单实例id，调用获取单个审批实例详情接口获取。
- file_id (String, required): 文件id，调用获取单个审批实例详情接口获取。 **[!IMPORTANT]** 文件id是审批组件中上传的fileid（如下图所示），评论中上传的附件fileid暂不支持获取下载链接。 文件组件

## Returns
- optional: result(AppSpaceResponse), file_id(String), space_id(Number), download_uri(String), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- 文件下载地址。 **[!NOTE]** 文件下载地址有效期15分钟。
- - 该接口只能下载审批附件钉盘空间的文件，无法下载到审批评论的附件。

source_url: https://open.dingtalk.com/document/development/grants-the-permission-to-download-the-approval-file
updated_at: 2026-08-25 09:37:50
