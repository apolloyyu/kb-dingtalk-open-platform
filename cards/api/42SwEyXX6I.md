# 创建项目任务

doc_id: 42SwEyXX6I
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/tasks
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Task.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。

## Query params
- none

## Body
- projectId (String, required): 项目id。 **[!NOTE]** 目前需要从项目链接中获取该参数值，获取步骤：进入**项目** > 右上角单击**菜单** > **复制链接** 得到的项目链接示例：https://www.teambition.com/project/62c794xxxxx，project下一级路径的值就是项目id。
- content (String, required): 任务标题。
- optional: executorId(String), dueDate(String), note(String), priority(Integer), customfields(Array), customfieldName(String), customfieldId(String), value(Array), title(String), id(String), thumbUrl(String), stageId(String), parentTaskId(String), scenariofieldconfigId(String), startDate(String), visible(String)

## Returns
- optional: result(Object), taskId(String), content(String), involveMembers(Array of String), projectId(String), executorId(String), creatorId(String), created(String), updated(String), note(String), dueDate(String), priority(Integer), customfields(Array), customfieldId(String), value(Array), title(String)

## Limits
- 任务截止时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。
- 任务创建时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。
- 任务更新时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。

source_url: https://open.dingtalk.com/document/development/create-a-project-task
updated_at: 2026-06-03 09:26:02
