---
title: "获取企业聊天数据"
source_url: "https://open.dingtalk.com/document/development/chat-data-statistics-query-for-key-accounts"
namespace: "development"
slug: "chat-data-statistics-query-for-key-accounts"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据统计 > 获取企业聊天数据"
doc_id: "VcI4usskaL"
updated_at: "2025-09-08 19:05:34"
---

> Source: https://open.dingtalk.com/document/development/chat-data-statistics-query-for-key-accounts
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据统计 > 获取企业聊天数据
> Updated: 2025-09-08 19:05:34

# 获取企业聊天数据

调用本接口查询当前企业每天的聊天汇总数据，包含用户数及群数等。

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

**请求地址**：`https://oapi.dingtalk.com/topapi/kac/datav/chat/summary/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 28398831xxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | ImSummaryRequest | 是 |  | 请求对象。 |
| data\_id | String | 是 | 20200501 | 日期标识。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | edyi1m70jbi1 | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| result | Object | result | 返回结果。 |
| group\_chat\_user\_count | Number | 10 | 群聊用户数。 |
| message\_total\_count | Number | 20 | 消息数。 |
| message\_user\_count | Number | 30 | 聊天用户数。 |
| chat\_user\_count | Number | 4 | 单聊用户数。 |
| group\_count | Number | 100 | 总群数。 |
| new\_group\_count | Number | 100 | 新增群数（当日）。 |
| active\_group\_count | Number | 2 | 活跃群数（当日）。 |
| group\_message\_count | Number | 12 | 群聊消息数。 |
| single\_message\_count | Number | 30 | 单聊消息数。 |
| message\_avg\_count | String | 3.2 | 人均发送消息数。 |
| group\_send\_file\_message\_count | String | 3 | 发送群文件数（当日）。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/kac/datav/chat/summary/get?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "request":{
                "data_id":"20201201"
        }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/kac/datav/chat/summary/get");
OapiKacDatavChatSummaryGetRequest req = new OapiKacDatavChatSummaryGetRequest();
ImSummaryRequest obj1 = new ImSummaryRequest();
obj1.setDataId("20201201");
req.setRequest(obj1);
OapiKacDatavChatSummaryGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "result": {
        "active_group_count": 0,
        "chat_user_count": 35,
        "group_chat_user_count": 23,
        "group_count": 16,
        "group_message_count": 242,
        "message_avg_count": "89.18",
        "message_total_count": 4013,
        "message_user_count": 35,
        "new_group_count": 0,
        "single_message_count": 3771,
        "group_send_file_message_count": "3"
    },
    "request_id": "edyi1m70jbi1"
}
```
