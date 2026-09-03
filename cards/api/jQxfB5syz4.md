# 获取组织内已完成的审批任务

doc_id: jQxfB5syz4
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/tasks/completedTasks/{corpId}/{userId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Task.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- corpId (String, required): 组织的corpId。
- userId (String, required): 用户userid。

## Query params
- token (String, required): 验权token。 校验方式如下：md5(corpId + userId + code)。md5取32位大写值。 每个企业有自己的唯一code。
- optional: pageSize(Integer), language(String), pageNumber(Integer), keyword(String), appTypes(String), processCodes(String), createFromTimeGMT(Long), createToTimeGMT(Long), env(String)

## Body
- none

## Returns
- optional: totalCount(Long), pageNumber(Long), data(Array), originatorNickName(String), processInstanceId(String), originatorName(String), finishTimeGMT(String), activeTimeGMT(String), actualActionerId(String), originatorEmail(String), title(String), outResultName(String), outResult(String), originatorPhoto(String), taskType(String), originatorNickNameInEnglish(String), createTimeGMT(String), titleInEnglish(String), appType(String), originatorNameInEnglish(String), originatorId(String), taskId(String), status(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-completed-approval-tasks-in-an-organization
updated_at: 2026-06-03 10:11:54
