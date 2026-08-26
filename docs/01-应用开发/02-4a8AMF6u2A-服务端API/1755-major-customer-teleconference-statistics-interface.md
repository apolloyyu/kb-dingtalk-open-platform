---
title: "获取企业某天的电话会议数据"
source_url: "https://open.dingtalk.com/document/development/major-customer-teleconference-statistics-interface"
namespace: "development"
slug: "major-customer-teleconference-statistics-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 电话会议统计 > 获取企业某天的电话会议数据"
doc_id: "qXN5mqiz5y"
updated_at: "2025-09-08 19:05:32"
---

> Source: https://open.dingtalk.com/document/development/major-customer-teleconference-statistics-interface
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 电话会议统计 > 获取企业某天的电话会议数据
> Updated: 2025-09-08 19:05:32

# 获取企业某天的电话会议数据

调用本接口获取企业某天的电话会议数据。

> **[!IMPORTANT]**
>
> 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的[数据资产类OpenAPI](https://open.dingtalk.com/document/dataservice/data-asset-interface-adjustment-description)接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)获取相应的数据服务。
> 2. 本文档已于 2023 年 9 月 1 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力，说明如下：
>
>    - 如果未使用本接口，推荐使用[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。
>    - 如果已使用本接口，建议您根据自身实际情况评估是否切换至[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。

例如，企业有多个子部门，调用本接口可以获取在某天企业所有电话会议的统计数据，包括呼叫参与人次、呼叫成功次数、呼叫成功时长和呼叫成功时长。![iShot2021-12-21 13](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4845700461/p372093.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 钉钉数据产品权限包 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/kac/datav/telconf/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | TelConferenceSummaryRequest | 是 |  | 请求对象。 |
| data\_id | String | 是 | 20201202 | 日期标识。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | xsrzau3z0ymt | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | TelConferenceSummaryResponse |  | 返回结果。 |
| call\_count | Number | 1 | 呼叫成功次数。 |
| call\_duration | String | 2 | 呼叫成功时长，单位秒。 |
| call\_join\_pv | Number | 3 | 呼叫参与人数。 |
| call\_duration\_min | String | 10.12 | 呼叫成功时长，单位分钟。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/kac/datav/telconf/get?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "request":{
                "data_id":"20201202"
        }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/kac/datav/telconf/get");
OapiKacDatavTelconfGetRequest req = new OapiKacDatavTelconfGetRequest();
TelConferenceSummaryRequest obj1 = new TelConferenceSummaryRequest();
obj1.setDataId("20201202");
req.setRequest(obj1);
OapiKacDatavTelconfGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "result": {
        "call_count": 0,
        "call_duration": "0.0",
        "call_duration_min": "0.0",
        "call_join_pv": 0
    },
    "request_id": "zfzyv8uzxasc"
}
```
