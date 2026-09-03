# 获取审批记录

doc_id: 6l32VVyHkF
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/processes/operationRecords
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Process.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证。 - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- appType (String, required): 应用编码，获取方式可参考下图所示：
- systemToken (String, required): 应用密钥，获取方式可参考下图所示：
- userId (String, required): 用户的userId，，可通过获取部门用户userid列表接口获取。
- processInstanceId (String, required): 流程实例ID，可调用获取多个表单实例ID接口获取。
- optional: language(String), env(String)

## Body
- none

## Returns
- optional: result(Array), processInstanceId(String), showName(String), operatorNickName(String), activeTimeGMT(String), operateTimeGMT(String), operateType(String), operatorStatus(String), remark(String), taskHoldTimeGMT(Long), type(String), operatorName(String), operatorUserId(String), activityId(String), taskType(String), taskExecuteType(String), size(Integer), operatorDisplayName(String), files(String), action(String), actionExit(String), dataId(Long), taskId(String), digitalSign(String), operatorPhotoUrl(String), domainList(Array), digitalSignature(String), operator(String), formatAction(String), operatorAgentIdList(Array), orderNumber(String), displayName(String), userInformation(String), departmentDescription(String), userId(String), personalPhoto(String), displayNameInEnglish(String), status(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-an-approval-record
updated_at: 2026-06-03 10:12:03
