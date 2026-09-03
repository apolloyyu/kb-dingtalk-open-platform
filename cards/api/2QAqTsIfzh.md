# 设置全员看他

doc_id: 2QAqTsIfzh
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/focus
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- conferenceId (String, required): 会议id，可调用创建视频会议接口获取返回参数`conferenceId`字段。

## Query params
- none

## Body
- action (String, required): 行为动作： - **focus**:全员看他 - **un_focus**：取消全员看他
- unionId (String, required): 被操作用户unionId。 **[!NOTE]** action为focus时必填

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/set-the-whole-staff-to-see-him
updated_at: 2026-06-02 12:06:40
