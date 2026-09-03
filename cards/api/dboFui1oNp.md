# 根据指定条件查询自定义对象数据

doc_id: dboFui1oNp
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/customObjects/datas/query
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_crm_customdata_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- maxResults (Long, required): 分页大小。 **[!NOTE]** 最多可一次获取200条数据。
- name (String, required): 表单 code。
- optional: currentOperatorUserId(String), nextToken(String), queryDsl(String)

## Returns
- optional: result(Object), nextToken(String), hasMore(Boolean), maxResults(Long), values(Array), creatorNick(String), gmtModified(String), creatorUserId(String), instanceId(String), data(Map<String, String>), extendData(Map<String, String>), gmtCreate(String), objectType(String), permission(Object), participantUserIds(Array of String), ownerUserIds(Array of String), procInstStatus(String), procOutResult(String)

## Limits
- 分页大小。 **[!NOTE]** 最多可一次获取200条数据。

source_url: https://open.dingtalk.com/document/development/api-getobjectdata
updated_at: 2026-07-21 09:26:19
