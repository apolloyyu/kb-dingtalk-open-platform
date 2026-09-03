# 获取人脸对比接口调用记录

doc_id: esQ6obvUzK
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/faces/recognizeRecords/query
api_version: v2-new
app_types: 企业内部应用
permissions: Custom.Ding.Face.Recognize

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- nextToken (Long, required): 分页游标，从0开始。
- maxResults (Integer, required): 每页最大条目数，最大50。
- optional: fromTime(Long), toTime(Long), agentId(Long), userIds(Array of String), faceCompareResult(Integer)

## Returns
- optional: nextToken(Long), total(Integer), data(Array), agentId(Long), userId(String), invokeTime(Long), faceCompareResult(Integer), platform(Integer)

## Limits
- 每页最大条目数，最大50。

source_url: https://open.dingtalk.com/document/development/you-can-call-this-operation-to-query-the-call-records
updated_at: 2026-06-02 19:19:57
