# 批量获取表单实例数据

doc_id: YZ9lfkiMvC
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/yida/forms/instances/ids/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- formUuid (String, required): 页面编码，获取方式可参考下图所示：
- appType (String, required): 应用编码，获取方式可参考下图所示：
- systemToken (String, required): 应用密钥，获取方式可参考下图所示：
- formInstanceIdList (Array of String, required): 宜搭表单实例Id，调用获取实例ID列表接口或者获取多个表单实例ID接口获取。
- userId (String, required): 用户userId，可通过获取部门用户userid列表接口获取。
- optional: needFormInstanceValue(Boolean)

## Returns
- optional: result(Array), createTimeGMT(String), modifyUser(Object), name(Object), nameInChinese(String), nameInEnglish(String), userId(String), sequence(String), creatorUserId(String), formUuid(String), serialNumber(String), modifiedTimeGMT(String), modifier(String), formData(Map), originator(Object), formInstanceId(String), id(Long), title(String), version(Long), instanceValue(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-multiple-form-instance-data
updated_at: 2026-06-03 10:11:48
