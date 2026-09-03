# 查询DingTalkA1小助理分析

doc_id: L1hDQhqKPd
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/minutes/smartdevice/aisummary
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Minutes.Content.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: agentId(String), openFileId(String)

## Returns
- optional: aiSummaryList(Array), agentId(String), instanceId(String), templateId(String), openFileId(String), summary(String), title(String), creatorUnionId(String), aiSceneRuleAvatarUrl(String), order(Integer), state(Integer)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-querysmartdeviceaisummary
updated_at: 2026-07-03 10:11:27
