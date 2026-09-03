# 复制文档

doc_id: Cb7CJKB51v
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/doc/dentries/copy
api_version: v2-new
app_types: 企业内部应用
permissions: SNS.Document.WorkspaceDocument.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 接口调用凭证，通过调用获取用户token接口获取。

## Path params
- none

## Query params
- none

## Body
- param (Object, required): 必选参数。
- sourceDentryUuid (String, required): 源文件唯一标识，调用搜索文件接口获取的dentryUUid字段值。
- targetParentDentryUuid (String, required): 目标文件唯一标识，调用搜索文件接口获取的dentryUUid字段值。
- optional: targetPreDentryUuid(String)

## Returns
- optional: isAsync(Boolean), taskId(String), syncCopyResult(Object), dentryUuid(String), driveSpaceId(String), driveDentryId(String), extension(String), name(String), url(String), spaceInfo(Object), sceneType(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-copydoc
updated_at: 2026-06-03 10:13:07
