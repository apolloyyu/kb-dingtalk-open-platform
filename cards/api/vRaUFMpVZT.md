# 分页查询居民积分流水

doc_id: vRaUFMpVZT
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/resident/points/records
api_version: v2-new
app_types: 第三方企业应用
permissions: Village.Point.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- isCircle (Boolean, required): 是否查询全员圈积分记录，否则查询积分管理积分记录，取值： - **true**：是 - **false**：否（默认值）
- nextToken (Long, required): 分页游标，第一次请求传0，后续取值是上一次调用此API返回的nextToken参数。
- maxResults (Integer, required): 本次读取的最大数据记录数量，最大值20。
- optional: userId(String), startTime(Long), endTime(Long)

## Body
- none

## Returns
- optional: pointRecordList(Array), userId(String), score(Integer), createAt(Long), uuid(String), ruleCode(String), ruleName(String), hasMore(Boolean), nextToken(Long), totalCount(Long)

## Limits
- 本次读取的最大数据记录数量，最大值20。

source_url: https://open.dingtalk.com/document/development/query-the-integral-flow-records-by-page
updated_at: 2026-06-03 09:07:33
