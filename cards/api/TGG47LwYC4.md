# 创建代理关系

doc_id: TGG47LwYC4
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/yida/forms/resources/agents/insert
api_version: v2-new
app_types: 企业内部应用
permissions: Yida.PlatformResource.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- corpId (String, required): 组织的corpId。
- userId (String, required): 用户的userid。
- token (String, required): 验权token。校验方式如下：`md5(corpId + userId + corpToken)`。md5取32位大写值。 **[!NOTE]** 每个企业有自己的唯一corpToken。
- agentType (String, required): 代理类型。 - **NORMAL**：普通代理 - **DEPARTURE** ：离职代理
- agentUserId (String, required): 代理人的userid。
- principalUserId (String, required): 被代理人的userid。
- optional: startTimestamp(String), endTimestamp(String), agentCategory(String), agentRangeType(String), agentRangeValue(String), needNoticePrincipal(String)

## Body
- none

## Returns
- optional: success(Boolean), errorMsg(String), errorCode(String), result(String)

## Limits
- 调用本接口，设置代理人在有效期内承担被代理人流程审批工作，其中包含普通代理和离职代理。

source_url: https://open.dingtalk.com/document/development/api-createagenttask
updated_at: 2026-08-07 10:21:03
