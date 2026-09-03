# 获取Agoal指定目标规则下的周期列表

doc_id: S0EPWZTLYt
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/agoal/objectiveRules/periodLists
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Agoal.Period.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- objectiveRuleId (String, required): 目标规则id。

## Body
- none

## Returns
- optional: requestId(String), success(Boolean), content(Array), OpenObjectiveRulePeriodDTO(OpenObjectiveRulePeriodDTO)

## Limits
- 调用本接口获取指定目标规则下的周期列表，返回信息包括周期的id、名称、起止时间和类型，数组列表形式返回，按照开始时间排序，越往前（接近现在时间）的排在前面，同样开始时间的周期再按照周期的间隔时间排序，间隔时间短的在前（季度3个月，排在半年6个月前）。

source_url: https://open.dingtalk.com/document/development/api-agoalobjectiveruleperiodlist
updated_at: 2026-06-15 10:39:00
