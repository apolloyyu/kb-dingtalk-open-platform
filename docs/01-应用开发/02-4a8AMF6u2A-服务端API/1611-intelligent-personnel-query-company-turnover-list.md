---
title: "获取离职员工列表"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-query-company-turnover-list"
namespace: "development"
slug: "intelligent-personnel-query-company-turnover-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 智能人事 > 员工管理 > 获取离职员工列表"
doc_id: "zEgGjCM3r4"
updated_at: "2026-08-25 09:39:09"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-query-company-turnover-list
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 智能人事 > 员工管理 > 获取离职员工列表
> Updated: 2026-08-25 09:39:09

# 获取离职员工列表

调用本接口，查询企业离职员工userid列表。

> **[!IMPORTANT]**
>
> - 浏览器可能会转义某些字符导致请求失败，调试时请使用curl或者代码模拟请求。
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取离职员工列表](0947-obtain-the-list-of-employees-who-have-left.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/querydimission`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| offset | Number | 是 | 0 | 分页游标，从0开始。根据返回结果里的next\_cursor是否为空来判断是否还有下一页，且再次调用时offset设置成next\_cursor的值。 |
| size | Number | 是 | 50 | 分页大小，最大50。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Paginator |  | 返回结果。 |
| next\_cursor | Number | 8 | 下一次分页调用的offset值，当返回结果里没有nextCursor时，表示分页结束。 |
| data\_list | String[] | ["user123","user456"] | 离职人员userid列表。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码信息 |
| success | Boolean | true | 是否调用成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | nlmt2e4evxi0 | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/querydimission?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "offset":0,
  "size":50
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/querydimission");
OapiSmartworkHrmEmployeeQuerydimissionRequest req = new OapiSmartworkHrmEmployeeQuerydimissionRequest();
req.setOffset(0L);
req.setSize(50L);
OapiSmartworkHrmEmployeeQuerydimissionResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "data_list": [
      "ud",
      "001",
      "yy7",
      "yy6",
      "yy2"
    ],
    "next_cursor": 8
  },
  "success": true,
  "request_id": "7dnyz9kld0lw"
}
```
