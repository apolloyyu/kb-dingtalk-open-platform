# 撤销代理关系

doc_id: PZCS00Zesc
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/yida/forms/resources/agents/cancel
api_version: v2-new
app_types: 企业内部应用
permissions: Yida.PlatformResource.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- agentUuid (String, required): 代理关系唯一标识，可通过获取代理列表接口获取。
- corpId (String, required): 组织的corpId。
- userId (String, required): 用户的userid。
- token (String, required): 验权token，校验方式如下：`md5(corpId + userId + corpToken)`。md5取32位大写值。 **[!NOTE]** 每个企业有自己的唯一corpToken。
- optional: agentType(String)

## Body
- none

## Returns
- optional: result(Boolean), success(Boolean), errorMsg(String), errorCode(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-cancelagenttask
updated_at: 2026-08-07 10:21:07
