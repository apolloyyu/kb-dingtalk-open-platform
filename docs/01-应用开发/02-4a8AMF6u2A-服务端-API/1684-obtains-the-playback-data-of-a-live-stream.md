---
title: "获取培训观看数据"
source_url: "https://open.dingtalk.com/document/development/obtains-the-playback-data-of-a-live-stream"
namespace: "development"
slug: "obtains-the-playback-data-of-a-live-stream"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 培训 > 获取培训观看数据"
doc_id: "1ZeVfjqfdx"
updated_at: "2026-08-27 12:32:14"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-playback-data-of-a-live-stream
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 培训 > 获取培训观看数据
> Updated: 2026-08-27 12:32:14

# 获取培训观看数据

调用本接口获取培训观看数据，包含观看直播时长和观看回放时长。

> **[!IMPORTANT]**
>
> - 查询时受限于当前用户是否在群内，并且是否真正看过直播。
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[查询直播的观看数据](1494-queries-the-playback-data-of-a-live-stream.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/planetom/feeds/watchdata/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用服务端API的应用凭证，可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| chat\_id | String | 是 | cidzZ7txxxx | 直播绑定的群列表ID。   - 小程序通过[选择会话](../03-Ogu5SlPY4t-客户端-JSAPI/0707-select-session.md)方法获取。 - 微应用通过[根据corpid选择会话](../03-Ogu5SlPY4t-客户端-JSAPI/0767-select-session-based-on-corpid.md)方法获取。 |
| feed\_id | String | 是 | c16a6277-a538-466xxxx | 课程ID，调用[创建培训课程](1681-create-live-courses.md)接口返回的课程ID。 |
| page\_size | Number | 否 | 10 | 分页大小。  **默认值**：0 |
| index | Number | 否 | 0 | 分页起始位置，不传默认获取前10个。 |
| anchor\_id | String | 是 | 0225376 | 主播在组织内的userid。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenFeedWatchDetailRspModel |  | 返回结果。 |
| viewer\_watch\_details | OpenFeedWatchDetailModel[] |  | 观看数据列表。 |
| play\_record\_duration | Number | 30 | 观看回放时长，单位秒。 |
| play\_live\_duration | Number | 20 | 观看直播时长，单位秒。 |
| userid | String | 0225376 | 观看者在组织内的userid。 |
| has\_finish | Number | 0 | 是否还有数据没返回：   - **0**：还有 - **1**：没有 |
| success | Boolean | true | 请求是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/planetom/feeds/watchdata/get?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "anchor_id": "0225376",
  "index": 0,
  "chat_id": "cidzZ7txxxx",
  "feed_id": "c16a6277-a538-466xxxx",
  "page_size": 10
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/planetom/feeds/watchdata/get");
OapiPlanetomFeedsWatchdataGetRequest req = new OapiPlanetomFeedsWatchdataGetRequest();
req.setChatId("cidzZ7txxxx");
req.setFeedId("c16a6277-a538-466xxxx");
req.setPageSize(10L);
req.setIndex(0L);
req.setAnchorId("0225376");
OapiPlanetomFeedsWatchdataGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "result": {
    "viewer_watch_details": [
      {
        "play_record_duration": 30,
        "play_live_duration": 20,
        "userid": "0225376"
      }
    ],
    "has_finish": 0
  },
  "success": true,
  "errcode": 0,
  "errmsg": ""
}
```
