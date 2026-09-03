# 搜索文件

doc_id: 3dpgjZBxT0
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/storage/dentries/search
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.Dentry.Search

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- operatorId (String, required): 操作人unionId。

## Body
- keyword (String, required): 搜索关键词。
- optional: option(Object), nextToken(String), maxResults(Integer), dentryCategories(Array of String), creatorIds(Array of String), modifierIds(Array of String), createTimeRange(Object), startTime(Long), endTime(Long), visitTimeRange(Object)

## Returns
- optional: items(Array), dentryUuid(String), name(String), creator(Object), userId(String), modifier(Object), nextToken(String)

## Limits
- 分页大小，默认值50。 最大值50。
- 搜索结果列表，最大size50。

source_url: https://open.dingtalk.com/document/development/search-for-files
updated_at: 2026-06-04 19:09:27
