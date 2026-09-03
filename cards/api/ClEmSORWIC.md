# 订阅文件变更事件

doc_id: ClEmSORWIC
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/events/subscribe
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.Event.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取。

## Body
- scopeId (String, required): 订阅范围对应的ID。 - 当scope参数值为ORG时，scopeId对应的是企业corpId，请参考基础概念-CorpId。 - 当scope为SPACE时，scopeId对应的是存储空间ID，可调用添加空间接口获取id。
- scope (String, required): 订阅范围。 - ORG：企业 - SPACE：空间

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/subscribe-to-file-change-events
updated_at: 2026-06-04 19:09:47
