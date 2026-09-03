# 创建项目组

doc_id: aSHxP5HFwp
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/industry/campuses/projects/groups
api_version: v2-new
app_types: 第三方企业应用
permissions: Industry.Campus.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- name (String, required): 项目组名称。
- optional: extend(String)

## Returns
- optional: groupId(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-a-project-group
updated_at: 2026-06-04 19:11:16
