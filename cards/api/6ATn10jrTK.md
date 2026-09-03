# 知识库转交所有者

doc_id: 6ATn10jrTK
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/doc/dentries/workspace/handover
api_version: v2-new
app_types: 企业内部应用
permissions: SNS.Document.WorkspaceDocument.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- param (Object, required): 必选参数。
- resourceId (String, required): 待转交的知识库的rootNodeUUid，可通过批量获取知识库接口获取。
- receiverUnionId (String, required): 接收人unionId。
- optional: leave(Boolean)

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-handoveryworkspace
updated_at: 2026-06-03 10:13:07
