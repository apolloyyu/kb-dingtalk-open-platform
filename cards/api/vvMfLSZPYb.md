# 获取已加入或正在申请加入上下游组织的组织和个人信息

doc_id: vvMfLSZPYb
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/union/cooperate/info/list
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
- status (Number, required): 加入空间的状态： - **0**：申请中的 - **1**：已成功加入

## Returns
- optional: result(OpenCooperateUnionVo[]), auth_level(Number), userids(String[]), dept_ids(Number[]), union_type(Number), dept_name(String), dept_id(Number), union_org_name(String), union_corp_id(String), success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-information-about-how-to-join-or-apply-to
updated_at: 2026-05-26 09:00:59
