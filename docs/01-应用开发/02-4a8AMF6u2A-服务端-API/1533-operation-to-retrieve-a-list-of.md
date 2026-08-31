---
title: "获取审批实例ID列表"
source_url: "https://open.dingtalk.com/document/development/operation-to-retrieve-a-list-of"
namespace: "development"
slug: "operation-to-retrieve-a-list-of"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > OA审批 > 获取审批实例ID列表"
doc_id: "TG2aHOIvY1"
updated_at: "2026-08-25 09:37:44"
---

> Source: https://open.dingtalk.com/document/development/operation-to-retrieve-a-list-of
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > OA审批 > 获取审批实例ID列表
> Updated: 2026-08-25 09:37:44

# 获取审批实例ID列表

调用本接口获取权限范围内的相关部门审批实例ID列表。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取审批实例ID列表](0501-obtain-an-approval-list-of-instance-ids.md)接口，已接入用户不受影响。

**调用本接口前，请注意以下限制：**

- 如果只传了**start\_time**参数，这个时间距离当前时间不能超过120天，**end\_time**不传则默认取当前时间。
- 如果传了**start\_time**和**end\_time**，时间范围不能超过120天，同时**start\_time**时间距当前时间不能超过365天。
- 批量获取的实例ID个数（循环获取），最多不能超过10000个。

> **[!NOTE]**
>
> 可以通过本接口获取审批流对应的审批实例ID，然后再调用[获取单个审批实例详情](1535-get-details-single-approval-instance.md)接口，获取审批实例详情信息。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/processinstance/listids`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| process\_code | String | 是 | PROC-FF6Y2xxxx | 审批流的唯一码。  process\_code在审批模板编辑页面的URL中获取。 |
| start\_time | Number | 是 | 1496678400000 | 审批实例开始时间。Unix时间戳，单位毫秒。  例如：获取审批单发起时间在2020.4.10-2020.4.14之间审批单，该值传2020.4.10 00:00:00对应的时间戳1586448000000。 |
| end\_time | Number | 否 | 1496678400000 | 审批实例结束时间，Unix时间戳，单位毫秒。  例如：获取审批单发起时间在2020.4.10-2020.4.14之间审批单，该值传2020.4.14 23:59:59对应的时间戳1586879999000。 |
| size | Number | 否 | 10 | 分页参数，每页大小，最多传20。 |
| cursor | Number | 否 | 0 | 分页查询的游标，最开始传0，后续传返回参数中的next\_cursor值。 |
| userid\_list | String | 否 | manager1,manager2 | 发起userid列表，最大列表长度为10。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageResult |  | 查询结果。 |
| list | String[] | ["1","2"] | 审批实例ID列表。 |
| next\_cursor | Number | 1 | 表示下次查询的游标，当返回结果没有该字段时表示没有更多数据了。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | o3161m2bu22f | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/processinstance/listids?access_token=ACCESS_TOKEN
```

请求正文

```
{
 "end_time":1496678400000,
 "cursor":0,
 "start_time":1496678400000,
 "size":10,
 "process_code":"PROC-FF6Y2xxxx",
 "userid_list":"manager1,manager2"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/processinstance/listids");
OapiProcessinstanceListidsRequest req = new OapiProcessinstanceListidsRequest();
req.setProcessCode("PROC-FF6Y2xxxx");
req.setStartTime(1599148800000L);
req.setEndTime(1599321599000L);
req.setSize(10L);
req.setCursor(0L);
req.setUseridList("manager1,manager2");
OapiProcessinstanceListidsResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "result": {
    "list": [
      "b6a42e32-1867-499c-94f2-xxxx"
    ]
  },
  "errmsg":"ok",
  "request_id": "o3161m2bu22f"
}
```
