---
title: "获取企业某天的视频会议统计数据"
source_url: "https://open.dingtalk.com/document/development/video-conferencing-statistics-query-v2-for-key-accounts"
namespace: "development"
slug: "video-conferencing-statistics-query-v2-for-key-accounts"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 视频会议统计 > 获取企业某天的视频会议统计数据"
doc_id: "HaqMsJShnr"
updated_at: "2025-09-08 19:05:27"
---

> Source: https://open.dingtalk.com/document/development/video-conferencing-statistics-query-v2-for-key-accounts
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 视频会议统计 > 获取企业某天的视频会议统计数据
> Updated: 2025-09-08 19:05:27

# 获取企业某天的视频会议统计数据

调用本接口获取企业在某一天的视频会议统计数据。

> **[!IMPORTANT]**
>
> 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的[数据资产类OpenAPI](https://open.dingtalk.com/document/dataservice/data-asset-interface-adjustment-description)接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)获取相应的数据服务。
> 2. 本文档已于 2023 年 9 月 1 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力，说明如下：
>
>    - 如果未使用本接口，推荐使用[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。
>    - 如果已使用本接口，建议您根据自身实际情况评估是否切换至[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。

例如：企业有多个子部门，调用该接口，可以获取在某天企业所有视频会议的统计数据，包括总时长，总参与人次、视频会议发起次数等。

![iShot2021-12-20 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3026600461/p371914.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 钉钉数据产品权限包 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/kac/v2/datav/videoconf/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | be3Fxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | McsSummaryRequest | 是 |  | 请求对象。 |
| data\_id | String | 是 | 20200709 | 日期标识。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | McsSummaryResponse |  | 返回结果对象。 |
| join\_video\_conf\_len | Number | 1000 | 视频会议企业的累积消耗时长，单位毫秒。  即参会者入会总时长，且算到发起企业上。 |
| join\_video\_conf\_secc\_usr\_cnt | Number | 2 | 视频会议成功参与人次。 |
| join\_video\_conf\_secc\_usr\_num | Number | 3 | 视频会议成功参与用户数。 |
| join\_video\_conf\_usr\_cnt | Number | 4 | 参与视频会议用户数。 |
| start\_video\_conf\_cnt | Number | 5 | 视频会议发起次数。 |
| start\_video\_conf\_secc\_cnt | Number | 6 | 成功发起视频会议数。 |
| start\_video\_conf\_usr\_num | Number | 7 | 视频会议发起用户数。 |
| video\_conf\_ave\_usr\_num | Number | 8 | 视频会议平均每通参与人次。 |
| join\_video\_conf\_len\_min | String | 10.23 | 视频会议企业的累积消耗时长，单位分钟。 |
| start\_video\_conf\_len\_min | String | 10.32 | 成功发起视频会议时长，单位分钟。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/kac/v2/datav/videoconf/get?access_token=ACCESS_TOKEN
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
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/kac/v2/datav/videoconf/get");
OapiKacV2DatavVideoconfGetRequest req = new OapiKacV2DatavVideoconfGetRequest();
McsSummaryRequest obj1 = new McsSummaryRequest();
obj1.setDataId("20201202");
req.setRequest(obj1);
OapiKacV2DatavVideoconfGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "result": {
        "join_video_conf_len": 0,
        "join_video_conf_len_min": "0.0",
        "join_video_conf_secc_usr_cnt": 0,
        "join_video_conf_secc_usr_num": 0,
        "join_video_conf_usr_cnt": 0,
        "start_video_conf_cnt": 0,
        "start_video_conf_len_min": "0.0",
        "start_video_conf_secc_cnt": 0,
        "start_video_conf_usr_num": 0,
        "video_conf_ave_usr_num": 0
    },
    "request_id": "wckmrmgqwgth"
}
```
