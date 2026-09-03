# 通过指标编码推送指标时间维度数据

doc_id: IAUi3JKxJr
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/agoal/indicator/data/push
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Agoal.Indicator.Data.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: code(String), data(Array), periodType(String), period(String)

## Returns
- optional: success(Boolean), result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-agoalindicatordatapush
updated_at: 2026-06-15 10:39:08
