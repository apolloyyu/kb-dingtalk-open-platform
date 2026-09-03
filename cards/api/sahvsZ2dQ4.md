# 查询表单实例数据

doc_id: sahvsZ2dQ4
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/yida/forms/instances/search
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
- appType (String, required): 应用编码，获取方式如下图所示：
- systemToken (String, required): 应用密钥，获取方式如下图所示：
- userId (String, required): 用户userid，可通过查询用户详情或获取部门用户userid列表接口获取。
- formUuid (String, required): 表单的页面编码，获取方式如下图所示：
- optional: language(String), searchFieldJson(String), currentPage(Integer), pageSize(Integer), originatorId(String), createFromTimeGMT(String), createToTimeGMT(String), modifiedFromTimeGMT(String), modifiedToTimeGMT(String), dynamicOrder(String), useAlias(Boolean)

## Returns
- optional: currentPage(Long), totalCount(Long), data(Array), dataId(Long), formInstanceId(String), createdTimeGMT(String), modifiedTimeGMT(String), formUuid(String), modelUuid(String), originator(Object), userId(String), userName(Object), nameInChinese(String), nameInEnglish(String), type(String), modifyUser(Object), formData(Map), title(String), serialNo(String), instanceValue(String), version(Long), creatorUserId(String), modifierUserId(String), sequence(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-searchformdatas-v2
updated_at: 2026-06-04 19:08:58
