# 查询单聊机器人的快捷入口

doc_id: UCIEZHdilh
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/robot/plugins/query
api_version: v2-new
app_types: 企业内部应用
permissions: Robot.SingleChat.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- robotCode (String, required): 机器人的编码，参见机器人名词表-robotCode内容，获取`robotCode`。

## Returns
- optional: pluginInfoList(Array), name(String), icon(String), pcUrl(String), mobileUrl(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/quick-entrance-of-inquiry-single-chat-robot
updated_at: 2026-06-05 13:49:09
