# 更新块元素

doc_id: pplS9nSNPE
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/doc/suites/documents/{documentId}/blocks/{blockId}
api_version: v2-new
app_types: 企业内部应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- documentId (String, required): 文档ID（文档的 docKey 或 dentryUuid），通过创建知识库文档接口创建文档后，从返回值中获取`docKey`参数。 从文档URL获取`dentryUuid`，以https://alidocs.dingtalk.com/i/nodes/Zxxxxa-id为例，dentryUuid就是Zxxxxa-id。
- blockId (String, required): 目标段落的唯一标识，可以通过查询块元素接口获得该段落的 `blockId` 参数。

## Query params
- operatorId (String, required): 用户unionId，可通过查询用户详情接口获取unionid参数值。

## Body
- element (Map<String, Any>, required): 待更新的块元素 BlockElement 类型和对应类型所需的属性（详情参考块元素数据结构），结构如下： ``` { "blockType": enum(BlockType), [blockType]: Object(ElementProperties), } ```

## Returns
- optional: success(Boolean), result(Object)

## Limits
- 调用本接口，可以更新文档中任意 1 个块元素的内容或属性。

source_url: https://open.dingtalk.com/document/development/api-docblocksmodify
updated_at: 2026-06-04 19:09:03
