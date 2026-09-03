# 通讯录userId排序

doc_id: H6pL3kluqJ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/contact/users/sort
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_get_member

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userIdList (Array of String, required): 用户userId，可通过通过免登码获取用户信息获得userid参数值。
- optional: sortType(Integer)

## Returns
- optional: userIdList(Array of String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/address-book-userid-sorting
updated_at: 2026-06-02 09:18:13
