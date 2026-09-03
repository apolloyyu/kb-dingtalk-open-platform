# 更新企业内部应用

doc_id: tG02MsNilC
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/microApp/apps/{agentId}
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_microapp_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- agentId (Long, required): 应用的agentId，请参考基础概念-AgentId。

## Query params
- none

## Body
- opUnionId (String, required): 操作更新的员工unionId，可调用查询用户详情接口获取unionid参数值。 操作更新的员工必须有该应用的管理权限，否则会出现**没有操作应用的权限**的错误。 应用管理权限查看路径：管理员登录钉钉管理后台 **> 安全与权限 > 权限管理 > 管理组查看**。
- optional: name(String), desc(String), icon(String), homepageLink(String), pcHomepageLink(String), ompLink(String), ipWhiteList(Array of String)

## Returns
- optional: result(Boolean)

## Limits
- 应用名称，名称可以由中文、数字以及字母组成，长度范围要求2-20个字符。
- 应用描述，最大长度200个字符。

source_url: https://open.dingtalk.com/document/development/update-internal-h5-applications
updated_at: 2026-07-14 09:22:20
