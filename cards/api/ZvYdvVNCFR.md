# 批量获取流程实例列表

doc_id: ZvYdvVNCFR
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/processes/instances/searchWithIds
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Process.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- appType (String, required): 应用编码，获取方式可参考下图所示：
- systemToken (String, required): 应用密钥，获取方式可参考下图所示：
- userId (String, required): 用户的userId，可通过获取部门用户userid列表接口获取。
- processInstanceIds (String, required): 流程实例ID列表，多个流程实例ID之间使用英文逗号分隔。
- optional: language(String)

## Body
- none

## Returns
- optional: result(Array), actionExecutor(Array), userId(String), name(Object), nameInChinese(String), nameInEnglish(String), type(String), departmentName(String), email(String), processInstanceId(String), formUuid(String), processCode(String), title(String), instanceStatus(String), approvedResult(String), originator(Object), data(Map)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-multiple-process-instances
updated_at: 2026-06-03 10:11:41
