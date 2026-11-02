---
title: "单聊酷应用事件"
source_url: "https://open.dingtalk.com/document/development/one-on-one-chat-cool-application-extension-event"
namespace: "development"
slug: "one-on-one-chat-cool-application-extension-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 单聊酷应用事件"
doc_id: "8sPdWLdyEY"
updated_at: "2025-10-16 15:06:43"
---

> Source: https://open.dingtalk.com/document/development/one-on-one-chat-cool-application-extension-event
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 单聊酷应用事件
> Updated: 2025-10-16 15:06:43

# 单聊酷应用事件

本文介绍了单聊酷应用事件回调的RDS和SyncHTTP推送的数据格式。

## 数据表

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 201 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=201的数据格式解释。 | 201 | 单聊安装酷应用事件。 |
| 202 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=202的数据格式解释。 | 202 | 单聊卸载酷应用事件。 |

## biz\_type=201

当biz\_type=201时，数据为单聊安装酷应用相关数据。

该数据为单聊安装酷应用的数据推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值201，表示单聊安装酷应用的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "syncAction": "single_conversation_cool_app_install",
  "OpenConversationCorpId": "ding9bd1bfb59xxxxxxxxxxxxxxxxxxx",
  "OperateTime": "1641866135051",
  "OpenConversationId": "cidT461wC7yvGJxxxxxxxxxxxxxx",
  "CoolAppCode": "COOLAPP-1-1018xxxxxxxxxxxxxxxx",
  "RobotCode": "rBLBXuiaA2rn3xxxxxxxxxxxxxx"
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 事件类型。 |
| OpenConversationCorpId | String | 会话企业corpId。 |
| OperateTime | String | 操作时间。 |
| OpenConversationId | String | 加密会话ID。 |
| CoolAppCode | String | 酷应用code。 |
| RobotCode | String | 机器人code。 |

## biz\_type=202

当biz\_type=202时，数据为单聊卸载酷应用相关数据。

该数据为单聊卸载酷应用的数据推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值202，表示单聊卸载酷应用的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "syncAction": "single_conversation_cool_app_uninstall",
  "OpenConversationCorpId": "ding9bd1bfb59xxxxxxxxxxxxxxxxxxx",
  "OperateTime": "1641866135051",
  "OpenConversationId": "cidT461wC7yvGJxxxxxxxxxxxxxx",
  "CoolAppCode": "COOLAPP-1-1018xxxxxxxxxxxxxxxx",
  "RobotCode": "rBLBXuiaA2rn3xxxxxxxxxxxxxx"
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 事件类型。 |
| OpenConversationCorpId | String | 会话企业corpId。 |
| OperateTime | String | 操作时间。 |
| OpenConversationId | String | 加密会话ID。 |
| CoolAppCode | String | 酷应用code。 |
| RobotCode | String | 机器人code。 |
