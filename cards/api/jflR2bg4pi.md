# 批量删除跟进记录数据

doc_id: jflR2bg4pi
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/followRecords/batchRemove
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_crm_maindata_write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- operatorUserId (String, required): 操作人userId。
- instanceIds (Array of String, required): 跟进记录ID。 - 企业内部应用，调用接口获取。 - 第三方企业应用，调用接口获取。

## Returns
- optional: results(Array), success(Boolean), errorCode(String), errorMsg(String), instanceId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/batch-delete-follow-up-record-data
updated_at: 2026-06-04 19:12:14
