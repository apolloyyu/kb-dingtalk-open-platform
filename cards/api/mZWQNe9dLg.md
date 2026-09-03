# 删除项目组

doc_id: mZWQNe9dLg
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/industry/campuses/projects/groups
api_version: v2-new
app_types: 第三方企业应用
permissions: Industry.Campus.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- campusProjectGroupId (Long, required): 项目组ID，可调用创建项目组接口获取groupId参数值。

## Body
- none

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-the-project-group-team
updated_at: 2026-06-08 11:45:03
