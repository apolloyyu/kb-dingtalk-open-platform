# 更新 AI 卡片

doc_id: 3EhxX76bt2
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/card/ai/instances/update
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: AICard.Instance.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- outTrackId (String, required): 待更新卡片在当前应用和企业范围内的业务标识。 **[!NOTE]** 非空，长度限制与普通卡片一致。
- outUpdateId (String, required): 本次业务更新的幂等标识，1–64 位字母、数字、下划线或连字符。 **[!NOTE]** 重试保持不变，与网关 `RequestId` 独立。
- flowStatus (String, required): 本次更新后的流状态，使用枚举名，不使用内部数字码。
- a2uiMessages (Array of String, required): A2UI JSON 字符串列表，最多 100 条，必填且不能为 null。 **[!NOTE]** - 允许空列表仅更新状态或标注。 - 总计不超过 256 KiB（UTF-8）。 - 消息 version 为 v1.0，仅支持 `updateComponents` 和 `updateDataModel`。
- surfaceId (String, required): Surface 标识。
- componentId (String, required): 组件标识。
- type (String, required): 标注类型，目前仅 `artifact`。
- optional: a2uiAnnotations(Array)

## Returns
- optional: success(Boolean), result(Object), outTrackId(String), outUpdateId(String), flowStatus(String)

## Limits
- A2UI JSON 字符串列表，最多 100 条，必填且不能为 null。 **[!NOTE]** - 允许空列表仅更新状态或标注。 - 总计不超过 256 KiB（UTF-8）。 - 消息 version 为 v1.0，仅支持 `updateComponents` 和 `updateDataModel`。
- 组件语义标注，最多 100 项且不能重复。 **[!NOTE]** 不传或空列表表示不新增标注，不表示清空已有标注。

source_url: https://open.dingtalk.com/document/development/api-updateaicard
updated_at: 2026-10-23 15:53:02
