---
title: "获取企业应用访问情况"
source_url: "https://open.dingtalk.com/document/development/queries-the-daily-usage-summary-of-microapplications-in-an-enterprise"
namespace: "development"
slug: "queries-the-daily-usage-summary-of-microapplications-in-an-enterprise"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据统计 > 获取企业应用访问情况"
doc_id: "Ggpt0NIdty"
updated_at: "2025-09-08 19:05:35"
---

> Source: https://open.dingtalk.com/document/development/queries-the-daily-usage-summary-of-microapplications-in-an-enterprise
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据统计 > 获取企业应用访问情况
> Updated: 2025-09-08 19:05:35

# 获取企业应用访问情况

调用本接口查询当前企业每天的微应用使用汇总数据。

> **[!IMPORTANT]**
>
> 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的[数据资产类OpenAPI](https://open.dingtalk.com/document/dataservice/data-asset-interface-adjustment-description)接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)获取相应的数据服务。
> 2. 本文档已于 2023 年 9 月 1 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力，说明如下：
>
>    - 如果未使用本接口，推荐使用[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。
>    - 如果已使用本接口，建议您根据自身实际情况评估是否切换至[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。

> **[!NOTE]**
>
> 本接口只返回有访问记录的应用信息，无访问记录的应用不返回。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 钉钉数据产品权限包 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/kac/datav/microapp/detail/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | MicroAppSummaryRequest | 是 |  | 请求对象。 |
| data\_id | String | 是 | 20200501 | 日期标识。  **[!NOTE]**  支持获取距今90天内的历史记录信息。 |
| size | Number | 是 | 10 | 分页大小，不超过100。 |
| cursor | Number | 是 | 0 | 分页游标。首页请使用0，之后直接使用返回结果中next\_cursor的值。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 3ralkmnd7yst | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | MicroAppSummaryResponse |  | 查询结果。 |
| data | MicroAppSummaryVo[] |  | 返回的数据列表。 |
| micro\_app\_name | String | 钉钉数据 | 微应用名称。 |
| micro\_app\_type | Number | 1 | 微应用类型。   - 1：第三方企业应用 - 2：官方基础应用 - 3：企业自建应用 |
| micro\_app\_user\_count | Number | 9 | 访问用户数。 |
| has\_more | Boolean | true | 是否有下一页，true表示存在更多分页。 |
| next\_cursor | Number | 100 | 下一次请求的分页游标。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/kac/datav/microapp/detail/list?access_token=ACCESS_TOKEN
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
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/kac/datav/microapp/detail/list");
OapiKacDatavMicroappDetailListRequest req = new OapiKacDatavMicroappDetailListRequest();
MicroAppSummaryRequest obj1 = new MicroAppSummaryRequest();
obj1.setDataId("20200501");
obj1.setSize(10L);
obj1.setCursor(0L);
req.setRequest(obj1);
OapiKacDatavMicroappDetailListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "result": {
        "data": [
            {
                "micro_app_name": "钉钉数据",
                "micro_app_type": 1,
                "micro_app_user_count": 9
            }
        ],
        "has_more": true,
        "next_cursor": 100
    },
    "request_id": "3ralkmnd7yst"
}
```
