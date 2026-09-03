# 插入内容

doc_id: F4EkpmUDTs
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/suites/documents/{documentId}/content
api_version: v2-new
app_types: 企业内部应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- documentId (String, required): 文档ID（文档的 docKey 或 dentryUuid），通过创建知识库文档接口创建文档后，从返回值中获取`docKey`参数。 从文档URL获取`dentryUuid`，以https://alidocs.dingtalk.com/i/nodes/Zxxxxa-id为例，dentryUuid就是Zxxxxa-id。

## Query params
- operatorId (String, required): 用户unionId，可通过查询用户详情接口获取unionid参数值。

## Body
- content (Object, required): 插入内容。
- type (String, required): 具体插入的内容类型，目前只支持 `markdown`。
- optional: path(Array of Integer), index(Integer)

## Returns
- optional: success(Boolean), result(Map)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-insertcontent
updated_at: 2026-06-04 19:09:01
