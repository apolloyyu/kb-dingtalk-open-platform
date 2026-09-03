# 授权用户访问企业的自定义空间

doc_id: sGCnOjhdFi
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/cspace/grant_custom_space
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。
- domain (String, required): 企业内部调用时传入，授权访问该domain的自定义空间，该值来自添加空间接口参数。
- type (String, required): 权限类型： - **add**：上传 - **download**：下载 - **delete**：删除
- userid (String, required): 授权的企业用户userid。
- duration (Number, required): 权限有效时间，有效范围为0~3600秒，超出此范围或不传默认为30秒。
- optional: agent_id(String), path(String), fileids(String)

## Body
- none

## Returns
- optional: errmsg(String), errcode(Number)

## Limits
- 权限有效时间，有效范围为0~3600秒，超出此范围或不传默认为30秒。

source_url: https://open.dingtalk.com/document/development/authorize-a-user-to-access-a-custom-workspace-of-an
updated_at: 2026-08-25 09:38:16
