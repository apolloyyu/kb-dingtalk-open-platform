---
title: "查询企业通讯录未激活用户列表"
source_url: "https://open.dingtalk.com/document/development/queries-the-list-of-inactive-accounts-in-the-key-account"
namespace: "development"
slug: "queries-the-list-of-inactive-accounts-in-the-key-account"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据统计 > 查询企业通讯录未激活用户列表"
doc_id: "SqloR8V79e"
updated_at: "2025-09-08 19:05:37"
---

> Source: https://open.dingtalk.com/document/development/queries-the-list-of-inactive-accounts-in-the-key-account
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据统计 > 查询企业通讯录未激活用户列表
> Updated: 2025-09-08 19:05:37

# 查询企业通讯录未激活用户列表

调用本接口查询当前企业当前通讯录未激活用户明细列表。

> **[!IMPORTANT]**
>
> 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的[数据资产类OpenAPI](https://open.dingtalk.com/document/dataservice/data-asset-interface-adjustment-description)接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)获取相应的数据服务。
> 2. 本文档已于 2023 年 9 月 1 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力，说明如下：
>
>    - 如果未使用本接口，推荐使用[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。
>    - 如果已使用本接口，建议您根据自身实际情况评估是否切换至[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。

![iShot2021-12-21 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6155700461/p372100.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 钉钉数据产品权限包 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/kac/datav/inactivated/user/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | UnactivatedUserRequest | 是 |  | 请求对象。 |
| data\_id | String | 是 | 20200501 | 日期标识。 |
| size | Number | 是 | 10 | 分页大小，不超过100。 |
| cursor | Number | 是 | 0 | 分页游标，首页请使用0，之后直接使用返回结果中next\_cursor的值。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 6v4qtgo9a6q0 | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | UnactivatedUserResponse |  | 返回结果。 |
| data | UnactivatedUserVo[] |  | 返回数据列表。 |
| dept\_id | Number | 1 | 部门id。 |
| dept\_name | String | 技术部 | 部门名称。 |
| userid | String | 123 | 员工userid。 |
| staff\_job\_num | String | 1001 | 员工工号。 |
| staff\_name | String | 测试用户 | 员工姓名。 |
| has\_more | Boolean | true | 是否有下一页，true表示存在更多分页。 |
| next\_cursor | Number | 10002 | 下一次请求的分页游标。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/kac/datav/inactivated/user/list?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "request":{
                "cursor":0,
                "size":10,
                "data_id":"20200501"
        }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/kac/datav/inactivated/user/list");
OapiKacDatavInactivatedUserListRequest req = new OapiKacDatavInactivatedUserListRequest();
UnactivatedUserRequest obj1 = new UnactivatedUserRequest();
obj1.setDataId("20200501");
obj1.setSize(10L);
obj1.setCursor(0L);
req.setRequest(obj1);
OapiKacDatavInactivatedUserListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode":0,
    "request_id":"6v4qtgo9a6q0",
    "result":{
        "data":[
            {
                "dept_id":1,
                "dept_name":"技术部",
                "userid":"123",
                "staff_job_num":"101",
                "staff_name":"测试用户"
            }
        ],
        "has_more":true,
        "next_cursor":10002
    }
}
```
