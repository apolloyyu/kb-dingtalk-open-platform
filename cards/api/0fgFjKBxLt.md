# 创建实际工时

doc_id: 0fgFjKBxLt
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/workTimes
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Task.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者用户userId。

## Query params
- tenantType (String, required): 接口校验类型，固定值：organization。

## Body
- executorId (String, required): 任务执行者userId。
- objectId (String, required): 对象ID，传项目任务ID，调用创建项目任务接口获取的taskId。
- objectType (String, required): 对象类型，固定值为task，表示项目任务。
- submitterId (String, required): 工时提交人员的userId。
- isDuration (Boolean, required): 当startDate和endDate指定的时间跨天时，添加的工时时长是否平均分配。 - **true**：表示将workTime时长的实际工时平均分配给对应的日期。 - **false**：表示每个日期都添加workTime时长的实际工时。
- includesHolidays (Boolean, required): 添加实际工时的日期是否包含假期。 - **true**：表示日期范围内如果有假期，则假期也添加工时。 - **false**：表示日期范围内如果有假期，则假期不添加工时。
- startDate (String, required): 添加实际工时的开始日期，格式：yyyy-MM-dd。 **[!NOTE]** 实际工时的开始日期不能早于当前日期。
- endDate (String, required): 添加实际工时的结束日期，格式：yyyy-MM-dd。
- workTime (Long, required): 实际工时时长，单位毫秒，1小时即为3600000。 **[!NOTE]** 不超过24小时。
- optional: description(String)

## Returns
- optional: result(Object), ok(Boolean), message(String), body(Array), taskId(String), date(String), workTime(Long)

## Limits
- 实际工时时长，单位毫秒，1小时即为3600000。 **[!NOTE]** 不超过24小时。

source_url: https://open.dingtalk.com/document/development/create-actual-work
updated_at: 2026-06-03 09:29:40
