# 根据文档id或URL获取文件DentryUuid

doc_id: bqHoeV9hjx
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/doc/documents/queryDentryUuid
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Document.WorkspaceDocument.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- idOrUrl (String, required): 文档标识，支持以下形态： - 钉钉文档docKey，如文档编辑URL（alidocs.dingtalk.com/document/edit）中docKey参数的值。 - 钉盘dentryKey，如文件URL中dentryKey参数的值。 - 知识库workspaceKey，如知识库相关接口返回的workspaceKey。 - 钉钉文档/钉盘/知识库链接URL，直接传入完整URL。 **[!NOTE]** 纯数字ID（如dentryId）不支持。
- operatorId (String, required): 操作人unionId，通过查询用户详情接口获取。

## Body
- none

## Returns
- optional: dentryUuid(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getuuidbyidorurl
updated_at: 2026-09-10 19:22:41
