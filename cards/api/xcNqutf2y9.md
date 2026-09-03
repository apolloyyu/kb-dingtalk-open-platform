# 更新自由任务的优先级

doc_id: xcNqutf2y9
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/project/organizations/users/{userId}/tasks/{taskId}/priorities
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Task.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- taskId (String, required): 任务id，调用创建自由任务接口获取的id值。
- userId (String, required): 操作者userId。

## Query params
- none

## Body
- priority (Integer, required): 自由任务优先级。 - 默认优先级有以下4个： - **-10**：较低，默认值。 - **0**：普通 - **1**：紧急 - **2**：非常紧急 - 新增优先级，调用查询优先级列表接口获取priorityId值。 - 优先级数值越大，优先级越高。 - 自定义优先级需要开通企业版或者旗舰版项目。
- optional: disableActivity(Boolean), disableNotification(Boolean)

## Returns
- optional: result(Object), priority(Integer), updated(String)

## Limits
- 自由任务优先级。 - 默认优先级有以下4个： - **-10**：较低，默认值。 - **0**：普通 - **1**：紧急 - **2**：非常紧急 - 新增优先级，调用查询优先级列表接口获取priorityId值。 - 优先级数值越大，优先级越高。 - 自定义优先级需要开通企业版或者旗舰版项目。
- 更新后的自由任务优先级。 - 优先级有以下4个默认值。 - **-10**：较低，默认值。 - **0**：普通 - **1**：紧急 - **2**：非常紧急 - 自定义优先级，以接口实际调用结果为准，优先级越高，数值越大。
- 更新优先级的时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。 转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。

source_url: https://open.dingtalk.com/document/development/change-free-task-priority
updated_at: 2026-06-04 19:11:48
