# 同步存储数据

doc_id: CKait4oTVw
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/datas/sync
api_version: v2-new
app_types: 第三方企业应用
permissions: Custom.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- sql (String, required): sql 语句。

## Returns
- optional: rowsAffected(Integer), dataList(Array of Object)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-datasync
updated_at: 2026-06-02 19:19:55
