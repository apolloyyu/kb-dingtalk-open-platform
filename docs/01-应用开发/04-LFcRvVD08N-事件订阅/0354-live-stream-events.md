---
title: "直播事件"
source_url: "https://open.dingtalk.com/document/development/live-stream-events"
namespace: "development"
slug: "live-stream-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 直播事件"
doc_id: "n0yNflApWY"
updated_at: "2025-10-16 15:06:33"
---

> Source: https://open.dingtalk.com/document/development/live-stream-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 直播事件
> Updated: 2025-10-16 15:06:33

# 直播事件

本文介绍了直播事件回调的RDS和SyncHTTP推送的数据格式。

## 准备工作

- 钉钉会向第三方企业应用推送订阅的回调事件，详情参见[第三方企业应用事件与回调流程](https://open.dingtalk.com/document/isvapp/third-party-enterprise-application-address-book-change-event-subscription-process)。

## 数据表

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 220 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=220的数据格式解释。 | 220 | 直播状态变化事件。 |
| 221 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=221的数据格式解释。 | 221 | 直播修改信息事件。 |
| 223 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=223的数据格式解释。 | 223 | 直播观看回放信息事件。 |
| 229 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=229的数据格式解释。 | 229 | 直播结束数据处理任务完成事件。 |

## biz\_type=220

当biz\_type=220时，数据为直播状态变化相关数据。

该数据为直播状态变化的数据推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值220，表示直播状态变化的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "syncAction": "live_status_change_event",
  "liveId":"1fc2eaca-****-****-****-b23e1bda4225",
  "liveStatus":3
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 事件类型。 |
| liveId | String | 直播id。 |
| liveStatus | Integer | 直播状态：   - 0：预告态 - 1：直播中 - 2：暂停态 - 3：结束态 - 4：处罚态 - 6：预告过期失效态 |

## biz\_type=221

当biz\_type=221时，数据为直播修改信息相关数据。

该数据为直播修改信息的数据推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值221，表示直播修改信息的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "syncAction": "live_update_event",
  "title":"测试直播",
  "introduction":"测试直播简介",
  "coverUrl":"http://xxx.png",
  "preStartTime":1660266147700,
  "preEndTime":1660268147000,
  "liveId":"1fc2eaca-****-****-****-b23e1bda4225"
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 事件类型。 |
| title | String | 直播标题。 |
| introduction | String | 直播简介。 |
| coverUrl | String | 直播封面。 |
| preStartTime | Long | 直播预计开播时间戳。 |
| preEndTime | Long | 直播预计结束时间戳。 |
| liveId | String | 直播id。 |

## biz\_type=223

当biz\_type=223时，数据为直播观看回放信息相关数据。

该数据为直播观看回放信息的数据推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值223，表示直播观看回放信息的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "syncAction": "live_watch_playback_event",
  "unionId":"C8GuTH**********0v3QAiEiE",
  "watchDuration":17527,
  "name":"起*",
  "liveId":"1fc2eaca-****-****-****-b23e1bda4225"
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 事件类型。 |
| unionId | String | 用户unionId。 |
| watchDuration | Long | 回放观看时长。 |
| name | String | 用户昵称。 |
| liveId | String | 直播id。 |

## biz\_type=229

当biz\_type=229时，数据为直播结束数据处理任务完成的相关数据。

该数据为直播结束数据处理任务完成的数据推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值223，表示直播结束数据处理任务完成的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "syncAction": "live_statistic_done_event",
  "liveId":"1fc2eaca-****-****-****-b23e1bda4225",
  "finishTime": 166011401308
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 事件类型。 |
| liveId | String | 直播id。 |
| finishTime | Long | 数据处理完成时间。 |
