# 查询组织维度配置的所有积分规则

doc_id: WePfaAgPwK
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/resident/points/rules
api_version: v2-new
app_types: 第三方企业应用
permissions: Village.Point.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- isCircle (Boolean, required): 是否查询全员圈积分规则，否则查询积分管理积分规则，取值： - **true**：是 - **false**：否（默认值）

## Body
- none

## Returns
- optional: pointRuleList(Array), score(Integer), dayLimitTimes(Integer), status(Integer), ruleCode(String), ruleName(String), extension(String), groupId(Integer), orderId(Integer)

## Limits
- 单日计次上限，0表示无上限。

source_url: https://open.dingtalk.com/document/development/query-all-credit-rules
updated_at: 2026-06-03 09:07:31
