---
title: "创建培训课程"
source_url: "https://open.dingtalk.com/document/development/create-live-courses"
namespace: "development"
slug: "create-live-courses"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 培训 > 创建培训课程"
doc_id: "8C1gTtKqr1"
updated_at: "2025-10-17 16:56:57"
---

> Source: https://open.dingtalk.com/document/development/create-live-courses
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 培训 > 创建培训课程
> Updated: 2025-10-17 16:56:57

# 创建培训课程

调用本接口通过培训平台开放能力，创建培训课程。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对培训课程相关接口规范进行升级，本文接口文档已于2022年9月23日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用[创建直播](https://open.dingtalk.com/document/isvapp/create-live-streaming)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

> **[!NOTE]**
>
> 本接口返回创建的培训课程ID，使用如下构造方式，可进入培训课程的创建页面。
>
> ```
> dingtalk://dingtalkclient/action/start_uniform_live?liveUuid=ID
> ```

![iShot2021-12-28 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9989470461/p377696.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | — | — |
| 第三方企业应用 | 是 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/planetom/feeds/create`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用服务端API的应用凭证，可通过[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| cover\_url | String | 否 | http://tblearxxxx | 封面的URL，必须是公网可访问的图片地址。 |
| appoint\_begin\_time | Number | 是 | 1546358399000 | 约定开播（未来时间），Unix时间戳，单位毫秒。 |
| pic\_introduction\_url | String | 否 | http://tblearxxxx | 图片简介URL，必须是公网可访问的图片地址。 |
| feed\_type | Number | 是 | 0 | 课程类型：   - **0**：直播 |
| group\_ids | String | 否 | cidzZ7txxxx,cidaZ5xxxx | 直播要绑定的群列表ID。   - 小程序通过[选择会话](https://open.dingtalk.com/document/isvapp/select-session)方法获取。 - 微应用通过[根据corpid选择会话](https://open.dingtalk.com/document/isvapp/select-session-based-on-corpid)方法获取。 |
| title | String | 是 | 测试课程 | 课程标题。 |
| anchor\_id | String | 是 | 0225376 | 主播在组织内的userId。 |
| introduction | String | 否 | 简介 | 培训简介。 |
| group\_id\_type | Number | 否 | 1 | group\_ids传入时的类型格式。   - **1**：chatId - **2**：openConversationId   **[!NOTE]**  不传默认为OpenConversationId |
| open\_app\_id | Number | 是 | 66555 | 开放平台中应用的appId，参考[AppId](https://open.dingtalk.com/document/isvapp/basic-concepts#section-p92-l2z-dmz)。 |
| pre\_video\_url | String | false | http:xxx.mp4 | 预告片视频，必须是公网可访问的图片地址。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | String | c16a6277-a538-466xxxx | 课程ID。 |
| success | Boolean | true | 请求是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/planetom/feeds/create?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "cover_url": "http://tblearxxxx",
    "anchor_id": "0225376",
    "pic_introduction_url": "http://tblearxxxx",
    "group_ids": "cidzZ7txxxx,cidaZ5xxxx",
    "appoint_begin_time": 1546358399000,
    "title": "测试课程",
    "feed_type": 0,
    "introduction": "简介",
    "group_id_type": 1,
    "open_app_id": 66555
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/planetom/feeds/create");
OapiPlanetomFeedsCreateRequest req = new OapiPlanetomFeedsCreateRequest();
req.setCoverUrl("http://tblearxxxx");
req.setAppointBeginTime(1546358399000L);
req.setPicIntroductionUrl("http://tblearxxxx");
req.setFeedType(0L);
req.setGroupIds("cidzZ7txxxx,cidaZ5xxxx");
req.setTitle("测试课程");
req.setAnchorId("1234567");
req.setIntroduction("简介");
req.setGroupIdType(1L);
req.setOpenAppId(66555L);
req.setPreVideoUrl("http:xxx.mp4");
OapiPlanetomFeedsCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "result":"c16a6277-a538-466xxxx",
    "success":true,
    "errcode":0,
    "errmsg":"ok"
}
```
