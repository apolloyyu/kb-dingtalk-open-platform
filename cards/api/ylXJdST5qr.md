# 开启视频会议直播推流

doc_id: ylXJdST5qr
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/streamOuts/start
api_version: v2-new
app_types: 第三方个人应用
permissions: VideoConference.Conference.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取第三方个人应用的access_token接口获取。

## Path params
- conferenceId (String, required): 会议id，可调用创建视频会议接口获取返回参数`conferenceId`字段。

## Query params
- none

## Body
- unionId (String, required): 用户unionId。
- needHostJoin (Boolean, required): 是否需要主持人加入后才允许推流： - true：允许 - false：不允许
- streamUrlList (Array of String, required): 推流地址列表，最多10个，需要以rtmp开头。
- streamName (String, required): 推流名称。
- mode (String, required): 布局，取值： - **grid**：宫格模式 - **speech**：演讲者模式 - **full_screen**：全屏模式
- smallWindowPosition (String, required): 小窗位置，取值： - **relative_right**：分离右侧 - **float_right**：悬浮右侧 - **float_bottom**：悬浮底部

## Returns
- optional: successStreamMap(Map), failStreamMap(Map)

## Limits
- 推流地址列表，最多10个，需要以rtmp开头。

source_url: https://open.dingtalk.com/document/development/video-conference-enables-live-stream-ingest
updated_at: 2026-06-03 10:12:05
