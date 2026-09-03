# 获取单条填表实例详情

doc_id: DLJ4fwHEp4
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/swform/instances/{formInstanceId}
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_swapp_collection_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- formInstanceId (String, required): 填表实例ID，调用获取填表实例列表接口获取formInstanceId参数值。

## Query params
- optional: bizType(Integer)

## Body
- none

## Returns
- optional: success(Boolean), result(Object), createTime(String), modifyTime(String), formCode(String), title(String), creator(String), forms(Array), label(String), key(String), value(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-instance-details-of-a-single-fill-table
updated_at: 2026-06-04 19:10:38
