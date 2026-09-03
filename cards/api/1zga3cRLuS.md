# 获取组织内某人提交的任务

doc_id: 1zga3cRLuS
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/tasks/myCorpSubmission/{userId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Process.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 用户userid。

## Query params
- corpId (String, required): 组织的corpId。
- token (String, required): 验权token。 校验方式如下：md5(corpId + userId + code)。md5取32位大写值。 每个企业有自己的唯一code。
- optional: pageSize(Integer), language(String), pageNumber(Integer), keyword(String), appTypes(String), processCodes(String), createFromTimeGMT(Long), createToTimeGMT(Long), env(String)

## Body
- none

## Returns
- optional: totalCount(Long), pageNumber(Long), data(Array), actionerName(Array of String), processInstanceId(String), modifiedTimeGMT(String), finishTimeGMT(String), formUuid(String), processInstanceStatus(String), originatorDisplayName(String), dataType(String), originatorAvatar(String), processInstanceStatusText(String), actioner(Array), employeeTypeInformation(String), employeeType(String), level(String), nickName(String), orderNumber(String), pinyinNickName(String), superUserId(String), userId(String), buName(String), tbWang(String), humanResourceGroupWorkNumber(String), pinyinNameAll(String), name(String), state(String), personalPhotoUrl(String), isSystemAdmin(Boolean), email(String), personalPhoto(String), processApprovedResultText(String), formInstanceId(String), title(String), version(Long), instanceValue(String), processApprovedResult(String), createTimeGMT(String), processId(Long), processName(String), processCode(String), appType(String), actionerId(Array of String), dataMap(Map), currentActivityInstances(Array), activityName(String), activityNameEn(String), activityId(String), id(Long), activityInstanceStatus(String), originatorId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-tasks-submitted-by-someone-in-an-organization
updated_at: 2026-06-03 10:11:53
