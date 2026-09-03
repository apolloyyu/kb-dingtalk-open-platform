# 根据流程实例ID获取流程实例

doc_id: E43nL1NThr
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/yida/processes/instancesInfos/{id}
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Yida.Process.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- id (String, required): 流程实例ID。

## Query params
- appType (String, required): 应用ID。
- systemToken (String, required): 应用密钥，在应用数据中获取。
- userId (String, required): 用户userid。
- optional: language(String), useAlias(Boolean), formUuid(String)

## Body
- none

## Returns
- optional: createTimeGMT(String), processInstanceId(String), actionExecutor(Array), name(Object), nameInEnglish(String), type(String), nameInChinese(String), deptName(String), userId(String), email(String), approvedResult(String), formUuid(String), data(Map), modifiedTimeGMT(String), processCode(String), originator(Object), title(String), instanceStatus(String), version(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getinstancebyid-v2
updated_at: 2026-06-15 10:44:09
