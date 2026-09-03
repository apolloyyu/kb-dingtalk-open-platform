# 获取员工人数

doc_id: Nl8Xx4wCcQ
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/user/count
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_get_member

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- only_active (Boolean, required): 是否包含未激活钉钉人数： - **false**：包含未激活钉钉的人员数量。 - **true**：只包含激活钉钉的人员数量。

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(CountUserResponse), count(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/user-management-acquires-number-employees
updated_at: 2026-06-08 09:28:36
