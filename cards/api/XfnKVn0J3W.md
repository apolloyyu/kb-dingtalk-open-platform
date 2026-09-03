# 获取授权企业的永久授权码

doc_id: XfnKVn0J3W
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/service/get_permanent_code
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- suite_access_token (String, required): 第三方应用的suite_access_token，可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- tmp_auth_code (String, required): 回调接口（tmp_auth_code）获取的临时授权码。 **[!NOTE]** 临时授权码只能使用一次。

## Returns
- optional: auth_corp_info(AuthCorpInfo), corpid(String), corp_name(String), permanent_code(String), errmsg(String), errcode(Number)

## Limits
- 回调接口（tmp_auth_code）获取的临时授权码。 **[!NOTE]** 临时授权码只能使用一次。

source_url: https://open.dingtalk.com/document/development/obtain-a-permanent-authorization-code
updated_at: 2026-09-02 18:13:45
