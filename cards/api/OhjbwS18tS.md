# 添加文件夹

doc_id: OhjbwS18tS
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{parentId}/folders
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 空间Id，可调用添加空间接口获取id参数值。
- parentId (String, required): 父目录Id，调用获取文件或文件夹列表接口获取。根目录时，该参数是0。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取。

## Body
- name (String, required): 文件夹的名称，命名有以下要求： - 头尾不能包含空格，否则会自动去除 - 不能包含特殊字符，包括：制表符、\*、"、<、>、
- value (String, required): 属性值。
- visibility (String, required): 属性可见性。 - **PUBLIC**：所有应用都可见 - **PRIVATE**：仅限当前应用可见
- optional: option(Object), conflictStrategy(String), appProperties(Array)

## Returns
- optional: dentry(Object), id(String), spaceId(String), parentId(String), type(String), name(String), size(Long), path(String), version(Long), status(String), extension(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), properties(Object), readOnly(Boolean), appProperties(Map<String, Array>), value(String), visibility(String), uuid(String), partitionType(String), storageDriver(String)

## Limits
- 当前文件夹的应用属性列表，最大值3。
- 属性可见性。 - **PUBLIC**：所有应用都可见 - **PRIVATE**：仅限当前应用可见

source_url: https://open.dingtalk.com/document/development/add-folder
updated_at: 2026-06-04 19:09:32
