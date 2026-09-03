# 数据集成培训学习数据删除

doc_id: GjtBKjWWte
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/trainings/remove
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
- trainEndDate (String, required): 训练结束时间。
- trainName (String, required): 训练名称。
- trainStartDate (String, required): 训练开始时间。
- workNo (String, required): 钉钉UserId。
- optional: params(Array)

## Returns
- optional: requestId(String), success(Boolean), result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbraindeletetraining
updated_at: 2026-06-02 19:30:24
