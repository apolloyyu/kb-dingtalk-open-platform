---
title: "获取企业DING使用数据"
source_url: "https://open.dingtalk.com/document/development/enterprise-ding-quantity-statistics"
namespace: "development"
slug: "enterprise-ding-quantity-statistics"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据统计 > 获取企业DING使用数据"
doc_id: "oXSPYIKttb"
updated_at: "2025-09-08 19:05:38"
---

> Source: https://open.dingtalk.com/document/development/enterprise-ding-quantity-statistics
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据统计 > 获取企业DING使用数据
> Updated: 2025-09-08 19:05:38

# 获取企业DING使用数据

调用本接口查询企业各类DING的使用情况。

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

**请求地址**：`https://oapi.dingtalk.com/topapi/kac/datav/ding/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| ding\_usage\_summary\_request | DingUsageSummaryRequest | 是 |  | 请求对象。 |
| data\_id | String | 是 | 20200729 | 日期标识。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | DingUsageSummaryResponse |  | 返回结果。 |
| ding\_voip\_cnt | Number | 1 | 最近一天发送语音DING数。 |
| ding\_call\_cnt | Number | 2 | 最近一天发送电话DING数。 |
| ding\_sms\_cnt | Number | 3 | 最近一天发送短信DING数。 |
| ding\_app\_cnt | Number | 4 | 最近一天发送应用DING数。 |
| ding\_cnt | Number | 10 | 最近1天发送DING数。 |
| ding\_voip\_user\_cnt | Number | 3 | 最近一天发送语音DING人数。 |
| ding\_call\_user\_cnt | Number | 5 | 最近一天发送电话DING人数。 |
| ding\_sms\_user\_cnt | Number | 2 | 最近一天发送短信DING人数。 |
| ding\_app\_user\_cnt | Number | 1 | 最近一天发送应用DING人数。 |
| ding\_user\_cnt | Number | 10 | 最近1天发送DING人数 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | er9sv4zsvs0b | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/kac/datav/ding/get?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "ding_usage_summary_request":{
                "data_id":"20200729"
        }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/kac/datav/ding/get");
OapiKacDatavDingGetRequest req = new OapiKacDatavDingGetRequest();
DingUsageSummaryRequest obj1 = new DingUsageSummaryRequest();
obj1.setDataId("20200729");
req.setDingUsageSummaryRequest(obj1);
OapiKacDatavDingGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "result": {
        "ding_app_cnt": 29,
        "ding_app_user_cnt": 13,
        "ding_call_cnt": 2,
        "ding_call_user_cnt": 2,
        "ding_cnt": 34,
        "ding_sms_cnt": 3,
        "ding_sms_user_cnt": 3,
        "ding_user_cnt": 16,
        "ding_voip_cnt": 0,
        "ding_voip_user_cnt": 0
    },
    "request_id": "er9sv4zsvs0b"
}
```
