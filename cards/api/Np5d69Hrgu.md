# 创建预约会议

doc_id: Np5d69Hrgu
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/conference/scheduleConferences
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: VideoConference.Conference.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证： - 企业内部应用，可调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，可调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- creatorUnionId (String, required): 创建者unionId。
- title (String, required): 预约会议标题。标题最大长度限制不允许超过50。超过50字符时会被截断。超过256字符时调用接口会失败。
- startTime (Long, required): 预约会议开始时间，毫秒级UTC时间戳。
- endTime (Long, required): 预约会议结束时间，毫秒级UTC时间戳。
- optional: scheduleConfSettingModel(Object), hostUnionId(String), confAllowedCorpId(String), lockRoom(Integer), screenShareForbidden(Integer), muteOnJoin(Integer), moziConfVirtualExtraSetting(Object), waitingRoom(Integer), joinBeforeHost(Integer), enableChat(Integer), lockNick(Integer), lockMediaStatusMicMute(Integer), moziConfExtensionAppSettings(Array), coolAppCode(String), autoOpenMode(Integer), extensionAppBizData(String), enableWebAnonymousJoin(Boolean), pushAllMeetingRecords(Boolean), pushMinutesCard(Boolean), pushCloudRecordCard(Boolean), minutesOwnerUnionId(String), cloudRecordOwnerUnionId(String), minutesSummaryTemplateType(String), minutesSummaryTemplateId(String), minutesSummaryDiyTemplateVersion(String), hiddenOwnerNick(Boolean), cohostUnionIds(Array of String), moziConfOpenRecordSetting(Object), recordAutoStart(Integer), recordAutoStartType(Integer), mode(String), isFollowHost(Boolean), restrictShareMinutesSummaryOnly(Integer), aiAgentSummarySetting(Object), value(String), receiverType(Integer), allowAllParticipantsStart(Integer), enableAiAgentStatus(Boolean), allowParticipantShowAiAgentRecord(Boolean)

## Returns
- optional: requestId(String), scheduleConferenceId(String), roomCode(String), url(String), phones(Array of String)

## Limits
- 预约会议标题。标题最大长度限制不允许超过50。超过50字符时会被截断。超过256字符时调用接口会失败。
- 成员入会时静音： - **-1**：开启 - **0**：不开启 - **6**：超过6人自动开启静音
- 会议录制布局： - **grid**：宫格模式,默认9宫格(3x3) - **speech**：演讲者模式 - **full_screen**：全屏模式 - **auto_grid**：自动宫格模式，默认最大4x4宫格 - **screen_cast**：屏幕共享模式，仅放置屏幕共享流 - **p2p**：双人通话模式 - **full_screen_and_speaker**：共享内容+发言人模式
- 是否限制分享听记只能分享摘要： - **0**：不限制 - **1**：限制

source_url: https://open.dingtalk.com/document/development/create-appointment-meeting
updated_at: 2026-06-10 18:28:07
