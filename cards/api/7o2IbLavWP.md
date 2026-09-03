# 搜索部门ID

doc_id: 7o2IbLavWP
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/contact/departments/search
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
- queryWord (String, required): 部门名称或者部门名称拼音。
- offset (Integer, required): 分页页码。
- size (Integer, required): 分页大小。

## Returns
- optional: hasMore(Boolean), totalCount(Long), list(Array of Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/address-book-search-department-id
updated_at: 2026-06-01 16:07:06
