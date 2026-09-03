# 查询家庭孩子信息

doc_id: LkBhtT587G
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/family/child/get
api_version: v1-oapi
app_types: 第三方企业应用
permissions: edu_family_group_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取第三方企业的access_token接口获取。

## Body
- child_userid (String, required): 孩子的userId。
- op_userid (String, required): 操作人的userId。

## Returns
- optional: result(ChildDto), userid(String), nick(String), bind_students(BindStudent[]), corp_id(String), class_id(String), period_code(String), avatar(String), open_id(String), unionId(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-family-child-information
updated_at: 2026-06-08 09:47:57
