# 创建快捷方式

doc_id: cGsEYJ7wpn
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/doc/resource/shortcut/create
api_version: v2-new
app_types: 企业内部应用
permissions: snsapi_base

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，调用获取用户token接口获取。

## Path params
- none

## Query params
- none

## Body
- param (Object, required): 必选参数。
- sourceResourceId (String, required): 源资源位置的id，可以是dentryUUid或rootNodeUUid，通过调用搜索文件接口获取的dentryUUid字段值。
- sourceResourceType (String, required): 源资源的类型： - **DENTRY**：文件 - **WORKSPACE**：知识库
- targetResourceId (String, required): 目标位置的id，可以是dentryUUid或rootNodeUUid，通过调用搜索文件接口获取的dentryUUid字段值。
- targetResourceType (String, required): 目标资源的类型： - **DENTRY**：文件 - **WORKSPACE**：知识库
- optional: targetResourceName(String)

## Returns
- optional: openDentryInfo(Object), dentryUuid(String), driveSpaceId(String), driveDentryId(String), extension(String), name(String), url(String), spaceInfo(Object), sceneType(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-createshortcut
updated_at: 2026-06-03 10:13:08
