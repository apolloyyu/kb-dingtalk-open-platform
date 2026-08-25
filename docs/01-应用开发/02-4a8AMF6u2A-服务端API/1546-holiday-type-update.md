---
title: "更新假期规则"
source_url: "https://open.dingtalk.com/document/development/holiday-type-update"
namespace: "development"
slug: "holiday-type-update"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 协同办公 > 考勤 > 更新假期规则"
doc_id: "pTHaZZt15p"
updated_at: "2026-08-25 09:38:03"
---

> Source: https://open.dingtalk.com/document/development/holiday-type-update
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 协同办公 > 考勤 > 更新假期规则
> Updated: 2026-08-25 09:38:03

# 更新假期规则

调用本接口，更新指定假期的相关规则。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[更新假期规则](0234-update-holiday-rules.md)接口，已接入用户不受影响。

## **接口调用说明**

创建假期规则有2种方式，通过调用接口创建、通过钉钉官方应用考勤产品创建：

| 创建假期规则方式 | 调用本接口是否支持更新假期类型 |
| --- | --- |
| 方式一：调用[添加假期规则](1545-holiday-type-added.md)接口创建的假期类型 | 支持 |
| 方式二：钉钉管理后台考勤应用创建的假期类型   - 考勤应用系统默认创建 - 通过考勤应用后台创建 | 不支持 |

如下图所示，在**考勤应用 > 假期管理 > 假期规则**页面，可以查看共4个假期规则。

- 接口添加的假期1、接口添加的假期2，是通过接口创建的假期类型。调用本接口，可以更新假期相关的信息，包括假期名称、请假单位、计算请假时长方式等。
- 事假、调休，是考勤应用系统默认创建的假期类型。调用本接口，无法更新假期类型，报以下错误信息：errcode:880015, errmsg:批量leaveCode或userId都不存在。![考勤-服务端API-更新假期类型1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7747369361/p369550.png)

  > **[!NOTE]**
  >
  > 查询哪些假期规则是通过调用接口创建的，可调用[查询假期规则列表](0238-holiday-type-query.md)接口获取。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/attendance/vacation/type/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_userid | String | 是 | user01 | 当前企业内拥有**OA审批**应用权限的管理员的userId。 |
| leave\_name | String | 否 | 年假 | 假期名称。 |
| leave\_view\_unit | String | 否 | day | 请假单位。   - **day**：天 - **halfDay**：半天 - **hour**：小时 |
| biz\_type | String | 否 | general\_leave | 假期类型。   - **general\_leave**：普通假期 - **lieu\_leave**：加班转调休 |
| natural\_day\_leave | Boolean | 否 | true | 是否按照自然日统计请假时长。   - **true**：按照自然日统计请假时长 - **false**：不按照自然日统计请假时长  **[!NOTE]**  当为**false**时，用户发起请假时，会根据用户在请假时间段内的排班情况来计算请假时长。 |
| leave\_code | String | 是 | f8ddsdxxxx | 接口添加的假期规则标识，  **[!NOTE]**  leave\_code必须是通过[添加假期规则](1545-holiday-type-added.md)接口添加的假期类型。 |
| hours\_in\_per\_day | Number | 否 | 1000 | 每天折算的工作时长，百分之一。例如：1天=10小时=1000。 |
| extras | String | 否 | {"validity\_type":"absolute\_time","validity\_value":"12-31"} | 调休假有效期规则。   - **validity\_type**：有效类型    - **absolute\_time**：绝对时间   - **relative\_time**：相对时间 - **validity\_value**：延长日期    - 当validity\_type为**absolute\_time**该值该值不为空且满足“yy-mm”格式。   - 当validity\_type为**relative\_time**该值为大于1的整数。 |
| leave\_certificate | LeaveCertificateVo | 否 |  | 请假证明。 |
| leave\_certificate.unit | String | 否 | hour | 请假证明单位。   - **hour**：小时 - **day**：天 |
| leave\_certificate.duration | Number | 否 | 1 | 超过多长时间需提供请假证明。 |
| leave\_certificate.enable | Boolean | 否 | false | 是否开启请假证明。   - **true**：开启 - **false**：不开启 |
| leave\_certificate.prompt\_information | String | 否 | 请假信息 | 请假提示文案。 |
| submit\_time\_rule | SubmitTimeRuleVo | 否 |  | 限时提交规则。 |
| submit\_time\_rule.time\_value | Number | 否 | 18 | 限制值。   - 当timeUnit为**day**时，有效值范围是0至30天； - timeUnit为**hour**时，有效值范围是0至24小时。 |
| submit\_time\_rule.time\_unit | String | 否 | hour | 时间单位。   - **day**：天 - **hour**：小时 |
| submit\_time\_rule.time\_type | String | 否 | before | 限制类型。   - **before**：提前 - **after**：补交 |
| submit\_time\_rule.enable\_time\_limit | Boolean | 否 | false | 是否开启限时提交功能。   - **true**：开启 - **false**：不开启 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 10tg0hlcqinnn | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| success | Boolean | true | 是否正确访问。   - **true**：是 - **false**：不是 |
| result | LeaveTypeVo |  | 返回结果。 |
| leave\_name | String | 年假 | 假期名称。 |
| leave\_code | String | f8ddsdxxxx | 假期规则唯一标识。 |
| leave\_view\_unit | String | day | 请假单位。   - **day**：天 - **halfDay**：半天 - **hour**：小时 |
| leave\_certificate | LeaveCertificateVo |  | 请假证明。 |
| leave\_certificate.unit | String | hour | 请假证明单位。   - **hour**：小时 - **day**：天 |
| leave\_certificate.duration | Number | 1 | 超过多长时间需提供请假证明。 |
| leave\_certificate.enable | Boolean | false | 是否开启请假证明。   - **true**：开启 - **false**：不开启 |
| leave\_certificate.prompt\_information | String | 请假信息 | 请假提示文案。 |
| submit\_time\_rule | SubmitTimeRuleVo |  | 限时提交规则。 |
| submit\_time\_rule.time\_value | Number | 18 | 限制值。   - 当timeUnit为**day**时，有效值范围是0至30天； - timeUnit为**hour**时，有效值范围是0至24小时。 |
| submit\_time\_rule.time\_unit | String | hour | 时间单位。   - **day**：天 - **hour**：小时 |
| submit\_time\_rule.time\_type | String | before | 限制类型。   - **before**：提前 - **after**：补交 |
| submit\_time\_rule.enable\_time\_limit | Boolean | false | 是否开启限时提交功能。   - **true**：开启 - **false**：不开启 |
| biz\_type | String | general\_leave | 假期类型。   - **general\_leave**：普通假期 - **lieu\_leave**：加班转调休 |
| natural\_day\_leave | Boolean | true | 是否按照自然日统计请假时长。   - **true**：按照自然日统计请假时长。 - **false**：不按照自然日统计请假时长。  **[!NOTE]**  当为**false**时，用户发起请假时，会根据用户在请假时间段内的排班情况来计算请假时长。 |
| hours\_in\_per\_day | Number | 1000 | 每天折算的工作时长，百分之一。  例如：1天=10小时=1000。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/attendance/vacation/type/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "natural_day_leave": true,
  "leave_view_unit": "day",
  "hours_in_per_day": 1000,
  "leave_name": "年假",
  "biz_type": "general_leave",
  "extras": "{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}",
  "leave_code": "f8ddsdxxxx",
  "op_userid": "user01",
  "leave_certificate": {
    "unit": "hour",
    "duration": 1,
    "enable": false,
    "prompt_information": "请假信息"
  },
  "submit_time_rule": {
    "time_value": 18,
    "time_unit": "day",
    "time_type": "before",
    "enable_time_limit": false
  }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/vacation/type/update");
OapiAttendanceVacationTypeUpdateRequest req = new OapiAttendanceVacationTypeUpdateRequest();
req.setOpUserid("user01");
req.setLeaveName("年假");
req.setLeaveViewUnit("day");
req.setBizType("general_leave");
req.setNaturalDayLeave(true);
req.setLeaveCode("f8ddsdxxxx");
req.setHoursInPerDay(1000L);
req.setExtras("{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}");
SubmitTimeRuleVo SubmitTimeRuleVo= new SubmitTimeRuleVo();
SubmitTimeRuleVo.setTimeType("before");
SubmitTimeRuleVo.setTimeValue(18L);
SubmitTimeRuleVo.setEnableTimeLimit(true);
SubmitTimeRuleVo.setTimeUnit("hour");
req.setSubmitTimeRule(SubmitTimeRuleVo);
LeaveCertificateVo leaveCertificateVo= new LeaveCertificateVo();
leaveCertificateVo.setUnit("hour");
leaveCertificateVo.setDuration(1L);
leaveCertificateVo.setEnable(false);
leaveCertificateVo.setPromptInformation("请假信息");
req.setLeaveCertificate(leaveCertificateVo);
OapiAttendanceVacationTypeUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "result": {
    "biz_type": "general_leave",
    "hours_in_per_day": 1000,
    "leave_code": "f8ddsdxxxx",
    "leave_name": "年假",
    "leave_view_unit": "day",
    "leave_certificate": {
      "unit": "hour",
      "duration": 1,
      "enable": false,
      "prompt_information": "请假信息"
    },
    "submit_time_rule": {
      "time_value": 18,
      "time_unit": "day",
      "time_type": "before",
      "enable_time_limit": false
    },
    "natural_day_leave": true
  },
  "success": true,
  "request_id": "10tg0hlcqinnn"
}
```
