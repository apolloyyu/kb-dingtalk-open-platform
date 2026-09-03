# 创建企业内部应用

doc_id: OPYhzodKBE
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/microApp/apps
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_microapp_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- opUnionId (String, required): 操作人的unionId，该用户必须是拥有**应用管理权限**的管理员，可调用查询用户详情接口获取。
- name (String, required): 应用名称。
- desc (String, required): 应用描述。
- optional: icon(String), homepageLink(String), pcHomepageLink(String), ompLink(String), ipWhiteList(Array of String), scopeType(String), developType(Integer)

## Returns
- optional: agentId(Long), appKey(String), appSecret(String)

## Limits
- 服务器出口IP白名单列表，最大值50。

source_url: https://open.dingtalk.com/document/development/create-an-h5-application-for-your-enterprise
updated_at: 2026-06-03 11:44:57
