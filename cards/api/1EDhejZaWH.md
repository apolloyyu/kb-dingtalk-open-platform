# 获取审批钉盘空间信息

doc_id: 1EDhejZaWH
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/processinstance/cspace/info
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- user_id (String, required): 用户的userid。
- optional: agent_id(String)

## Returns
- optional: result(AppSpaceResponse), space_id(Number), errcode(Number), errmsg(String), request_id(String), success(Boolean)

## Limits
- > - 此接口有授权上传权限的作用，每次调用上传附件API接口前，建议使用上传操作人userid再调用一次本接口。

source_url: https://open.dingtalk.com/document/development/query-the-space-of-an-approval-nail
updated_at: 2026-08-25 09:37:47
