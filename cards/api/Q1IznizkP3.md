# 插入块元素

doc_id: Q1IznizkP3
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks
api_version: v2-new
app_types: 企业内部应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- docKey (String, required): 文档ID（文档的 docKey 或 dentryUuid），通过创建知识库文档接口创建文档后，从返回值中获取`docKey`参数。 从文档URL获取`dentryUuid`，以https://alidocs.dingtalk.com/i/nodes/Zxxxxa-id为例，dentryUuid就是Zxxxxa-id。

## Query params
- operatorId (String, required): 用户unionId，可通过查询用户详情接口获取unionid参数值。

## Body
- element (Map<String, Any>, required): 待插入的 BlockElement 类型和创建对应类型所需的属性（详情参考块元素数据结构），结构如下： ``` { "blockType": enum(BlockType), [blockType]: Object(CreateElementProperties), } ```
- optional: blockId(String), index(Integer), where(String)

## Returns
- optional: success(Boolean), result(Object), data(Map<String, Any>)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-docinsertblocks
updated_at: 2026-06-04 19:09:02
