# AI卡片流式更新

doc_id: qEwYdVxzG4
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/card/streaming
api_version: v2-new
app_types: 第三方企业应用
permissions: Card.Streaming.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- outTrackId (String, required): 外部卡片实例Id，与创建卡片/创建并投放卡片中的 outTrackId 保持一致。也可在对应模板的**卡片实例管理**中获取： image
- guid (String, required): 请求调用的唯一标志，系统内部用于幂等判断。
- key (String, required): 需要进行流式更新的变量。
- content (String, required): 此更新的流式内容。 **[!NOTE]** - 由于 markdown 需要服务端进行格式转换，必须要保证是全量的内容及markdown 语法的完整性。 - 内容 size 单次不要超过 1 K，总大小建议不要超过 3 K。
- optional: isFull(Boolean), isFinalize(Boolean), isError(Boolean)

## Returns
- optional: success(Boolean), result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-streamingupdate
updated_at: 2026-06-04 14:08:38
