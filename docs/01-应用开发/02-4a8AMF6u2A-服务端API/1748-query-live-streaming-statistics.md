---
title: "获取企业视频直播统计数据"
source_url: "https://open.dingtalk.com/document/development/query-live-streaming-statistics"
namespace: "development"
slug: "query-live-streaming-statistics"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 视频直播统计 > 获取企业视频直播统计数据"
doc_id: "d2BDDoDaIZ"
updated_at: "2025-09-08 19:05:26"
---

> Source: https://open.dingtalk.com/document/development/query-live-streaming-statistics
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 视频直播统计 > 获取企业视频直播统计数据
> Updated: 2025-09-08 19:05:26

# 获取企业视频直播统计数据

调用本接口获取企业视频直播统计数据。

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
| 企业内部应用 | 是 | 查询钉钉直播统计数据的权限 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/kac/datav/videolive/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | be3Fxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| param\_video\_live\_summary\_request | VideoLiveSummaryRequest | 是 |  | 请求参数对象。 |
| data\_id | String | 是 | 20200302 | 日期标识。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 6v4qsb45fzhw | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | VideoLiveSummaryResponse |  | 统计数据对象。 |
| live\_launch\_succ5min\_cnt | Number | 1 | 成功发起5分钟直播次数。 |
| live\_launch\_succ\_cnt | Number | 2 | 成功发起直播次数。 |
| live\_play\_cnt | Number | 3 | 观看直播次数。 |
| live\_play\_user\_cnt | Number | 4 | 观看直播人数。 |
| live\_succ\_time\_len | String | 5.5 | 成功发起直播时长。 |
| max\_user\_cnt | Number | 100 | 观看人数最多直播的观看人数。 |
| watch\_group\_live\_user\_cnt | Number | 7 | 最近一天看直播的人数（包含观看和回放）。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/kac/datav/videolive/get?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "param_video_live_summary_request":{
                "data_id":"20201202"
        }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/kac/datav/videolive/get");
OapiKacDatavVideoliveGetRequest req = new OapiKacDatavVideoliveGetRequest();
VideoLiveSummaryRequest obj1 = new VideoLiveSummaryRequest();
obj1.setDataId("20201202");
req.setParamVideoLiveSummaryRequest(obj1);
OapiKacDatavVideoliveGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "result": {
        "live_launch_succ5min_cnt": 0,
        "live_launch_succ_cnt": 1,
        "live_play_cnt": 1,
        "live_play_user_cnt": 1,
        "live_succ_time_len": "1.0",
        "max_user_cnt": 1,
        "watch_group_live_user_cnt": 1
    },
    "request_id": "6v4qsb45fzhw"
}
```
