---
title: "获取员工人数"
source_url: "https://open.dingtalk.com/document/development/obtain-the-number-of-employees"
namespace: "development"
slug: "obtain-the-number-of-employees"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 获取员工人数"
doc_id: "bcTJZWhDZr"
updated_at: "2026-08-25 09:36:54"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-number-of-employees
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 获取员工人数
> Updated: 2026-08-25 09:36:54

# 获取员工人数

调用本接口获取企业员工的人数。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取员工人数](0059-user-management-acquires-number-employees.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/user/get_org_user_count`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1bxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |
| onlyActive | Number | 是 | 0 | 是否包含激活人数：   - **0**：包含未激活钉钉的人员数量 - **1**：不包含未激活钉钉的人员数量 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| count | Number | 100 | 企业员工数量。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/user/get_org_user_count?access_token=ACCESS_TOKEN&onlyActive=0
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/get_org_user_count");
OapiUserGetOrgUserCountRequest req = new OapiUserGetOrgUserCountRequest();
req.setOnlyActive(0L);
req.setHttpMethod("GET");
OapiUserGetOrgUserCountResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "count":100,
        "errmsg":"ok"
}
```
