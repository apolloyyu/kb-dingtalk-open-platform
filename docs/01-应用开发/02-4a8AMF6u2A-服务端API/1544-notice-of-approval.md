---
title: "通知审批通过"
source_url: "https://open.dingtalk.com/document/development/notice-of-approval"
namespace: "development"
slug: "notice-of-approval"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 协同办公 > 考勤 > 通知审批通过"
doc_id: "Vd5m7BSpe4"
updated_at: "2026-08-25 09:38:01"
---

> Source: https://open.dingtalk.com/document/development/notice-of-approval
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 协同办公 > 考勤 > 通知审批通过
> Updated: 2026-08-25 09:38:01

# 通知审批通过

通过本接口，通知审批通过，支持加班、请假、外出和出差类型。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[通知审批通过](0226-api-processapprovefinish.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/attendance/approve/finish`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager123 | 员工的userId。 |
| biz\_type | Number | 是 | 3 | 审批单类型：   - **1**：加班 - **2**：出差、外出 - **3**：请假 |
| from\_time | String | 是 | 2019-08-15 | 开始时间。开始时间不能早于当前时间前31天。  支持以下格式：   - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43 |
| to\_time | String | 是 | 2019-08-17 | 结束时间。  支持以下格式：   - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43   **[!NOTE]**   - 结束时间减去开始时间的天数不能超过31天。 - biz\_type为1时，结束时间减去开始时间的天数不能超过1天。 |
| duration\_unit | String | 是 | day | 时长单位，支持格式如下：   - day - halfDay - hour：biz\_type为1时仅支持hour。   时间格式必须与时长单位对应：   - 2019-08-15对应day - 2019-08-15 AM对应halfDay - 2019-08-15 12:43对应hour |
| calculate\_model | Number | 是 | 1 | 计算方法：   - **0**：按自然日计算 - **1**：按工作日计算 |
| tag\_name | String | 是 | 请假 | 审批单类型名称，最大长度20个字符。  支持类型如下：   - 请假 - 出差 - 外出 - 加班 |
| sub\_type | String | 否 | 年假 | 子类型名称，最大长度20个字符。  **[!NOTE]**  审批单类型biz\_type=3时，该参数必传。 |
| approve\_id | String | 是 | 1234abcd | 审批单ID，最大长度100个字符，自定义值。 |
| jump\_url | String | 是 | https://open.dingtalk.com/ | 审批单跳转地址，最大长度200个字符。 |
| overtime\_duration | String | 否 | 1.07 | biz\_type为1时必传，加班时长单位小时。 |
| overtime\_to\_more | Number | 否 | 1 | biz\_type为1时必传：   - **1**：加班转调休 - **2**：加班转工资 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | TopDurationVo |  | 返回结果。 |
| duration | String | 2.0 | 总时长。 |
| durationDetail | TopDayDurationVo[] |  | 详细信息。 |
| date | String | 2019-08-15 | 审批通过日期。 |
| duration | String | 1.0 | 每日时长。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/attendance/approve/finish?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "jump_url":"https://open.dingtalk.com/",
  "sub_type":"年假",
  "overtime_duration":"1.07",
  "tag_name":"请假",
  "biz_type":"3",
  "calculate_model":"1",
  "approve_id":"1234abcd",
  "to_time":"2019-08-17",
  "overtime_to_more":"1",
  "userid":"dd_dd",
  "from_time":"2019-08-15",
  "duration_unit":"day"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/approve/finish");
OapiAttendanceApproveFinishRequest req = new OapiAttendanceApproveFinishRequest();
req.setUserid("dd_dd");
req.setBizType(3L);
req.setFromTime("2019-08-15");
req.setToTime("2019-08-17");
req.setDurationUnit("day");
req.setCalculateModel(1L);
req.setTagName("请假");
req.setSubType("年假");
req.setApproveId("1234abcd");
req.setJumpUrl("https://open.dingtalk.com/");
req.setOvertimeDuration("1.07");
req.setOvertimeToMore(1L);
OapiAttendanceApproveFinishResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode":0,
  "errmsg":"ok",
  "result":{
    "duration":"2.0",
    "durationDetail":[
      {
        "date":"2019-08-15",
        "duration":"1.0"
      }
    ]
  }
}
```
