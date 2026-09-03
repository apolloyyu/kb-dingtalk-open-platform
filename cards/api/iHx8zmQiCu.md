# 更新文件或文件夹的应用属性

doc_id: iHx8zmQiCu
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{dentryId}/appProperties
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (Long, required): 空间Id，可调用添加空间接口获取id参数值。
- dentryId (Long, required): 文件或文件夹的id，可调用获取文件或文件夹列表或根据dentryUuid获取spaceId和dentryId接口获取id参数值。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取unionid参数值。

## Body
- appProperties (Array, required): 应用属性列表，最大值3。
- name (String, required): 属性名称。 - 如果属性名称已存在，会更新原有的属性信息。 - 如果属性名称不存在，会添加该属性信息。
- value (String, required): 属性值。
- visibility (String, required): 属性可见范围。 - **PUBLIC**：该属性所有App可见 - **PRIVATE**：该属性仅其归属App可见，默认值

## Returns
- optional: success(Boolean)

## Limits
- 应用属性列表，最大值3。

source_url: https://open.dingtalk.com/document/development/update-file-application-properties
updated_at: 2026-06-04 19:09:35
