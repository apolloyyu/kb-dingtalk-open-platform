# 企业内部群禁言或解除禁言

doc_id: Nl0I6BexfV
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/exclusive/enterpriseSecurities/banOrOpenGroupWords
api_version: v2-new
app_types: 第三方企业应用
permissions: Custom.Group.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- openConverationId (String, required): 群ID，获取方式如下 1. 拥有**专属安全-群管理**权限的管理员登录钉钉管理后台 > 专属钉钉 > 专属安全 > 群管理中读取，如图。 2. 通过接口获取，可调用查询企业内部群信息接口获取。
- banWordsType (Integer, required): 操作类型。 - **0**：解除禁言 - **1**：开启禁言

## Returns
- optional: code(String), cause(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/exclusive-dingtalk-group-ban
updated_at: 2026-06-02 19:18:37
