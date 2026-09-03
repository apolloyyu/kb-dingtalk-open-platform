# 查询服务窗粉丝用户基础信息

doc_id: 3koV3uugwR
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/crm/officialAccounts/basics/users
api_version: v2-new
app_types: 第三方个人应用
permissions: OfficialAccount.User.Read.OpenApp

## Request headers
- x-acs-dingtalk-access-token (String, required): 接口调用凭证，调用获取用户token接口获取。

## Path params
- none

## Query params
- unionId (String, required): 需要查询关注状态信息的用户unionId，调用获取用户基本信息接口，获取用户unionId信息。
- bindingToken (String, required): 服务窗与第三方个人应用绑定时生成的授权码，可通过服务窗微应用-开放互联功能进行账号与第三方个人应用的绑定后获取。

## Body
- none

## Returns
- optional: requestId(String), result(Object), status(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-the-basic-information-of-fans-in-the-service-window
updated_at: 2026-06-04 19:12:03
