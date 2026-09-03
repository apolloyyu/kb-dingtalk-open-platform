# 下载机器人接收消息的文件内容

doc_id: RFt9sbk5s9
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/robot/messageFiles/download
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_robot_sendmsg

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- downloadCode (String, required): 用户向机器人发送文件消息后，机器人回调给开发者消息中的下载码。详情参考机器人接收消息。
- robotCode (String, required): 机器人的编码，详情参考机器人 ID。

## Returns
- optional: downloadUrl(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/download-the-file-content-of-the-robot-receiving-message
updated_at: 2026-06-05 13:41:57
