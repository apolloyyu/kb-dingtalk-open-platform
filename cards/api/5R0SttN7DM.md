# 排班制考勤组排班

doc_id: 5R0SttN7DM
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/schedule/async
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_attendance_group_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- op_user_id (String, required): 操作人userId。
- group_id (Number, required): 考勤组ID。 **[!NOTE]** 如果你使用的是旧考勤组标识即group_key，可以调用groupKey转换为groupId接口将group_key转换为group_id。
- schedules (TopScheduleParam[], required): 排班详情。示例如下： ``` { "is_rest": false, "work_date": 1605150671000, "shift_id": 1, "userid": "user123" } ``` **[!NOTE]** 最大列表长度200。
- shift_id (Number, required): 班次ID，休息班次传1，可通过获取班次摘要信息接口获取id参数值。 **[!NOTE]** - 当is_rest参数传true时，shift_id传1。 - 如果你需要清空排班，shift_id传 -2。
- work_date (Number, required): 排班日期。 **[!NOTE]** 可排班日期不早于180天前，不晚于180天后。
- userid (String, required): 用户的userId。
- optional: is_rest(Boolean)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 排班详情。示例如下： ``` { "is_rest": false, "work_date": 1605150671000, "shift_id": 1, "userid": "user123" } ``` **[!NOTE]** 最大列表长度200。
- 排班日期。 **[!NOTE]** 可排班日期不早于180天前，不晚于180天后。

source_url: https://open.dingtalk.com/document/development/scheduling-system-attendance-group-scheduling
updated_at: 2026-05-27 17:06:08
