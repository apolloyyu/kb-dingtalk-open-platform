# 获取子标签列表

doc_id: fsOgYzZAGl
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/exclusive/partnerLabels/{parentId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Partner.Department.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- parentId (String, required): 父标签ID，根目录传-**1**。

## Query params
- none

## Body
- none

## Returns
- optional: data(Array), typeId(Float), typeName(String), labelId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-child-tags-from-a-parent-tag
updated_at: 2026-06-02 19:14:50
