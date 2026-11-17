# 项目文档管理：知识库文档沉淀与需求流程线上化

doc_id: wLUR56Gz0w
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/v2/user/getuserinfo
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- none

## Limits
- - **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。
- - `size`：分页大小，最大100。
- - ✅ 已添加`qyapi_base`、`qyapi_get_department_member`、`Wiki.Workspace.Write`、`Wiki.Workspace.Read`、`Document.WorkspaceDocument.Write`、`Wiki.Node.Read`、`Storage.Permission.Write`、`Storage.File.Write`共8个接口权限。

source_url: https://open.dingtalk.com/document/development/knowledge-document-requirement-process
updated_at: 2026-11-11 09:20:20
