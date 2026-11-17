# BV 设备结束录制

doc_id: doc_a59fcb832bfc4afa
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/dvi/bv/kanjian/recordings/stop
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.KanJian.Device.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- operatorUserId (String, required): 操作人 userId。
- sessionId (String, required): 会话ID，通过BV 设备开始录制接口获取。

## Returns
- optional: result(Object), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-stopkanjianrecording
updated_at: 2026-11-17 17:35:21
