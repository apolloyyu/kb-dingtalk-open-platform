# 查询预约会议设置

doc_id: rpa11SQ6W2
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/conference/scheduleConferences/settings
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- scheduleConferenceId (String, required): 预约会议 id，可通过创建预约会议接口获取返回参数`scheduleConferenceId`字段。

## Body
- none

## Returns
- optional: scheduleConfSettingModel(Object), hostUnionId(String), cohostUnionIds(Array of String), confAllowedCorpId(String), lockRoom(Integer), screenShareForbidden(Integer), muteOnJoin(Integer), moziConfVirtualExtraSetting(Object), waitingRoom(Integer), joinBeforeHost(Integer), enableChat(Integer), lockNick(Integer), lockMediaStatusMicMute(Integer), moziConfExtensionAppSettings(Array), clientId(String), coolAppCode(String), autoOpenMode(String), extensionAppBizData(String), enableWebAnonymousJoin(Boolean)

## Limits
- 成员入会时静音： - -1：开启 - 0：不开启 - 6：超过6人自动开启静音

source_url: https://open.dingtalk.com/document/development/api-queryscheduleconfsettings
updated_at: 2026-06-02 09:18:00
