# 查询用户钉钉365会员信息

doc_id: 3rfCmAyhQJ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/vipMember/users/memberInfos/query
api_version: v2-new
app_types: 第三方个人应用
permissions: Vip.Member.User.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: channelCode(String)

## Returns
- optional: isVip(Boolean), expireTime(String)

## Limits
- 标记业务场景字段，可以自定义（长度不超过32字节），用于后续对账和报表数据。

source_url: https://open.dingtalk.com/document/development/api-queryvipmemberinfo
updated_at: 2026-06-03 09:32:03
