# 获取发送给用户的通知

doc_id: 0y4YFy9FW5
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/corpNotifications/{userId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Task.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 用户的userid。

## Query params
- corpId (String, required): 组织的corpId。
- token (String, required): 验权token。 校验方式如下：md5(corpId + userId + code)。md5取32位大写值。 每个企业有自己的唯一code。
- optional: pageNumber(Integer), pageSize(Integer), language(String), keyword(String), appTypes(String), processCodes(String), instanceCreateFromTimeGMT(Long), instanceCreateToTimeGMT(Long), createFromTimeGMT(Long), createToTimeGMT(Long), env(String)

## Body
- none

## Returns
- optional: totalCount(Long), pageNumber(Long), data(Array), createTimeGMT(String), activityId(String), creatorUserId(String), corpId(String), titleInEnglish(String), modifiedTimeGMT(String), appType(String), processCode(String), mobileUrl(String), formInstanceId(String), instStatus(String), title(String), url(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-notifications-sent-to-users
updated_at: 2026-06-03 10:11:55
