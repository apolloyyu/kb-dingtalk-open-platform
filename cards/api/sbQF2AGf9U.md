# 发送Rooms中控API信令

doc_id: sbQF2AGf9U
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/rooms/central/control
api_version: v2-new
app_types: 企业内部应用
permissions: VideoConference.Conference.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: unionId(String), roomId(String), controlBody(String)

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-sendcentralcontrol
updated_at: 2026-06-01 14:27:50
