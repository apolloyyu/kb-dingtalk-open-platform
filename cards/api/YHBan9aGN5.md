# 删除个人或企业客户数据

doc_id: YHBan9aGN5
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/crm/personalCustomers/{dataId}
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_crm_maindata_write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- dataId (String, required): 客户数据ID，调用根据指定条件查询个人或企业客户数据接口获取instanceId参数值。

## Query params
- currentOperatorUserId (String, required): 操作人用户userId。
- optional: relationType(String)

## Body
- none

## Returns
- optional: instanceId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-crm-personal-customer
updated_at: 2026-06-04 19:12:07
