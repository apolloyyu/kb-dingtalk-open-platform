# 获取主干组织列表

doc_id: V7rs79p3KG
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/org/union/trunk/get
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_related_org_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- none

## Returns
- optional: result(OpenOrgUnion[]), org_name(String), corpid(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-backbone-organization-list
updated_at: 2026-05-26 09:01:00
