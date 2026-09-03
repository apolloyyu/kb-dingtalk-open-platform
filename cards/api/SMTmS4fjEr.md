# 获取所有数据表

doc_id: SMTmS4fjEr
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/notable/bases/{baseId}/sheets
api_version: v2-new
app_types: 企业内部应用
permissions: Notable.Base.Read.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，调用获取企业内部应用的accessToken接口获取。

## Path params
- baseId (String, required): AI表格ID，获取方式请参考数据结构。

## Query params
- operatorId (String, required): 操作人的unionId，可通过以下两种方式获取： - 调用查询用户详情接口获取。 - 调用通过免登码获取用户信息接口获取。

## Body
- none

## Returns
- optional: value(Array), id(String), name(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-notable-getallsheets
updated_at: 2026-08-19 09:07:42
