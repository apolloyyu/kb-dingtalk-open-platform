# 增加或减少居民积分

doc_id: bpVpopnvyJ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/resident/points
api_version: v2-new
app_types: 第三方企业应用
permissions: Village.Point.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- isCircle (Boolean, required): 是否查询全员圈积分规则，取值： - **true**：是 - **false**：否（默认值） **[!NOTE]** 取值为false时，查询积分管理积分规则。
- uuid (String, required): 加减积分的唯一幂等标志，由调用方自己生成。
- userId (String, required): 用户userid，可通过调用获取部门用户userid列表接口获取。
- ruleName (String, required): 规则名字。
- score (Integer, required): 本次增加积分。 - 如果为正数表示增加积分。 - 如果为负数表示扣减积分。
- optional: ruleCode(String), actionTime(Long)

## Body
- none

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/increase-or-decrease-resident-points
updated_at: 2026-06-03 15:02:46
