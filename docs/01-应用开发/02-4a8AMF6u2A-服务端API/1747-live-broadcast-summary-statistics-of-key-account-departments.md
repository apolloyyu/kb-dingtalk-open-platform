---
title: "获取企业视频直播统计列表（部门维度）"
source_url: "https://open.dingtalk.com/document/development/live-broadcast-summary-statistics-of-key-account-departments"
namespace: "development"
slug: "live-broadcast-summary-statistics-of-key-account-departments"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 视频直播统计 > 获取企业视频直播统计列表（部门维度）"
doc_id: "cGBQ9Qwvtd"
updated_at: "2025-09-08 19:05:25"
---

> Source: https://open.dingtalk.com/document/development/live-broadcast-summary-statistics-of-key-account-departments
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 视频直播统计 > 获取企业视频直播统计列表（部门维度）
> Updated: 2025-09-08 19:05:25

# 获取企业视频直播统计列表（部门维度）

调用本接口按部门直播视频统计列表数据。

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

**请求地址**：`https://oapi.dingtalk.com/topapi/kac/datav/dept/videolive/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | VideoLiveDeptSummaryRequest | 是 |  | 请求对象。 |
| data\_id | String | 是 | 20200501 | 日期标识。 |
| size | Number | 是 | 10 | 分页大小，不超过100。 |
| cursor | Number | 是 | 0 | 分页游标，首页请使用0，之后直接使用返回结果中next\_cursor的值。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 4f9md9obopn2 | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | VideoLiveDeptSummaryResponse |  | 返回结果。 |
| data | VideoLiveDeptSummaryVo[] |  | 返回数据列表。 |
| dept\_id | Number | 12 | 部门id。 |
| dept\_name | String | 技术部 | 部门名称。 |
| live\_launch\_count | Number | 100 | 直播发起次数。 |
| live\_time\_length | String | 10.2 | 直播时长，单位分钟。 |
| live\_play\_user\_count | Number | 19 | 观看直播人数。 |
| has\_more | Boolean | false | 是否有更多数据。 |
| next\_cursor | Number | 0 | 下一次请求的分页游标。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/kac/datav/dept/videolive/list?access_token=ACCESS_TOKEN
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
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/kac/datav/dept/videolive/list");
OapiKacDatavDeptVideoliveListRequest req = new OapiKacDatavDeptVideoliveListRequest();
VideoLiveDeptSummaryRequest obj1 = new VideoLiveDeptSummaryRequest();
obj1.setDataId("20200501");
obj1.setSize(10L);
obj1.setCursor(0L);
req.setRequest(obj1);
OapiKacDatavDeptVideoliveListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "result": {
        "data": [
            {
                "dept_id": -1,
                "dept_name": "互动服务窗测试",
                "live_launch_count": 1,
                "live_play_user_count": 1,
                "live_time_length": "1.22"
            }
        ],
        "has_more": false,
        "next_cursor": 0
    },
    "request_id": "ef17shy4ellv"
}
```
