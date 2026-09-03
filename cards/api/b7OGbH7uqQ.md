# 发送DING消息

doc_id: b7OGbH7uqQ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/robot/ding/send
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
- robotCode (String, required): 发DING消息的机器人ID，需填写创建企业内部应用机器人后获取的机器人 ID（robotCode）。
- remindType (Integer, required): DING消息类型： - **1**：应用内DING - **2**：短信DING - **3**：电话DING - 短信 DING 和电话 DING 需要单独购买权益包。本接口在没有购买短信 DING 和电话 DING的情况下，仅支持发送应用内 DING。 - 可登录钉钉管理后台，单击左侧导航栏增值服务 > 产品专区进行购买。
- receiverUserIdList (Array of String, required): 接收人userId列表，可通过查询用户详情或获取部门用户userid列表接口获取。 - 应用内DING消息，每次接收人不能超过200个。 - 短信DING和电话DING，每次接收人不能超过20个。
- content (String, required): DING消息内容。
- optional: callVoice(String)

## Returns
- optional: openDingId(String), failedList(Map)

## Limits
- 接收人userId列表，可通过查询用户详情或获取部门用户userid列表接口获取。 - 应用内DING消息，每次接收人不能超过200个。 - 短信DING和电话DING，每次接收人不能超过20个。
- 当前接口为钉钉专业版和钉钉专属版专享接口，仅限钉钉专业版和钉钉专属版客户使用，并可按需增购OpenAPI发DING额度

source_url: https://open.dingtalk.com/document/development/robot-sends-nail-message
updated_at: 2026-06-05 13:37:43
