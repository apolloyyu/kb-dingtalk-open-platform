# 获取集成自动化日志详情

doc_id: myDImCivs4
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/logs/automations
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.App.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- pageSize (Integer, required): 分页大小，最大值为100。
- userId (String, required): 钉钉userId。
- procInstanceId (String, required): 通过调用分页获取集成自动化日志列表接口获取实例 id。
- pageNumber (Integer, required): 当前第几页，大于等于1。
- token (String, required): corpId+userId+CorpToken做md5加密计算生成的字符串，每个企业有自己的唯一corpToken，可以在平台设置-基本信息中查看。
- corpId (String, required): 钉钉组织 corpId。
- optional: env(String)

## Body
- none

## Returns
- optional: hasMoreData(Boolean), pageNumber(Long), totalCount(Long), data(Array), activityKey(String), flag(String), uuid(String), outputParams(Map), name(String), inputParams(Map), elapsedTimeGMT(Long), finishTimeGMT(String), others(String), status(String)

## Limits
- 分页大小，最大值为100。

source_url: https://open.dingtalk.com/document/development/api-getautoflowlogdetail
updated_at: 2026-06-03 10:12:00
