# 创建字段

doc_id: aC9kXibPnK
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/notable/bases/{baseId}/sheets/{sheetIdOrName}/fields
api_version: v2-new
app_types: 企业内部应用
permissions: Notable.Base.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，调用获取企业内部应用的accessToken接口获取。

## Path params
- baseId (String, required): AI表格ID，获取方式请参考数据结构。
- sheetIdOrName (String, required): 数据表ID或数据表名称。数据表ID可以通过调用获取所有数据表或获取数据表接口获取。

## Query params
- operatorId (String, required): 操作人的unionId，可通过以下两种方式获取： - 调用查询用户详情接口获取。 - 调用通过免登码获取用户信息接口获取。

## Body
- name (String, required): 字段名。
- type (String, required): 字段类型。
- optional: property(Map<String, Any>)

## Returns
- optional: id(String), name(String), type(String), property(Map<String, Any>)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-noatable-createfield
updated_at: 2026-08-19 09:07:45
