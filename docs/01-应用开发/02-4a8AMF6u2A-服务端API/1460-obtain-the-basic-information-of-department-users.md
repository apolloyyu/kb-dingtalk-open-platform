---
title: "获取部门用户基础信息"
source_url: "https://open.dingtalk.com/document/development/obtain-the-basic-information-of-department-users"
namespace: "development"
slug: "obtain-the-basic-information-of-department-users"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 获取部门用户基础信息"
doc_id: "5bintD8CMc"
updated_at: "2026-08-25 09:36:52"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-basic-information-of-department-users
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 获取部门用户基础信息
> Updated: 2026-08-25 09:36:52

# 获取部门用户基础信息

调用本接口获取部门下的用户列表，该接口仅返回用户的userid和name。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取部门用户基础信息](0066-queries-the-simple-information-of-a-department-user.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/user/simplelist`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |
| lang | String | 否 | zh\_CN | 通讯录语言，默认为zh\_CN。如果是英文，请输入en\_US。 |
| department\_id | Number | 是 | 1 | 获取的部门ID。1表示根部门。 |
| offset | Number | 否 | 1 | 支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。 |
| size | Number | 否 | 1 | 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。 |
| order | String | 否 | entry\_asc | 支持分页查询，部门成员的排序规则，默认不传是按自定义排序：   - **entry\_asc**：代表按照进入部门的时间升序 - **entry\_desc**：代表按照进入部门的时间降序 - **modify\_asc**：代表按照部门信息修改时间升序 - **modify\_desc**：代表按照部门信息修改时间降序 - **custom**：代表用户定义(未定义时按照拼音)排序 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| userlist | Userlist[] |  | 成员列表。 |
| userid | String | 662200077 | 员工userid。 |
| name | String | 张x | 员工姓名。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| hasMore | Boolean | false | 在分页查询时返回，代表是否还有下一页更多数据。   - **false**：无下一页数据 - **true**：有下一页数据 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/user/simplelist?access_token=ACCESS_TOKEN&lang=zh_CN&department_id=1&offset=1&size=1&order=entry_asc
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/simplelist");
OapiUserSimplelistRequest req = new OapiUserSimplelistRequest();
req.setLang("zh_CN");
req.setDepartmentId(1L);
req.setOffset(1L);
req.setSize(1L);
req.setOrder("entry_asc");
req.setHttpMethod("GET");
OapiUserSimplelistResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "hasMore": false,
    "errmsg": "ok",
    "userlist": [
        {
            "name": "张x",
            "userid": "662200077"
        }
    ]
}
```
