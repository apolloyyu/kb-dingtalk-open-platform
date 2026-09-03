# 获取任务列表（组织维度）

doc_id: VOB0WQJhpi
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/corpTasks
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Task.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- corpId (String, required): 组织corpId。
- userId (String, required): 用户的userid。
- token (String, required): 验权token。 校验方式如下：`md5(corpId + userId + code)`。md5取32位大写值。 **[!NOTE]** 每个企业有自己的唯一code。
- optional: pageSize(Integer), language(String), pageNumber(Integer), keyword(String), appTypes(String), processCodes(String), createFromTimeGMT(Long), createToTimeGMT(Long), env(String)

## Body
- none

## Returns
- optional: totalCount(Long), pageNumber(Long), data(Array), originatorNickName(String), processInstanceId(String), originatorName(String), finishTimeGMT(String), activeTimeGMT(String), actualActionerId(String), originatorEmail(String), title(String), outResultName(String), outResult(String), originatorPhoto(String), taskType(String), originatorNickNameEn(String), createTimeGMT(String), titleInEnglish(String), appType(String), originatorNameInEnglish(String), originatorId(String), taskId(String), status(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-tasks-from-the-organization-dimension
updated_at: 2026-06-02 11:22:55
