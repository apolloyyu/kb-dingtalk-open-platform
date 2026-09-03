# 授权下载审批钉盘文件

doc_id: yakmBajb86
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/dentry/auth
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
- file_infos (FileInfo[], required): 授权的钉盘文件信息列表。
- space_id (Number, required): 钉盘空间spaceId。
- file_id (String, required): 文件ID。 **[!NOTE]** 只支持授予审批附件组件中文件的下载权限。
- userid (String, required): 授权的用户userid。
- optional: request(GrantCspaceRequestV2)

## Returns
- optional: result(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/approve-nail-disk-file-authorization
updated_at: 2026-08-25 09:37:49
