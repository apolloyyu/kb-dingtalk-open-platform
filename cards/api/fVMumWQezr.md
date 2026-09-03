# 新增记录

doc_id: fVMumWQezr
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/notable/bases/{baseId}/sheets/{sheetIdOrName}/records
api_version: v2-new
app_types: 企业内部应用
permissions: Notable.Base.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，调用获取企业内部应用的accessToken接口获取。

## Path params
- baseId (String, required): AI表格ID，获取方式请参考数据结构。
- sheetIdOrName (String, required): 数据表ID或数据表名称。数据表ID可通过获取所有数据表或获取数据表接口获取。

## Query params
- operatorId (String, required): 操作人的unionId，可通过以下两种方式获取： - 调用查询用户详情接口获取。 - 调用通过免登码获取用户信息接口获取。
- optional: clientToken(String)

## Body
- records (Array, required): 需要写入的行记录数据。
- fields (Map<String, Any>, required): 该行记录中各字段的值，采用Map<String, Any>格式： - key：字段名称（String类型），对应数据表中的字段名 - value：字段值（Any类型），根据字段类型传入相应格式的值，格式请参考记录值格式。

## Returns
- optional: value(Array), id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-notable-insertrecords
updated_at: 2026-08-19 09:07:50
