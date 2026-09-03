# 创建用户专属短链

doc_id: pgSXkO3PWz
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/conference/customShortLinks
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: VideoConference.Conference.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- creatorUnionId (String, required): 预约会议创建人 unionId。
- scheduleConferenceId (String, required): 预约会议 id，可通过创建预约会议接口获取返回参数`scheduleConferenceId`字段。
- coolAppCode (String, required): 酷应用 Code。可通过开发者后台，微应用中查看酷应用Code。
- optional: extensionAppBizData(String), useExtensionApp(Boolean)

## Returns
- optional: result(Object), customShortLink(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-createcustomshortlink
updated_at: 2026-06-02 09:17:58
