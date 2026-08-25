---
title: "添加假期规则"
source_url: "https://open.dingtalk.com/document/development/holiday-type-added"
namespace: "development"
slug: "holiday-type-added"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 协同办公 > 考勤 > 添加假期规则"
doc_id: "62jlhMFgNi"
updated_at: "2026-08-25 09:38:02"
---

> Source: https://open.dingtalk.com/document/development/holiday-type-added
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 协同办公 > 考勤 > 添加假期规则
> Updated: 2026-08-25 09:38:02

# 添加假期规则

调用本接口，新建一个假期规则。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[添加假期规则](0233-add-holiday-rules.md)接口，已接入用户不受影响。

> **[!NOTE]**
>
> 创建的假期规则主要有两类：
>
> - 普通假期规则，例如事假、婚假等，此类假期规则可以修改余额。调用本接口创建普通假期后，余额默认是0，需要再调用[初始化假期余额](0236-initialize-holiday-balance.md)接口，初始化假期余额。
> - 调休假期规则，调用本接口添加的调休假期，默认余额规则是**加班时长自动计入调休余额**，无需调用初始化余额接口。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/attendance/vacation/type/create`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| leave\_name | String | 是 | 年假 | 假期名称。 |
| leave\_view\_unit | String | 是 | day | 请假时长单位。   - **day**：天 - **halfDay**：半天 - **hour**：小时 |
| biz\_type | String | 是 | general\_leave | 假期类型。   - **general\_leave**：普通假期 - **lieu\_leave**：加班转调休  **[!NOTE]**  一个企业全局只允许存在一个加班转调休的假期类型。 |
| natural\_day\_leave | Boolean | 是 | true | 是否按照自然日统计请假时长。   - **true**：按照自然日统计请假时长 - **false**：不按照自然日统计请假时长  **[!NOTE]**  当为**false**的时候，用户发起请假时，会根据用户在请假时间段内的排班情况来计算请假时长。 |
| op\_userid | String | 是 | 03085665764167 | 当前企业内拥有**OA审批**应用权限的管理员的userId，否则接口会报错**部门的管理员不存在**。 |
| hours\_in\_per\_day | Number | 是 | 1000 | 每天折算的工作时长，百分之一。例如：1天=10小时=1000。  该参数值一般与企业员工排班工作时长保持一致。 |
| extras | String | 否 | {"validity\_type":"absolute\_time","validity\_value":"12-31"} | 调休假有效期规则   - **validity\_type**：有效类型    - **absolute\_time**：绝对时间   - **relative\_time**：相对时间 - **validity\_value**：延长日期    - 当validity\_type为**absolute\_time**该值该值不为空且满足“yy-mm”格式。   - 当validity\_type为**relative\_time**该值为大于1的整数。  **[!NOTE]**  假期类型biz\_type值为lieu\_leave时，该参数必传。 |
| submit\_time\_rule | Object | 否 |  | 限时提交规则。  **[!NOTE]**  本参数一般用在普通假期类型中，调休假期暂时不使用。 |
| time\_unit | String | 否 | day | 时间单位：   - **day**：天 - **hour**：小时 |
| time\_value | Number | 否 | 1 | 限制值。   - 当timeUnit为**day**时，有效值范围是0至30天； - timeUnit为**hour**时，有效值范围是0至24小时。 |
| time\_type | String | 否 | before | 限制类型：   - **before**：提前 - **after**：补交 |
| enable\_time\_limit | Boolean | 否 | false | 是否开启限时提交功能。   - **true**：开启 - **false**：不开启 |
| leave\_certificate | Object | 否 |  | 请假证明。  **[!NOTE]**  本参数一般用在普通假期类型中，调休假期暂时不使用。 |
| unit | String | 否 | hour | 需提供请假证明时长单位：   - **hour**：小时 - **day**：天 |
| duration | Number | 否 | 1 | 超过多长时间需提供请假证明。   - 如果unit值为day，表示请假超过一天，需要提供请假证明。 - 如果unit值为hour，表示请假超过一小时，需要提供请假证明。  **[!NOTE]**  提交请假超过设置时间，审批单会自动出现请假证明填写项。请假证明 |
| enable | Boolean | 否 | false | 是否开启请假证明。   - **true**：开启 - **false**：不开启 |
| prompt\_information | String | 否 | 请假信息 | 请假提示文案。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 错误码。 |
| errmsg | String | 成功 | 错误消息。 |
| success | Boolean | true | 是否正确访问。   - **true**：是 - **false**：不是 |
| result | Object |  | 业务结果。 |
| leave\_name | String | 年假 | 假期名称。 |
| leave\_code | String | 037477ae-1009-4632-b8e9-e919ae5e7973 | 假期规则唯一标识。 |
| leave\_view\_unit | String | day | 请假单位。   - **day**：天 - **halfDay**：半天 - **hour**：小时 |
| biz\_type | String | general\_leave | 假期类型。   - **general\_leave**：普通假期 - **lieu\_leave**：加班转调休 |
| natural\_day\_leave | Boolean | true | 是否按照自然日统计请假时长。   - **true**：按照自然日统计请假时长。 - **false**：不按照自然日统计请假时长。  **[!NOTE]**  当为**false**的时候，用户发起请假时，会根据用户在请假时间段内的排班情况来计算请假时长。 |
| hours\_in\_per\_day | Number | 1000 | 每天折算的工作时长，百分之一。  例如：1天=10小时=1000。 |
| submit\_time\_rule | Object | {"enableTimeLimit":true,"timeType":"before","timeUnit":"day","timeValue":1} | 限时提交规则，请求携带了submit\_time\_rule参数，才会返回该字段。 |
| time\_value | Number | 1 | 限制值。   - 当timeUnit为**day**时，有效值范围是0至30天； - timeUnit为**hour**时，有效值范围是0至24小时。 |
| time\_unit | String | day | 时间单位：   - **day**：天 - **hour**：小时 |
| time\_type | String | before | 限制类型：   - **before**：提前 - **after**：补交 |
| enable\_time\_limit | Boolean | false | 是否开启限时提交功能。   - **true**：开启 - **false**：不开启 |
| leave\_certificate | Object |  | 请假证明，请求携带了leave\_certificate参数，才会返回该字段。 |
| unit | String | hour | 需提供请假证明时长单位：   - **hour**：小时 - **day**：天 |
| duration | Number | 1 | 超过多长时间需提供请假证明。 |
| enable | Boolean | false | 是否开启请假证明。   - **true**：开启 - **false**：不开启 |
| prompt\_information | String | 请假信息 | 请假提示文案。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/attendance/vacation/type/create?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "when_can_leave":"entry",
  "leave_time_ceil_min_unit":"hour",
  "visibility_rules":{
    "visible":"userid1,userid2",
    "type":"staff"
  },
  "leave_view_unit":"day",
  "leave_name":"年假",
  "biz_type":"general_leave",
  "min_leave_hour":"2",
  "extras":"{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}",
  "freedom_leave":"false",
  "submit_time_rule":{
    "enable_time_limit":"false",
    "time_type":"before",
    "time_value":"1",
    "time_unit":"day"
  },
  "op_userid":"03085665764167",
  "natural_day_leave":"true",
  "paid_leave":"true",
  "leave_time_ceil":"false",
  "hours_in_per_day":"1000",
  "leave_hour_ceil":"up",
  "leave_certificate":{
    "duration":"1",
    "unit":"hour",
    "enable":"false",
    "prompt_information":"请假信息"
  },
  "max_leave_time":"1"
}
```

**请求示例（JAVA SDK）**

```
public class Main {
  public static void main(String[] args) {
    try {
      DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/vacation/type/create");
      OapiAttendanceVacationTypeCreateRequest req = new OapiAttendanceVacationTypeCreateRequest();
      OapiAttendanceVacationTypeCreateResponse rsp = client.execute(req, "");
      System.out.println(rsp.getBody());
    } catch (ApiException e) {
      e.printStackTrace();
    }
  }
}
```

**返回示例**

```
{
  "errcode":"0",
  "result":{
    "when_can_leave":"entry",
    "leave_time_ceil_min_unit":"hour",
    "visibility_rules":{
      "visible":"userid1,userid2",
      "type":"staff"
    },
    "leave_view_unit":"day",
    "leave_name":"年假",
    "biz_type":"general_leave",
    "min_leave_hour":"2",
    "freedom_leave":"false",
    "submit_time_rule":{
      "enable_time_limit":"false",
      "time_type":"before",
      "time_value":"1",
      "time_unit":"day"
    },
    "natural_day_leave":"true",
    "paid_leave":"true",
    "leave_time_ceil":"false",
    "hours_in_per_day":"1000",
    "leave_hour_ceil":"up",
    "leave_code":"037477ae-1009-4632-b8e9-e919ae5e7973",
    "leave_certificate":{
      "duration":"1",
      "unit":"hour",
      "enable":"false",
      "prompt_information":"请假信息"
    },
    "max_leave_time":"1"
  },
  "success":"true",
  "errmsg":"成功"
}
```
