# 恢复项目归档

doc_id: Ka4A2HXKIx
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/projects/{projectId}/unsuspend
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Project.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- projectId (String, required): 项目ID，可通过调用查询项目接口获取返回参数`projectId`字段。
- userId (String, required): 用户userId。

## Query params
- none

## Body
- none

## Returns
- optional: result(Object), updated(String)

## Limits
- 更新时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。

source_url: https://open.dingtalk.com/document/development/cancel-project-archiving
updated_at: 2026-06-03 09:19:53
