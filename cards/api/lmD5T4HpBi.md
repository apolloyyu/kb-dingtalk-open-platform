# 根据会议逻辑ID查询会议基本信息

doc_id: lmD5T4HpBi
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/exclusive/data/conferences
api_version: v2-new
app_types: 第三方企业应用
permissions: Custom.Common.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- logicalConferenceId (String, required): 会议逻辑ID，可调用创建日程接口获取conferenceId参数值。

## Body
- none

## Returns
- optional: conferenceId(String), title(String), startTime(Long), logicalConferenceId(String), unionId(String), nickname(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-basic-meeting-information-using-a-logical-id
updated_at: 2026-07-14 09:22:17
