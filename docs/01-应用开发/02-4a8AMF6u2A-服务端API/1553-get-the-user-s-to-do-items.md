---
title: "查询企业下用户待办列表"
source_url: "https://open.dingtalk.com/document/development/get-the-user-s-to-do-items"
namespace: "development"
slug: "get-the-user-s-to-do-items"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 待办任务 > 查询企业下用户待办列表"
doc_id: "jLH3GTXgM6"
updated_at: "2026-08-25 09:38:12"
---

> Source: https://open.dingtalk.com/document/development/get-the-user-s-to-do-items
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 待办任务 > 查询企业下用户待办列表
> Updated: 2026-08-25 09:38:12

# 查询企业下用户待办列表

调用本接口分页获取用户的待办任务列表。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[查询企业下用户待办列表](0798-query-the-to-do-list-of-enterprise-users.md)接口，已接入用户不受影响。

## 权限

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/workrecord/getbyuserid`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager7080 | 要查询的用户userid。 |
| offset | Number | 是 | 0 | 分页游标，从0开始，如返回结果中has\_more为true，则表示还有数据，offset再传上一次的offset+limit。 |
| limit | Number | 是 | 50 | 分页大小，最多50。 |
| status | Number | 是 | 0 | 待办任务状态：   - **0**：未完成 - **1**：完成 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 51ynzjcpw72k | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| records | PageResult |  | 查询结果。 |
| has\_more | Boolean | true | 是否有更多数据：   - **true**：有 - **false**：没有 |
| list | WorkRecordVo[] |  | 待办列表。 |
| record\_id | String | recordbc83ea0f6ae83aee9 | 待办任务ID。 |
| create\_time | Number | 1599580799000 | 待办任务发起时间。 |
| title | String | 学习任务 | 待办标题。 |
| url | String | https://oa.dingtalk.com | 待办跳转链接。 |
| forms | FormItemVo[] | 表单 | 待办表单内容。 |
| title | String | 新人学习 | 表单标题。 |
| content | String | 产品学习 | 表单内容。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/workrecord/getbyuserid?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "offset":"0",
  "limit":"50",
  "userid":"manager7080",
  "status":"0"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/workrecord/getbyuserid");
OapiWorkrecordGetbyuseridRequest req = new OapiWorkrecordGetbyuseridRequest();
req.setUserid("manager7080");
req.setOffset(0L);
req.setLimit(50L);
req.setStatus(0L);
OapiWorkrecordGetbyuseridResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "records": {
    "has_more": true,
    "list": [
      {
        "create_time": 1599580799000,
        "forms": [
          {
            "content": "产品学习",
            "title": "新人学习2"
          }
        ],
        "record_id": "recordbc83ea0f6ae83aee95c4812119eea02a",
        "title": "学习任务",
        "url": "https://oa.dingtalk.com"
      },
      {
        "create_time": 1599580799000,
        "forms": [
          {
            "content": "规章制度学习",
            "title": "新人学习"
          }
        ],
        "record_id": "recordf1c4ac14f4c111cf015ead5b6642543a",
        "title": "title",
        "url": "https://oa.dingtalk.com"
      }
    ]
  },
  "request_id": "zpuar3sisl86"
}
```

## 错误码

| 错误码 | 错误码说明 | 排查方法 |
| --- | --- | --- |
| 40068 | 无效的offset | offset不能小于0。 |
| 40069 | 无效的limit | limit必须在0和50之间。 |
| 33012 | 无效的userid | 请检查userid参数是否合法。 |
