# 更新业务实体

doc_id: YUIllDwWtS
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/agoal/entities
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Agoal.Entity.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: Entity(Entity)

## Returns
- optional: success(Boolean), result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-agoalentityupdate
updated_at: 2026-06-15 10:40:58
