# 查询直播观看人员信息

doc_id: oO5JlT5NGJ
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/live/lives/watchUsers
api_version: v2-new
app_types: 第三方企业应用
permissions: Live.Common.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- liveId (String, required): 直播ID，可调用创建直播接口获取。
- unionId (String, required): 用户unionId，可调用查询用户详情接口获取。
- pageSize (Integer, required): 分页大小，每页大小不超过200。
- optional: pageNumber(Integer)

## Body
- none

## Returns
- optional: result(Object), orgUsesList(Array), unionId(String), userId(String), name(String), deptName(String), watchLiveTime(Long), watchPlaybackTime(Long), watchProgressMs(Long), firstWatchTime(Long), outOrgUserList(Array)

## Limits
- 分页大小，每页大小不超过200。
- - 非当前组织内的成员观看直播信息，只能获取到观看时长。

source_url: https://open.dingtalk.com/document/development/queries-the-viewing-information-of-viewers
updated_at: 2026-06-02 12:14:34
