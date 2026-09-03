# 删除块元素

doc_id: qjfMqiMixD
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks/{blockId}
api_version: v2-new
app_types: 企业内部应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- docKey (String, required): 文档ID（文档的 docKey 或 dentryUuid），通过创建知识库文档接口创建文档后，从返回值中获取`docKey`参数。 **[!NOTE]** 从文档URL获取`dentryUuid`，以https://alidocs.dingtalk.com/i/nodes/Zxxxxa-id为例，dentryUuid就是Zxxxxa-id。
- blockId (String, required): 待删除块的 `blockId`，可以通过查询块元素接口获得 `blockId` 参数。

## Query params
- operatorId (String, required): 用户unionId，可通过查询用户详情接口获取unionid参数值。

## Body
- none

## Returns
- optional: success(Boolean)

## Limits
- 调用本接口，可以删除文档中 1 个特定的块元素。

source_url: https://open.dingtalk.com/document/development/api-docdeleteblock
updated_at: 2026-06-02 18:38:42
