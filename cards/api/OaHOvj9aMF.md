# 获取企业已经加入的或申请加入中的上下游组织的信息

doc_id: OaHOvj9aMF
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/union/cooperate/joined/list
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_related_org_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- status (Number, required): 要查询的空间状态： - **0**：申请中 - **1**：已成功加入

## Returns
- optional: result(OpenCooperateOrgVo[]), belong_org_name(String), belong_corp_id(String), org_name(String), corp_id(String), success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-information-about-the-workspaces-that-the-enterprise-has-joined
updated_at: 2026-05-26 09:00:59
