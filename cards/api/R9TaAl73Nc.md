# 查询宜搭应用列表

doc_id: R9TaAl73Nc
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/organizations/applications
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.App.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- corpId (String, required): 钉钉企业的corpId值。
- userId (String, required): 操作人userId。
- token (String, required): 根据corpId、userId和CorpToken使用md5加密计算生成的字符串。 该参数需线下提供，请通过宜搭技术支持咨询。
- optional: appFilter(String), pageNumber(Integer), pageSize(Integer), appNameSearchKeyword(String), env(String)

## Body
- none

## Returns
- optional: pageNumber(Long), totalCount(Long), data(Array), creatorUserId(String), corpId(String), icon(String), description(String), applicationStatus(String), appConfig(String), inexistence(String), subCorpId(String), appType(String), name(String), systemToken(String), releaseToDingStatus(String)

## Limits
- 每页最大条目数，最大值100。

source_url: https://open.dingtalk.com/document/development/query-the-application-list
updated_at: 2026-06-03 10:11:58
