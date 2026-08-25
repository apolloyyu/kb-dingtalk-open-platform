---
title: "获取企业DING使用数据（部门维度）"
source_url: "https://open.dingtalk.com/document/development/query-the-departmental-transmission-status-of-key-clients"
namespace: "development"
slug: "query-the-departmental-transmission-status-of-key-clients"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据统计 > 获取企业DING使用数据（部门维度）"
doc_id: "k6UyFWHG0i"
updated_at: "2025-09-08 19:05:39"
---

> Source: https://open.dingtalk.com/document/development/query-the-departmental-transmission-status-of-key-clients
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据统计 > 获取企业DING使用数据（部门维度）
> Updated: 2025-09-08 19:05:39

# 获取企业DING使用数据（部门维度）

调用本接口查询企业各部门各类DING的使用情况。

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

**请求地址**：`https://oapi.dingtalk.com/topapi/kac/datav/dept/ding/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | DingUsageSummaryRequest | 是 |  | 请求对象。 |
| data\_id | String | 是 | 20200829 | 日期标识。 |
| cursor | Number | 是 | 100 | 分页游标。首页请使用0，之后直接使用返回结果中next\_cursor的值。 |
| size | Number | 是 | 0 | 分页大小，不超过100。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Object |  | 返回结果。 |
| has\_more | Boolean | false | 否有下一页，true表示存在更多分页。 |
| next\_cursor | Number | 0 | 下一次请求的分页游标。 |
| data | Object[] |  | 返回数据列表。 |
| ding\_voip\_cnt | Number | 1 | 最近一天发送语音DING数量。 |
| ding\_call\_cnt | Number | 2 | 最近一天发送电话DING数量。 |
| ding\_sms\_cnt | Number | 3 | 最近一天发送短信DING数量。 |
| ding\_app\_cnt | Number | 4 | 最近一天发送应用DING数量。 |
| ding\_cnt | Number | 10 | 最近一天发送DING的数量。 |
| dept\_name | String | 部门 | 部门名称。 |
| dept\_id | Number | 123 | 部门ID。 |
| ding\_voip\_user\_cnt | Number | 3 | 最近一天发送语音DING人数。 |
| ding\_call\_user\_cnt | Number | 2 | 最近一天发送电话DING人数。 |
| ding\_sms\_user\_cnt | Number | 5 | 最近一天发送短信DING人数。 |
| ding\_app\_user\_cnt | Number | 4 | 最近一天发送应用DING人数。 |
| ding\_user\_cnt | Number | 8 | 最近一天发送DING的人数。 |
| send\_ding\_total\_cnt | String | 100 | 历史累计发钉数。 |
| errcode | Number | 400002 | 返回码。 |
| errmsg | String | 参数错误 | 返回码描述。 |
| request\_id | String | xsrzau3z0ymt | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/kac/datav/dept/ding/list?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "request":{
                "cursor":"100",
                "size":"0",
                "data_id":"20200829"
        }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/kac/datav/dept/ding/list");
OapiKacDatavDeptDingListRequest req = new OapiKacDatavDeptDingListRequest();
DingUsageSummaryRequest obj1 = new DingUsageSummaryRequest();
obj1.setDataId("20200829");
obj1.setCursor(0L);
obj1.setSize(100L);
req.setRequest(obj1);
OapiKacDatavDeptDingListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "result": {
        "data": [
            {
                "ding_app_cnt": "4",
                "ding_sms_cnt": "3",
                "dept_name": "部门",
                "ding_app_user_cnt": "4",
                "ding_voip_cnt": "1",
                "ding_call_user_cnt": "2",
                "ding_user_cnt": "8",
                "ding_call_cnt": "2",
                "send_ding_total_cnt": "100",
                "ding_cnt": "10",
                "ding_sms_user_cnt": "5",
                "dept_id": "123",
                "ding_voip_user_cnt": "3"
            }
        ],
        "has_more": false,
        "next_cursor": 0
    },
    "errcode": 0,
    "errmsg": "ok",
    "request_id": "xsrzau3z0ymt"
}
```
