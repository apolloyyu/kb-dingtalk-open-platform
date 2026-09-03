# 获取代理列表

doc_id: dA3ePqHdVO
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/yida/forms/resources/agents
api_version: v2-new
app_types: 企业内部应用
permissions: Yida.PlatformResource.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- corpId (String, required): 组织的corpId。
- userId (String, required): 用户的userid。
- token (String, required): 验权token。校验方式如下：`md5(corpId + userId + corpToken)`。md5取32位大写值。 **[!NOTE]** 每个企业有自己的唯一corpToken。
- optional: pageSize(Integer), pageNumber(Integer), keywords(String), status(String), agentUuid(String)

## Body
- none

## Returns
- optional: values(Array), creator(String), creatorName(String), agentCreateGMT(String), agentUserId(String), agentName(String), principalUserId(String), principalName(String), agentStartGMT(String), agentEndGMT(String), agentType(String), status(String), agentUuid(String), agentCategory(String), agentRangeType(String), agentRangeValue(String), modifier(String), needNoticePrincipal(String), start(Integer), limit(Integer), totalCount(Integer), currentPage(Integer)

## Limits
- 分页大小，默认每页10条。

source_url: https://open.dingtalk.com/document/development/api-getagenttasks
updated_at: 2026-08-07 10:21:09
