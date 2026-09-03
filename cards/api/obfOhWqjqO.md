# 查询宜搭表单服务调用执行记录

doc_id: obfOhWqjqO
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/services/invocationRecords
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- userId (String, required): 操作人的userId。
- systemToken (String, required): 宜搭应用密钥。 该参数从宜搭应用中查看。
- instanceId (String, required): 宜搭表单实例Id，调用获取实例ID列表接口或者获取多个表单实例ID接口获取。
- appType (String, required): 宜搭应用编码。 该参数从宜搭应用中查看。
- formUuid (String, required): 宜搭表单编码。 该参数从宜搭应用中查看。
- optional: hookType(String), hookUuid(String), sourceUuid(String), requestUrl(String), success(Boolean), pageNumber(Integer), invokeAfterDateGMT(String), pageSize(Integer), invokeStatus(String), invokeBeforeDateGMT(String)

## Body
- none

## Returns
- optional: totalCount(Integer), values(Array), serviceContent(String), formUuid(String), sourceUuid(String), invokeStatus(String), invokeUrl(String), invokeResult(String), invokeParameter(String), hookUuid(String), formInstanceId(String), serviceParameter(String), serviceName(String), hookType(String), invokeSuccess(String)

## Limits
- 每页最大条目数，最大值100。

source_url: https://open.dingtalk.com/document/development/the-query-should-be-based-on-the-execution-records-of
updated_at: 2026-06-03 10:11:59
