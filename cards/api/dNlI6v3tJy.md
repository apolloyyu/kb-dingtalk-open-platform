# 在段落末尾追加行内元素

doc_id: dNlI6v3tJy
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks/{blockId}/paragraph/appendElement
api_version: v2-new
app_types: 企业内部应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- docKey (String, required): 文档ID（文档的 docKey 或 dentryUuid），通过创建知识库文档接口创建文档后，从返回值中获取`docKey`参数。 从文档URL获取`dentryUuid`，以https://alidocs.dingtalk.com/i/nodes/Zxxxxa-id为例，dentryUuid就是Zxxxxa-id。
- blockId (String, required): 目标段落的唯一标识，可以通过查询块元素接口获取`blockId`参数。

## Query params
- operatorId (String, required): 用户unionId，可通过查询用户详情接口获取unionid参数值。

## Body
- elementType (String, required): 行内元素类型，详情参考块元素数据结构中的行内元素类型。
- properties (Map<String, Any>, required): 创建对应`elementType`类型的行内元素所需的属性。

## Returns
- optional: success(Boolean), result(Object), data(Map<String, Any>)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-docappendparagraph
updated_at: 2026-06-04 19:09:04
