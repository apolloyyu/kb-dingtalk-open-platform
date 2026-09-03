# 组织变革主数据人员角色数据推送

doc_id: kCZnLl9v0Y
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/amdp/employeeRoles/datas/push
api_version: v2-new
app_types: 第三方企业应用
permissions: Amdp.Data.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: param(Array), userId(String), deptId(String), roleCode(String), isDelete(String)

## Returns
- optional: requestId(String), success(Boolean), status(String), result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-amdpemproledatapush
updated_at: 2026-06-03 09:34:45
