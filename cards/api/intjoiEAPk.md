# 在段落末尾追加文本

doc_id: intjoiEAPk
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks/{blockId}/paragraph/appendText
api_version: v2-new
app_types: 企业内部应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- docKey (String, required): 文档ID（文档的 docKey 或 dentryUuid），通过创建知识库文档接口创建文档后，从返回值中获取`docKey`参数。 从文档URL获取`dentryUuid`，以https://alidocs.dingtalk.com/i/nodes/Zxxxxa-id为例，dentryUuid就是Zxxxxa-id。
- blockId (String, required): 目标段落的唯一标识，可以通过查询块元素接口获得该段落的`blockId`参数。

## Query params
- operatorId (String, required): 用户unionId，可通过查询用户详情接口获取unionid参数值。

## Body
- text (String, required): 待插入的文本。

## Returns
- optional: success(Boolean), result(Object), data(Map<String, Any>)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-docappendtext
updated_at: 2026-06-04 19:09:03
