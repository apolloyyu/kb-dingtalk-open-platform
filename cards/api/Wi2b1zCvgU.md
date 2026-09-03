# 查询公告已读未读人员列表

doc_id: Wi2b1zCvgU
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/blackboard/readers
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_blackboard_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- operationUserId (String, required): 操作人userId。
- maxResults (Integer, required): 每页条目数，最大500。
- blackboardId (String, required): 公告id，可通过调用获取公告ID列表接口获取。
- optional: nextToken(String)

## Body
- none

## Returns
- optional: nextToken(String), users(Array), userId(String), read(String), readTimestamp(Long)

## Limits
- 每页条目数，最大500。

source_url: https://open.dingtalk.com/document/development/query-bulletin-read-unread-persons-list
updated_at: 2026-06-01 18:25:31
