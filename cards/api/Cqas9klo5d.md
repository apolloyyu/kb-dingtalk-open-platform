# 专属小红点推送

doc_id: Cqas9klo5d
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/exclusiveDesigns/redPoints/push
api_version: v2-new
app_types: 第三方企业应用
permissions: Custom.Design.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证： - 企业内部应用可调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用可调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- agentId (String, required): 微应用agentId，请参考基础概念-AgentId。
- pushType (String, required): 推送类型取值： - Number：pushValue值为数字
- optional: badgeItems(Array), userId(String), pushValue(String), version(Long)

## Returns
- optional: success(Boolean)

## Limits
- 推送列表，建议不超过100。
- 推送的内容（目前仅限数字）。 - 当该参数值为"0"时，表示移除对应的小红点推送。
- 仅限购买了**开放&集成包**的专属钉钉企业进行使用，如需购买，请联系钉钉小二咨询，使用前你可以登录**钉钉管理后台** > **钉钉专属版** > **开放&运维** > **能力开放** > **推送小红点**进行配置。 ![](https://down-cdn.dingtalk.com/ddmedia/iwElAqNwbmcDBgTRB2oF0QLGBrAKg0X-H_CgFQWiegjMpQoAB9MAAAAA-hsdTwgACapvcGVuLnRvb2xzCgAL0

source_url: https://open.dingtalk.com/document/development/push-a-red-dot-to-the-micro-application
updated_at: 2026-06-04 19:10:01
