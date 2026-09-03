# 获取空间信息

doc_id: 8TUzoEG5yQ
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.Space.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 空间Id，可调用添加空间接口获取id参数值。

## Query params
- unionId (String, required): 操作者unionId，查询用户详情接口获取。

## Body
- none

## Returns
- optional: space(Object), id(String), corpId(String), creatorId(String), ownerType(String), ownerId(String), modifierId(String), usedQuota(Long), quota(Long), status(String), createTime(String), modifiedTime(String), appId(String), scene(String), sceneId(String), capabilities(Object), canSearch(Boolean), canRename(Boolean), canRecordRecentFile(Boolean), name(String), partitions(Array), partitionType(String), used(Long), max(Long), reserved(Long), type(String)

## Limits
- 分区容量信息，最大值2。
- 最大容量，单位Byte。 - 当前应用容量被设置为max时，代表当前应用容量设置了上限，used参数值不能大于max参数值。 - 当前应用容量未设置为max时，返回空，此时应用共享该企业剩余可用容量。

source_url: https://open.dingtalk.com/document/development/get-space-information
updated_at: 2026-06-04 19:09:31
