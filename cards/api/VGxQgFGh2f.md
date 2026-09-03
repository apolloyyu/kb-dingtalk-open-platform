# 数据集成转正记录同步

doc_id: VGxQgFGh2f
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/regulars/import
api_version: v2-new
app_types: 第三方企业应用
permissions: Hrbrain.Import.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- corpId (String, required): 组织编码。

## Body
- regularDate (String, required): 实际转正日期。
- workNo (String, required): 钉钉用户 UserId。
- optional: deptName(String), deptNo(String), extendInfo(Map), jobCodeName(String), jobLevel(String), name(String), planRegularDate(String), postName(String), superEmpId(String), superName(String)

## Returns
- optional: requestId(String), result(Boolean), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbrainimportregular
updated_at: 2026-06-02 19:25:02
