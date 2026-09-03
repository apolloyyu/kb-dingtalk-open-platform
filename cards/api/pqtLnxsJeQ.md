# 数据集成工作经历删除

doc_id: pqtLnxsJeQ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/workExperiences/remove
api_version: v2-new
app_types: 第三方企业应用
permissions: Hrbrain.Import.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- workNo (String, required): 钉钉 UserId。
- optional: params(Array), companyName(String), endDate(String), startDate(String)

## Returns
- optional: requestId(String), success(Boolean), result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbraindeleteworkexp
updated_at: 2026-06-02 19:29:07
