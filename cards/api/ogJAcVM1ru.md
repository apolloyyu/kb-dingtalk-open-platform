# 更新企业内部应用微应用的可使用范围

doc_id: ogJAcVM1ru
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/microapp/set_visible_scopes
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端接口的授权凭证，可通过获取企业内部应用的access_token接口获取。

## Body
- agentId (Number, required): 应用AgentID。
- optional: userVisibleScopes(String[]), deptVisibleScopes(Number[]), isHidden(Boolean)

## Returns
- optional: errmsg(String), errcode(Number)

## Limits
- 是否仅限管理员可见： - **true** - **false**

source_url: https://open.dingtalk.com/document/development/set-the-visible-range-of-the-microapplication
updated_at: 2026-08-25 09:39:03
