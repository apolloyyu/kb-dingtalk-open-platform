# 群发任务

doc_id: wX4Rd0AFnr
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/serviceGroup/messages/tasks/send
api_version: v2-new
app_types: 企业内部应用
permissions: ServiceGroup.Message.Send

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- openTeamId (String, required): 团队ID。 image
- taskName (String, required): 群发任务名称。
- messageContent (Object, required): 群发内容。
- messageType (String, required): 消息类型，取值： - **MARKDOWN**：markdowm消息 - **ACTIONCARD**：卡片消息 - **NOTICE**：群公告
- queryGroup (Object, required): 查询条件。
- queryType (String, required): 群发圈选类型，取值： - **AIMED**：精准圈选 - **MULTI_CONDITIONS**：多条件圈选
- sendConfig (Object, required): 发送配置。
- sendType (String, required): 发送类型，取值： - **TIMING**：定时执行 - **INSTANT**：立即执行
- optional: atAll(Boolean), atActiveUser(Boolean), title(String), content(String), images(Array of String), btns(Array), actionURL(String), atActiveMemberNum(Long), top(Boolean), remind(Boolean), openConversationIds(Array of String), lastActiveTimeStart(String), lastActiveTimeEnd(String), lastActiveDateFilterType(String), groupTagNames(Array of String), openGroupSetId(String), sendTime(String), needUrlTrack(Boolean), urlTrackConfig(Array), trackUrl(String), trackId(String)

## Returns
- optional: openBatchTaskId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/service-group-sending-task-interface
updated_at: 2026-07-15 17:02:08
