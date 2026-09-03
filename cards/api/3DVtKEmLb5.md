# 获取用户可见的企业应用列表

doc_id: 3DVtKEmLb5
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/microapp/list_by_userid
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端接口的授权凭证，可通过获取企业内部应用的access_token接口获取。
- userid (String, required): 要查询的员工userid。

## Body
- none

## Returns
- optional: appList(Applist[]), name(String), agentId(Number), appIcon(String), appDesc(String), isSelf(Boolean), appStatus(Number), ompLink(String), homepageLink(String), pcHomepageLink(String), errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/list-the-microapplications-visible-to-employees
updated_at: 2026-08-25 09:39:02
