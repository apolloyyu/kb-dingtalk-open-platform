# 获取回收项列表

doc_id: aElUOWshat
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/storage/recycleBins/{recycleBinId}/recycleItems
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.RecycleBin.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- recycleBinId (String, required): 回收站Id，可调用获取回收站信息接口获取id参数值。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取。
- optional: nextToken(String), maxResults(Integer)

## Body
- none

## Returns
- optional: recycleItems(Array), id(String), spaceId(String), dentryId(String), size(Long), type(String), originalName(String), originalPath(String), operatorId(String), operatorTime(String), nextToken(String)

## Limits
- 每页最大条目数，默认值50，最大值50。

source_url: https://open.dingtalk.com/document/development/gets-the-list-of-recycle-items
updated_at: 2026-06-04 19:09:43
