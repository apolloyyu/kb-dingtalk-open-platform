# 创建自由任务

doc_id: PV6r1qh7mH
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/project/organizations/users/{userId}/tasks
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
- content (String, required): 任务标题。
- priority (Integer, required): 自由任务优先级，如下图所示。用户是否有自定义更新优先级，获取该参数方法不同。 - 用户未更新优先级。该参数默认为以下值： - **较低，默认值**：10 - **普通**：0 - **紧急**：1 - **非常紧急**：2 - 用户自定义优先级，如下图所示，新增**一般紧急**并调整优先级顺序等，需要通过调用查询优先级列表接口获取接口获取该参数值。 **[!NOTE]** - 优先级数值越大，优先级越高。 - 自定义优先级需要开通企业版或者旗舰版项目，开通请参考开通企业版或旗舰版。
- visible (String, required): 任务可见性。 - **involves**：仅参与者可见 - **members**：所有人可见
- optional: note(String), involveMembers(Array of String), executorId(String), dueDate(String), createTime(String), disableNotification(Boolean), disableActivity(Boolean)

## Returns
- optional: result(Object), dueDate(String), executor(Object), avatarUrl(String), name(String), userId(String), id(String), visible(String), created(String), priority(Integer), involvers(Array), updated(String), note(String), hasReminder(Boolean), creatorId(String), content(String), attachmentsCount(Integer), isDeleted(Boolean), ancestorIds(Array of String), creator(Object), executorId(String), involveMembers(Array of String), isDone(String)

## Limits
- 参与者userId列表，建议参与者总人数不超过20个。
- 任务截止日期，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。
- 任务创建日期，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。
- 创建时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。
- 更新时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 **[!NOTE]** 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。

source_url: https://open.dingtalk.com/document/development/create-a-free-task
updated_at: 2026-06-03 09:26:17
