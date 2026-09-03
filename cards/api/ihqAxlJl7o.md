# 获取指定应用下的表单列表

doc_id: ihqAxlJl7o
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/forms
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- appType (String, required): 应用编码，获取方式可参考下图所示：
- systemToken (String, required): 应用密钥，获取方式可参考下图所示：
- userId (String, required): 操作人userId，可通过获取部门用户userid列表接口获取。
- optional: formTypes(String), pageSize(Integer), pageNumber(Integer)

## Body
- none

## Returns
- optional: success(Boolean), result(Object), data(Array), formType(String), creator(String), formUuid(String), gmtCreate(String), title(Object), enUS(String), zhCN(String), totalCount(Integer), currentPage(Integer)

## Limits
- 每页条目数，默认值100，最大值100。

source_url: https://open.dingtalk.com/document/development/depending-on-the-application-id-to-get-the-form-list
updated_at: 2026-06-03 10:11:42
