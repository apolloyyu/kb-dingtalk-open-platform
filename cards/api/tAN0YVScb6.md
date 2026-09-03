# 查询会议录制中的文本信息

doc_id: tAN0YVScb6
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/cloudRecords/getTexts
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- optional: conferenceId(String)

## Query params
- optional: unionId(String), startTime(Long), direction(String), maxResults(Long), nextToken(Long)

## Body
- none

## Returns
- optional: hasMore(Boolean), paragraphList(Array), nextTtoken(Long), status(Long), unionId(String), nickName(String), recordId(Long), startTime(Long), endTime(Long), paragraph(String), sentenceList(Array), sentence(String), wordList(Array), word(String), wordId(String)

## Limits
- 开始时间的千分之一秒，单位毫秒。 **[!NOTE]** 例如，该参数值传2000，表示从录制开始的第2秒开始查询。
- 单词查询条数，最大2000。
- 段落记录产生时，在会议录制期间内相对时间的千分之一秒，单位毫秒。 **[!NOTE]** 例如，该参数值是2000，表示在会议录制开始的第2秒，开始了本次语音转文字的记录。
- 段落记录结束时，在会议录制期间内相对时间的千分之一秒，单位毫秒。 **[!NOTE]** 例如，该参数值是8000，表示在会议录制开始的第8秒，结束了本次语音转文字的记录。

source_url: https://open.dingtalk.com/document/development/queries-the-text-information-about-cloud-recording
updated_at: 2026-06-02 12:08:32
