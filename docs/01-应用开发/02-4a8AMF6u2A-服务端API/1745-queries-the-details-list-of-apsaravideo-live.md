---
title: "获取视频直播明细列表"
source_url: "https://open.dingtalk.com/document/development/queries-the-details-list-of-apsaravideo-live"
namespace: "development"
slug: "queries-the-details-list-of-apsaravideo-live"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 视频直播统计 > 获取视频直播明细列表"
doc_id: "6nri4rfm21"
updated_at: "2025-09-08 19:05:23"
---

> Source: https://open.dingtalk.com/document/development/queries-the-details-list-of-apsaravideo-live
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 视频直播统计 > 获取视频直播明细列表
> Updated: 2025-09-08 19:05:23

# 获取视频直播明细列表

调用本接口获取视频直播明细列表。

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

**请求地址**：`https://oapi.dingtalk.com/topapi/kac/datav/videolive/detail/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | jahsdgxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | VideoLiveDetailRequest | 是 |  | 请求参数对象。 |
| data\_id | String | 是 | 20200401 | 日期标识。 |
| size | Number | 是 | 10 | 分页大小，不超过100。 |
| cursor | Number | 是 | 0 | 分页游标。  首页请使用0，之后直接使用返回结果中**next\_cursor**的值**。** |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 5av7ifh2atw0 | 请求ID。 |
| errcode | Number | 0 | 状态码，0表示调用成功。 |
| errmsg | String | ok | 调用失败时返回错误信息。 |
| result | VideoLiveDetailResponse |  | 返回结果。 |
| has\_more | Boolean | false | 是否还有更多数据。 |
| next\_cursor | Number | 100 | 下一次请求的分页游标。 |
| data | VideoLiveDetailVo[] |  | 数据明细列表。 |
| openConversationId | String | 2571318 | 直播群ID。 |
| group\_name | String | 直播演示群 | 直播群名称。 |
| group\_user\_count | Number | 100 | 群人数。 |
| live\_watch\_count | Number | 10 | 观看直播次数。 |
| live\_watch\_duration | String | 1000 | 直播时长，单位秒。 |
| live\_watch\_end\_time | String | 2020-04-08 10:54:03 | 直播结束时间。 |
| live\_watch\_start\_time | String | 2020-04-08 09:54:03 | 直播开始时间。 |
| live\_watch\_title | String | 演示教学课 | 直播标题。 |
| live\_watch\_user\_count | Number | 10 | 观看直播人数。 |
| userid | String | 1234 | 用户的userid。 |
| staff\_name | String | 王小毛 | 直播发起人用户名称。 |
| uuid | String | 21232d87-2b63-4f68-9c0a-db54ddd72379 | 直播uuid。 |
| dept\_id | Number | 1233 | 部门ID。 |
| dept\_name | String | 部门名称 | 部门名称。 |
| staff\_job\_num | String | 10002 | 直播发起人员工工号。 |
| live\_watch\_duration\_min | String | 10.123 | 直播时长，单位分钟。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/kac/datav/videolive/detail/list?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "request":{
                "cursor":0,
                "size":10,
                "data_id":"20201202"
        }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/kac/datav/videolive/detail/list");
OapiKacDatavVideoliveDetailListRequest req = new OapiKacDatavVideoliveDetailListRequest();
VideoLiveDetailRequest obj1 = new VideoLiveDetailRequest();
obj1.setDataId("20201202");
obj1.setSize(10L);
obj1.setCursor(0L);
req.setRequest(obj1);
OapiKacDatavVideoliveDetailListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "result": {
        "data": [
            {
                "openConversationId": "33441299903",
                "dept_id": -1,
                "dept_name": "互动服务窗测试",
                "group_name": "数据统计测试群",
                "group_user_count": 100,
                "live_watch_count": 1,
                "live_watch_duration": "73.21",
                "live_watch_duration_min": "1.22",
                "live_watch_end_time": "2020-12-02 18:40:49",
                "live_watch_start_time": "2020-12-02 18:39:36",
                "live_watch_title": "测试",
                "live_watch_user_count": 1,
                "staff_job_num": "10002",
                "staff_name": "测试用户",
                "userid": "user123",
                "uuid": "6f2a6b79-xxxx-xxxx-xxxx-28be9ba82568"
            }
        ],
        "has_more": false,
        "next_cursor": 0
    },
    "request_id": "10ssxnxjtgzlt"
}
```
