# 批量添加最近使用应用

doc_id: DZRBJ8hUti
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workbench/components/recentUsed/batch
api_version: v2-new
app_types: 企业内部应用
permissions: Workbench.Component.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- corpId (String, required): 组织corpId。
- usedAppDetailList (Array, required): 最近使用应用列表。
- agentId (String, required): 组织开通的应用Id，可通过调用获取企业所有应用列表接口获取返回参数`agentId`字段。
- userId (String, required): 员工userId。

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-recently-used-apps-in-bulk
updated_at: 2026-06-02 19:48:40
