# 获取用户高管模式设置

doc_id: zjUVKU7Lly
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/contact/seniorSettings
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_get_member

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- seniorStaffId (String, required): 用户userId，可通过通过免登码获取用户信息获得userId。

## Body
- none

## Returns
- optional: seniorStaffId(String), protectScenes(Array of String), seniorWhiteList(Array), id(String), type(Integer), name(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-user-executive-mode-settings
updated_at: 2026-06-01 15:25:05
