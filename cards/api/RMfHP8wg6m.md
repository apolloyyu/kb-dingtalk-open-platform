# 覆写文档（应用授权）

doc_id: RMfHP8wg6m
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/overwriteContent
api_version: v2-new
app_types: 企业内部应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- docKey (String, required): 文档ID（文档的 docKey 或 dentryUuid），通过创建知识库文档接口创建文档后从返回值中获取`docKey`参数。 **[!NOTE]** 从文档URL获取`dentryUuid`，以https://alidocs.dingtalk.com/i/nodes/Z9xxxxa-id为例，dentryUuid 就是Z9xxxxa-id。

## Query params
- operatorId (String, required): 用户unionId，可通过查询用户详情接口获取unionid参数值。

## Body
- content (String, required): 需要写入的内容字符串，注意： - 若 dataType 为 **markdown**，则这里为 markdown 格式的字符串。 - 最大长度为 50000 字符。
- optional: dataType(String)

## Returns
- optional: success(Boolean), result(Object), data(Map<String, Any>)

## Limits
- 需要写入的内容字符串，注意： - 若 dataType 为 **markdown**，则这里为 markdown 格式的字符串。 - 最大长度为 50000 字符。

source_url: https://open.dingtalk.com/document/development/api-doc-updatecontent
updated_at: 2026-06-15 10:34:49
