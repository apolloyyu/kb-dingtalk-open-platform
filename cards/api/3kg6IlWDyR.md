# 添加任务的关联内容

doc_id: 3kg6IlWDyR
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/tasks/{taskId}/objectLinks
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Task.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。
- taskId (String, required): 被关联的项目任务id，调用创建项目任务接口获取的taskId。

## Query params
- none

## Body
- title (String, required): 关联内容的标题。
- url (String, required): 关联内容的链接url。
- optional: linkedData(Object), content(String), thumbnailUrl(String)

## Returns
- optional: result(Object), created(String), objectLinkId(String)

## Limits
- 关联内容的创建时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。

source_url: https://open.dingtalk.com/document/development/create-a-linked-object-associated-with-a-task
updated_at: 2026-06-04 19:11:40
