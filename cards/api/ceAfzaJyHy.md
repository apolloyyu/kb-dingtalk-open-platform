# 通过高级查询条件获取表单实例数据（包括子表单组件数据）

doc_id: ceAfzaJyHy
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/yida/forms/instances/advances/queryAll
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Yida.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- formUuid (String, required): 表单的页面编码，该参数从宜搭应用中获取。
- systemToken (String, required): 宜搭应用密钥，该参数从宜搭应用中获取。
- userId (String, required): 用户userid，可通过查询用户详情或获取部门用户userid列表接口获取。
- appType (String, required): 宜搭应用编码，该参数从宜搭应用中获取。
- optional: pageNumber(Integer), searchCondition(String), modifiedToTimeGMT(String), modifiedFromTimeGMT(String), pageSize(Integer), orderConfigJson(String), originatorId(String), createToTimeGMT(String), createFromTimeGMT(String), useAlias(Boolean)

## Returns
- optional: pageNumber(Long), data(Array), createTimeGMT(String), modifyUser(Object), name(Object), nameInChinese(String), nameInEnglish(String), userId(String), sequence(String), creatorUserId(String), formUuid(String), serialNumber(String), modifiedTimeGMT(String), modifier(String), formData(Map), originator(Object), formInstanceId(String), id(Long), title(String), version(Long), instanceValue(String), totalCount(Long)

## Limits
- 每页最大条目数，最大值100。

source_url: https://open.dingtalk.com/document/development/api-searchformdatasecondgeneration-v2
updated_at: 2026-06-15 11:27:05
