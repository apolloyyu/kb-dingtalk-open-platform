---
title: "获取员工花名册字段信息"
source_url: "https://open.dingtalk.com/document/development/obtain-employee-roster-field-information-in-batches"
namespace: "development"
slug: "obtain-employee-roster-field-information-in-batches"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 智能人事 > 花名册 > 获取员工花名册字段信息"
doc_id: "oDo9jHRGQQ"
updated_at: "2026-08-25 09:39:06"
---

> Source: https://open.dingtalk.com/document/development/obtain-employee-roster-field-information-in-batches
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 智能人事 > 花名册 > 获取员工花名册字段信息
> Updated: 2026-08-25 09:39:06

# 获取员工花名册字段信息

调用本接口根据员工userid批量获取员工花名册字段信息。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取员工花名册字段信息](0939-api-getemployeerosterbyfield.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端接口的授权凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid\_list | String | 是 | "manager4220,User123" | 员工userid列表，最大列表长度为50。 |
| field\_filter\_list | String | 否 | "hrm-sys01-employeeStatus, hrm-sys01-regularTime" | 需要获取的花名册字段列表，最大列表长度为20。  **[!NOTE]**  不传入该参数时，企业可获取所有字段信息。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | EmpFieldInfoVO[] |  | 返回结果。 |
| userid | String | 2 | 员工的userid。 |
| field\_list | EmpFieldVO[] |  | 字段信息列表。 |
| group\_id | String | sys00 | 字段分组ID。 |
| value | String | 2 | 字段值。 |
| field\_code | String | sys01-employeeStatus | 字段编码。 |
| field\_name | String | 姓名 | 字段业务名称。 |
| label | String | 试用 | 对应value的文本值。  当value为枚举值时，label取值为value的文本翻译；否则，label取值同value。 |
| partner | Boolean | false | 是否是合伙伙伴：   - false：不是 - true：是 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | false | 调用是否成功。 |
| request\_id | String | 5lbpbu5btcu6 | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/list?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "field_filter_list":"[\"hrm-sys01-employeeStatus\", \"hrm-sys01-regularTime\"]",
  "agentid":"1",
  "userid_list":"[\"1\", \"2\", \"3\"]"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/list");
OapiSmartworkHrmEmployeeListRequest req = new OapiSmartworkHrmEmployeeListRequest();
req.setUseridList("1, 2, 3");
req.setFieldFilterList("hrm-sys01-employeeStatus, hrm-sys01-regularTime");
req.setAgentid(1L);
OapiSmartworkHrmEmployeeListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": [
    {
      "field_list": [
        {
          "field_code": "sys00-name",
          "field_name": "姓名",
          "group_id": "sys00",
          "label": "杨xx",
          "value": "杨xx"
        },
        {
          "field_code": "sys00-email",
          "field_name": "邮箱",
          "group_id": "sys00",
          "label": "1@example.com",
          "value": "1@example.com"
        }
      ],
      "partner": false,
      "userid": "manager4220"
    }
  ],
  "success": true,
  "request_id": "5lbpbu5btcu6"
}
```
