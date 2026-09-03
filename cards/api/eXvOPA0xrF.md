# 创建计划工时

doc_id: eXvOPA0xrF
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/project/users/{userId}/planTimes
api_version: v2-new
app_types: 第三方企业应用
permissions: Project.Task.Write.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 操作者userId。

## Query params
- tenantType (String, required): 接口校验类型，目前为固定值：organization。

## Body
- executorId (String, required): 目标任务执行者的userId。
- objectId (String, required): 对象ID，传项目任务ID，调用创建项目任务接口获取的taskId。
- objectType (String, required): 对象类型，固定值为task，表示项目任务。
- isDuration (Boolean, required): 当startDate和endDate指定的时间跨天时，添加的工时时长是否平均分配。 - **true**：表示将planTime时长的计划工时平均分配给对应的日期。 - **false**：表示每个日期都添加planTime时长的计划工时。
- includesHolidays (Boolean, required): 添加计划工时的日期是否包含假期。 - **true**：表示日期范围内如果有假期，则假期也添加工时。 - **false**：表示日期范围内如果有假期，则假期不添加工时。
- submitterId (String, required): 工时提交人员的userId。
- startDate (String, required): 开始日期，格式：yyyy-MM-dd。
- endDate (String, required): 结束时间，格式：yyyy-MM-dd。
- planTime (Long, required): 计划工时时长，单位毫秒，1小时即为3600000。 **[!NOTE]** 不超过24小时。

## Returns
- optional: result(Object), ok(Boolean), message(String), body(Array), objectId(String), date(String), planTime(Long)

## Limits
- 计划工时时长，单位毫秒，1小时即为3600000。 **[!NOTE]** 不超过24小时。

source_url: https://open.dingtalk.com/document/development/create-planned-work
updated_at: 2026-06-03 09:29:38
