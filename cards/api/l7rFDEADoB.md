# 获取用户关注服务窗状态

doc_id: l7rFDEADoB
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/link/isv/followers/statuses
api_version: v2-new
app_types: 第三方企业应用
permissions: OfficialAccount.Meta.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用本接口的访问凭证，通过调用获取第三方企业应用的suiteAccessToken接口获取。

## Path params
- none

## Query params
- accountId (String, required): 服务窗账号ID，通过获取企业下服务窗列表接口获得。
- optional: unionId(String)

## Body
- none

## Returns
- optional: result(Object), status(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/third-party-enterprise-application-obtains-user-attention-service-window-status
updated_at: 2026-06-04 11:32:14
