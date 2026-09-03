# 查询项目

doc_id: jfXXDUgzrL
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/projects/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Project.Read.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。

## Query params
- optional: projectIds(String), name(String), maxResults(Integer), nextToken(String), sourceId(String)

## Body
- none

## Returns
- optional: result(Array), projectId(String), name(String), logo(String), description(String), organizationId(String), visibility(String), isTemplate(Boolean), creatorId(String), isArchived(Boolean), isSuspended(Boolean), uniqueIdPrefix(String), created(String), updated(String), startDate(String), endDate(String), customFields(Array), customFieldId(String), type(String), value(Array), customFieldValueId(String), title(String), metaString(String)

## Limits
- 分页大小。每页返回最大数量，默认10，最大300。
- 创建时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。
- 更新时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。
- 项目开始时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。
- 项目结束时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。

source_url: https://open.dingtalk.com/document/development/query-enterprise-all-projects
updated_at: 2026-06-03 09:19:52
