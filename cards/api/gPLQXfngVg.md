# 查询人脸录入状态

doc_id: gPLQXfngVg
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/faces/recognizeStates/query
api_version: v2-new
app_types: 企业内部应用
permissions: Custom.Ding.Face.State

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userIds (Array of String, required): userIduserId列表。

## Returns
- optional: data(Array), state(Integer), userId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-face-entry-status
updated_at: 2026-06-02 19:19:56
