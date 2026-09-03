# 撤回已经发送的DING消息

doc_id: stHyRQTKI2
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/robot/ding/recall
api_version: v2-new
app_types: 企业内部应用
permissions: Premium.Ding.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- robotCode (String, required): 发送DING消息的机器人ID。 需要撤销的DING消息，发送和撤回操作必须是同一个机器人。
- openDingId (String, required): 需要被撤回的DING消息ID，可调用发送DING消息接口获取。

## Returns
- optional: openDingId(String)

## Limits
- 当前接口为钉钉专业版和钉钉专属版专享接口，仅限钉钉专业版和钉钉专属版客户使用，并可按需增购OpenAPI发DING额度。

source_url: https://open.dingtalk.com/document/development/robot-withdraws-pin-message
updated_at: 2026-06-05 13:37:02
