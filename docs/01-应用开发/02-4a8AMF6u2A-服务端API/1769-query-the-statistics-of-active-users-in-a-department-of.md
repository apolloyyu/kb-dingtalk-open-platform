---
title: "企业活跃用户统计列表（部门维度）"
source_url: "https://open.dingtalk.com/document/development/query-the-statistics-of-active-users-in-a-department-of"
namespace: "development"
slug: "query-the-statistics-of-active-users-in-a-department-of"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据统计 > 企业活跃用户统计列表（部门维度）"
doc_id: "BwdzMrvZOz"
updated_at: "2025-09-08 19:05:37"
---

> Source: https://open.dingtalk.com/document/development/query-the-statistics-of-active-users-in-a-department-of
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据统计 > 企业活跃用户统计列表（部门维度）
> Updated: 2025-09-08 19:05:37

# 企业活跃用户统计列表（部门维度）

调用本接口查询部门维度的活跃用户统计数据列表。

> **[!IMPORTANT]**
>
> 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的[数据资产类OpenAPI](https://open.dingtalk.com/document/dataservice/data-asset-interface-adjustment-description)接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)获取相应的数据服务。
> 2. 本文档已于 2023 年 9 月 1 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力，说明如下：
>
>    - 如果未使用本接口，推荐使用[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。
>    - 如果已使用本接口，建议您根据自身实际情况评估是否切换至[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 钉钉数据产品权限包 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/kac/datav/dept/dau/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | Object | 是 |  | 请求对象。 |
| data\_id | String | 是 | 20200501 | 日期标识。  例如：20220101。 |
| size | Number | 是 | 10 | 每页最大条目数，最大值100。 |
| cursor | Number | 是 | 0 | 分页游标。   - 如果是首次调用，该参数传0。 - 如果是非首次调用，该参数传上传调用返回的next\_cursor。 |
| deptId | String | 否 | 123 | 统计部门ID。 |
| superDeptId | String | 否 | 123 | 统计部门的父部门ID。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回信息。 |
| result | Object | result | 返回结果。 |
| data | Object[] | data | 返回的数据列表。 |
| daily\_active\_users | Number | 123 | 日活跃人数。 |
| dept\_id | Number | 12 | 部门ID。 |
| dept\_name | String | 技术部 | 部门名称。 |
| contacts\_number | Number | 12 | 通讯录人数。 |
| pc\_active\_users | Number | 14 | 钉钉pc端登录人数。 |
| app\_active\_users | Number | 10 | 钉钉app端登录人数。 |
| has\_more | Boolean | true | 是否有下一页。   - true：有 - false：每页 |
| next\_cursor | Number | 100 | 下一次请求的分页游标。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/kac/datav/dept/dau/list?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "request":{
                "cursor":"0",
                "superDeptId":"123",
                "size":"10",
                "data_id":"20200501",
                "deptId":"123"
        }
}
```

**请求示例（JAVA SDK）**

```
public class Main {
    public static void main(String[] args) {
        try {
            DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/kac/datav/dept/dau/list");
            OapiKacDatavDeptDauListRequest req = new OapiKacDatavDeptDauListRequest();
            DeptDauSummaryRequest obj1 = new DeptDauSummaryRequest();
            obj1.setDataId("20200501");
            obj1.setSize(10L);
            obj1.setCursor(0L);
            obj1.set
            req.setRequest(obj1);
            OapiKacDatavDeptDauListResponse rsp = client.execute(req, "");
            System.out.println(rsp.getBody());
        } catch (ApiException e) {
            e.printStackTrace();
        }
    }
}
```

**返回示例**

```
{
        "errcode":"0",
        "result":{
                "next_cursor":"100",
                "data":{
                        "contacts_number":"12",
                        "pc_active_users":"14",
                        "dept_name":"技术部",
                        "app_active_users":"10",
                        "daily_active_users":"123",
                        "dept_id":"12"
                },
                "has_more":"true"
        },
        "errmsg":"成功"
}
```
