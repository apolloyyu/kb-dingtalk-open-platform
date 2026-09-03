# 列出多行记录

doc_id: duHAHYEIjA
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/notable/bases/{baseId}/sheets/{sheetIdOrName}/records/list
api_version: v2-new
app_types: 企业内部应用
permissions: Notable.Base.Read.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，调用获取企业内部应用的accessToken接口获取。

## Path params
- baseId (String, required): AI表格ID，获取方式请参考数据结构。
- sheetIdOrName (String, required): 数据表ID或数据表名称。数据表ID可通过获取所有数据表或获取数据表接口获取。

## Query params
- operatorId (String, required): 操作人的unionId，可通过以下两种方式获取： - 调用查询用户详情接口获取。 - 调用通过免登码获取用户信息接口获取。

## Body
- conditions (Array, required): 条件。
- field (String, required): 字段ID或字段名。
- operator (String, required): 条件类型：equal
- optional: filter(Object), combination(String), value(Array of Any), maxResults(Integer), nextToken(String), fieldIdOrNames(Array of String)

## Returns
- optional: hasMore(Boolean), nextToken(String), records(Array), id(String), fields(Map<String, Any>), createdBy(Object), unionId(String), lastModifiedBy(Object), createdTime(Long), lastModifiedTime(Long)

## Limits
- 每页获取的数据量，默认值为100，最小值为1，最大值为100。
- 可选。指定要返回的字段列表。 建议在字段较多时按需传入，可显著减少响应体积；单次最多 100 个。

source_url: https://open.dingtalk.com/document/development/api-notable-listrecords
updated_at: 2026-08-19 09:07:54
