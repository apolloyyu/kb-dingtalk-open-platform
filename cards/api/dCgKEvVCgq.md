# 设置单聊机器人快捷入口

doc_id: dCgKEvVCgq
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/robot/plugins/set
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
- name (String, required): 快捷入口的名称，支持国际化形式，如`{"en_US":"test123","zh_CN":"测试123"}`。
- icon (String, required): 快捷入口的图标id，可通过调用上传媒体文件接口获取参数字段`mediaId`。
- optional: robotCode(String), pluginInfoList(Array), pcUrl(String), mobileUrl(String)

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/set-robot-quick-entrance
updated_at: 2026-06-05 13:49:11
