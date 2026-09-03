# 企业员工专属安全管控功能命中查询

doc_id: BJ2pcqJYSJ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/soc/functionHitStatuses/check
api_version: v2-new
app_types: 企业内部应用
permissions: Custom.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- userId (String, required): 查询的员工userId。
- optional: needMissedFunction(Boolean)

## Body
- none

## Returns
- optional: success(Boolean), result(Object), controlStatus(Integer), reason(String), controlList(Array of String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-checkcontrolhitstatus
updated_at: 2026-06-02 19:19:59
