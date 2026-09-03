# 获取文件或文件夹列表

doc_id: SDdLWa7D1P
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.File.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 空间Id，调用添加空间接口获取id参数值。

## Query params
- parentId (String, required): 父目录Id。根目录时，该参数是0，调用获取文件或文件夹列表接口获取parentId参数值。
- unionId (String, required): 操作者的unionId，可调用查询用户详情接口获取。
- optional: nextToken(String), maxResults(Integer), orderBy(String), order(String), withThumbnail(Boolean)

## Body
- none

## Returns
- optional: dentries(Array), id(String), spaceId(String), parentId(String), type(String), name(String), size(Long), path(String), version(Long), status(String), extension(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), properties(Object), readOnly(Boolean), appProperties(Map<String, Array>), value(String), visibility(String), uuid(String), partitionType(String), storageDriver(String), thumbnail(Object), width(Integer), height(Integer), url(String), nextToken(String)

## Limits
- 每页条目数，最大值50。

source_url: https://open.dingtalk.com/document/development/get-a-list-of-files-or-folders
updated_at: 2026-06-02 18:49:01
