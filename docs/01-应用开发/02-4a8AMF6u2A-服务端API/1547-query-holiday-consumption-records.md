---
title: "批量查询员工假期余额变更记录"
source_url: "https://open.dingtalk.com/document/development/query-holiday-consumption-records"
namespace: "development"
slug: "query-holiday-consumption-records"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 协同办公 > 考勤 > 批量查询员工假期余额变更记录"
doc_id: "SNDjjcI05n"
updated_at: "2026-08-25 09:38:04"
---

> Source: https://open.dingtalk.com/document/development/query-holiday-consumption-records
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 协同办公 > 考勤 > 批量查询员工假期余额变更记录
> Updated: 2026-08-25 09:38:04

# 批量查询员工假期余额变更记录

调用本接口，获取关于某员工的所有假期余额的变更记录，包括假期余额初始化、员工消费额度、假期余额更新记录等。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[批量查询员工假期余额变更记录](0240-batch-query-employee-leave-balance-change-record.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/attendance/vacation/record/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_userid | String | 是 | user01 | 当前企业内拥有**OA审批**应用权限的管理员的userId。 |
| leave\_code | String | 是 | f84a2dxxxx | 假期类型唯一标识，通过[查询假期规则列表](0238-holiday-type-query.md)接口获取leave\_code参数值。 |
| userids | String | 是 | user1,user2 | 待查询员工ID列表，每次调用最多传50个userId。 |
| offset | Number | 是 | 0 | 分页页码，从0开始非负整数。 |
| size | Number | 是 | 10 | 分页大小，最大200。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OapiLeaveRecordListVo |  | 返回结果。 |
| has\_more | Boolean | false | 是否存在更多记录。   - **true**：存在 - **false**：不存在 |
| leave\_records | OapiLeaveRecordVo[] |  | 假期消费记录列表。 |
| userid | String | user1 | 员工的userId。 |
| leave\_code | String | f84a2dxxxx | 假期类型唯一标识。 |
| record\_id | String | db1d74xxxxbaa | 假期消费记录唯一标识。 |
| quota\_id | String | db1d74xxxxbaa | 假期额度唯一标识。 |
| start\_time | Number | 1653851001000 | 额度有效期开始时间，毫秒级时间戳。 |
| end\_time | Number | 1753851001000 | 额度有效期结束时间，毫秒级时间戳。 |
| leave\_view\_unit | String | day | 显示单位。   - **day**：天 - **hour**：小时 |
| cal\_type | String | add | 计算类型。   - **insert**：新纪录 - **add**：新增 - **delete**：删除 - **update**：更新 - **null**（或者不返回该字段）：请假消耗 |
| leave\_reason | String | 管理员导入 | 原因。 |
| leave\_status | String | init | 请假状态。   - **init**：请假申请中 - **success**：请假并已通过 - **refuse**：请假但被被拒 - **abort**：请假撤销 - **revoke**：请假已通过但是撤销了请假并已同意 |
| leave\_record\_type | String | update | 假期记录类型。   - **leave**：请假 - **update**：更新配额 - **modify\_quota**:初始化余额或者更新余额 |
| record\_num\_per\_day | Number | 100 | 以天计算的消费额度。  **[!NOTE]**  假期类型按天计算时，该值不为空且按百分之一天折算。  例如：1000=10天。 |
| record\_num\_per\_hour | Number | 100 | 以小时计算的消费额度。  **[!NOTE]**  假期类型按小时，计算该值不为空且按百分之一小时折算。  例如：1000=10小时。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否正确访问。   - **true**：是 - **false**：不是 |
| request\_id | String | 4jkh6sgf8r1t | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/attendance/vacation/record/list?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "offset":"0",
  "size":"10",
  "userids":"user1,user2",
  "leave_code":"f84a2dxxxx",
  "op_userid":"user01"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/vacation/record/list");
OapiAttendanceVacationRecordListRequest req = new OapiAttendanceVacationRecordListRequest();
req.setOpUserid("user01");
req.setLeaveCode("f84a2dxxxx");
req.setUserids("user1,user2");
req.setOffset(0L);
req.setSize(10L);
OapiAttendanceVacationRecordListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "has_more": false,
    "leave_records": [
      {
        "cal_type": "add",
        "end_time": 1753851001000,
        "leave_code": "f84a2dxxxx",
        "leave_reason": "管理员导入",
        "leave_record_type": "update",
        "record_num_per_hour":100,
        "leave_status": "init",
        "leave_view_unit": "day",
        "quota_id": "dbb41d74xxxxbaa",
        "record_id": "db1d74xxxxbaa",
        "record_num_per_day": 100,
        "start_time": 1653851001000,
        "userid": "user01"
      }
    ]
  },
  "success": true,
  "request_id": "4jkh6sgf8r1t"
}
```
