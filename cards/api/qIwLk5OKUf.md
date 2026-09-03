# 获取通讯录权限范围

doc_id: qIwLk5OKUf
completeness: full
archived: false
method: GET
endpoint: https://oapi.dingtalk.com/auth/scopes
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- none

## Returns
- optional: auth_org_scopes(AuthOrgScopes), authed_user(String[]), authed_dept(Number[]), auth_user_field(String[]), errmsg(String), errcode(Number)

## Limits
- 如下图所示，当前应用的access_token只具备管理部门A的通讯录权限。开发者可以先调用本接口查看应用的通讯录授权范围。!通信录示意图开发者在调用通讯录接口时，只能获取到在授权范围内的员工通讯录信息，获取非授权范围内的员工通讯录信息会提示`获取部门/员工不在授权范围内`。

source_url: https://open.dingtalk.com/document/development/obtain-corpsecret-authorization-scope
updated_at: 2026-05-26 08:58:21
