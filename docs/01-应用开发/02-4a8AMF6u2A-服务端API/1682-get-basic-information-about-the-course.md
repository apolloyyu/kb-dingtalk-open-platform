---
title: "获取培训课程的基本信息"
source_url: "https://open.dingtalk.com/document/development/get-basic-information-about-the-course"
namespace: "development"
slug: "get-basic-information-about-the-course"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 培训 > 获取培训课程的基本信息"
doc_id: "fr5hjj4Ssw"
updated_at: "2025-10-17 16:57:15"
---

> Source: https://open.dingtalk.com/document/development/get-basic-information-about-the-course
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 培训 > 获取培训课程的基本信息
> Updated: 2025-10-17 16:57:15

# 获取培训课程的基本信息

调用本接口获取培训课程的基本信息。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对培训课程相关接口规范进行升级，本文接口文档已于2022年9月23日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用[查询直播信息](https://open.dingtalk.com/document/isvapp/queries-the-live-streaming-information)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

![iShot2021-12-28 18](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9700570461/p377716.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | — | — |
| 第三方企业应用 | 是 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/planetom/feeds/statistic/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用服务端API的应用凭证，可通过[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| feed\_id | String | 是 | c6277-a538-466xxxx | 课程ID，调用[创建培训课程](https://open.dingtalk.com/document/isvapp/create-live-courses)接口返回的课程ID。 |
| anchor\_id | String | 是 | 0225376 | 主播在对应组织的userid。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenFeedInfoModel |  | 返回结果。 |
| status | Number | 1 | 课程状态：   - **1**：有效 - **15**：无效 |
| introduction | String | 简介 | 课程简介。 |
| title | String | 测试课程 | 课程标题。 |
| cover\_url | String | http://tblearxxxx | 封面链接。 |
| feed\_id | String | c6277-a538-466xxxx | 课程ID。 |
| feed\_type | Number | 0 | 课程类型：   - **0**：直播 |
| start\_time | Date | 2020-12-09 09:23:00 | 开始时间。  **[!NOTE]**  当直播未开始，该参数为预计开播时间，开播后为实际的开始时间。如果在预计开播时间七天内未进行直播，会被清理。 |
| anchor\_id | String | 0225376 | 主播的userid。 |
| chat\_ids | String[] | ["cidzZ7txxxx","cidaZ5xxxx"] | 绑定的群ID。 |
| sub\_status | Number | 3 | 直播状态：   - **0**：已预告 - **1**：直播中 - **2**：暂停 - **3**：结束 - **4**：已发布 - **5**：已删除 |
| jump\_url | String | http://dingtalk.xxxx | 跳转链接。 |
| end\_time | Date | 2020-12-09 10:23:00 | 直播结束时间。 |
| has\_play\_back | Boolean | false | 是否有回放保存。 |
| replay\_url | String |  | 回放拉流地址。 |
| edit\_replay\_url | String |  | 剪辑过后的视频回放地址（含authkey,若空则代表没有经过剪辑）。 |
| duration | Number | 3600000 | 直播时长，单位毫秒。 |
| success | Boolean | true | 调用是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/planetom/feeds/statistic/get?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "anchor_id": "0225376",
    "feed_id": "c6277-a538-466xxxx"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/planetom/feeds/statistic/get");
OapiPlanetomFeedsStatisticGetRequest req = new OapiPlanetomFeedsStatisticGetRequest();
req.setFeedId("c6277-a538-466xxxx");
req.setAnchorId("0225376");
OapiPlanetomFeedsStatisticGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "result": {
        "status": 1,
        "introduction": "简介",
        "title": "测试课程",
        "cover_url": "http://tblearxxxx",
        "feed_id": "c6277-a538-466xxxx",
        "feed_type": 1,
        "start_time": "2020-12-09 09:23:00",
        "anchor_id": "0225376",
        "chat_ids": [
            "cidzZ7txxxx",
            "cidaZ5xxxx"
        ],
        "sub_status": 3,
        "jump_url": "http://dingtalk.xxxx",
        "end_time": "2020-12-09 10:23:00",
        "has_play_back": false,
        "duration": 3600000,
        "replay_url": "",
        "edit_replay_url":""
    },
    "success": true,
    "errcode": 0,
    "errmsg": "ok"
}
```
