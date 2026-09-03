# 搜索用户userId

doc_id: 6WLlTUpfus
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/contact/users/search
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_addresslist_search

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- queryWord (String, required): 用户名称、名称拼音或英文名称。
- offset (Integer, required): 分页页码。
- size (Integer, required): 分页大小。
- optional: fullMatchField(Integer)

## Returns
- optional: hasMore(Boolean), totalCount(Long), list(Array of String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/address-book-search-user-id
updated_at: 2026-06-01 15:38:10
