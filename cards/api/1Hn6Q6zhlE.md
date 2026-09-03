# 获取外部联系人列表

doc_id: 1Hn6Q6zhlE
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/extcontact/list
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_ext_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- optional: size(Number), offset(Number)

## Returns
- optional: results(OpenExtContact[]), title(String), share_dept_ids(Number[]), label_ids(Number[]), remark(String), address(String), name(String), follower_user_id(String), state_code(String), company_name(String), share_user_ids(String[]), mobile(String), userid(String), email(String), errcode(Number), errmsg(String), request_id(String)

## Limits
- 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。

source_url: https://open.dingtalk.com/document/development/obtain-the-external-contact-list
updated_at: 2026-05-27 13:09:33
