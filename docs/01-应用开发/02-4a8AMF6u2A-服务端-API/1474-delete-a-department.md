---
title: "删除部门"
source_url: "https://open.dingtalk.com/document/development/delete-a-department"
namespace: "development"
slug: "delete-a-department"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 部门管理1.0(不推荐) > 删除部门"
doc_id: "ZnQICRSq6u"
updated_at: "2026-08-25 09:37:03"
---

> Source: https://open.dingtalk.com/document/development/delete-a-department
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 通讯录管理 > 部门管理1.0(不推荐) > 删除部门
> Updated: 2026-08-25 09:37:03

# 删除部门

调用本接口根据部门ID删除指定部门。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[删除部门](0079-address-book-deletion-department.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/department/delete`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |
| id | String | 是 | 123 | 部门ID，可调用[获取部门列表](1469-obtain-the-department-list.md)接口获取。  **[!NOTE]**  以下情况无法删除部门：   - 不能删除根部门，即部门ID为1。 - 部门或子部门内还有未删除的员工。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/department/delete?access_token=ACCESS_TOKEN&id=123
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/department/delete");
OapiDepartmentDeleteRequest req = new OapiDepartmentDeleteRequest();
req.setId("123");
req.setHttpMethod("GET");
OapiDepartmentDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode":0,
  "errmsg":"ok"
}
```
