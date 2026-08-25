---
title: "获取当前企业所有可管理的表单"
source_url: "https://open.dingtalk.com/document/development/obtains-the-information-about-all-manageable-templates-of-the-current"
namespace: "development"
slug: "obtains-the-information-about-all-manageable-templates-of-the-current"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 获取当前企业所有可管理的表单"
doc_id: "zJGXaU4wLD"
updated_at: "2026-08-25 09:37:47"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-information-about-all-manageable-templates-of-the-current
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 获取当前企业所有可管理的表单
> Updated: 2026-08-25 09:37:47

# 获取当前企业所有可管理的表单

调用本接口，获取在当前企业，该用户可以管理的表单。比如，用户可以管理“审批模板测试”，调用该接口，只能获取到“审批模板测试”表单的信息。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取当前企业所有可管理的表单](0495-get-all-manageable-forms-for-the-current-enterprise.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/template/manage/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | user123 | 用户的userid。  **[!NOTE]**  userid对应的人员必须拥有该企业OA审批的权限。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ProcessSimpleVO[] |  | 模板列表。 |
| icon\_name | String | common | 模板图标名。 |
| flow\_title | String | 通用审批 | 模板名称。 |
| process\_code | String | PROC-44E84FC1-16E2-4A69-BB3C-xxxx | 模板code。 |
| gmt\_modified | Date | 2020-07-14 14:24:59 | 修改时间。 |
| attendance\_type | Number | 0 | 关联考勤类型，取值。   - **0**：无 - **1**：补卡申请 - **2**：请假 |
| icon\_url | String | `https://gw.alicdn.com/tfs/xxxx-112-112.png` | 图标URL地址。 |
| is\_new\_process | Boolean | false | 是否新模板。 |
| success | Boolean | true | 调用是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | o1ud59ekq12g | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/template/manage/get?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "userid":"user123"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/template/manage/get");
OapiProcessTemplateManageGetRequest req = new OapiProcessTemplateManageGetRequest();
req.setUserid("user123");
OapiProcessTemplateManageGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": [
    {
      "attendance_type": 0,
      "flow_title": "物品领用",
      "gmt_modified": "2020-07-14 14:24:59",
      "icon_name": "common",
      "icon_url": "https://gw.alicdn.com/tfs/xxxx-112-112.png",
      "is_new_process": false,
      "process_code": "PROC-E580A0F2-AAAE-4B7C-B42A-xxxx"
    },
    {
      "attendance_type": 0,
      "flow_title": "通用审批",
      "gmt_modified": "2020-07-14 14:24:59",
      "icon_name": "common",
      "icon_url": "https://gw.alicdn.com/tfs/xxxx-112-112.png",
      "is_new_process": false,
      "process_code": "PROC-598BB40C-9C32-4C60-9EA0-xxxx"
    },
    {
      "attendance_type": 0,
      "flow_title": "采购",
      "gmt_modified": "2020-07-14 14:24:59",
      "icon_name": "procurement",
      "icon_url": "https://gw.alicdn.com/tfs/TB1oQi.xxxx-112-112.png",
      "is_new_process": false,
      "process_code": "PROC-44E84FC1-16E2-4A69-BB3C-xxxx"
    }
  ],
  "success": true,
  "request_id": "o1ud59ekq12g"
}
```
