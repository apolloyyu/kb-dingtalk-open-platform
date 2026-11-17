---
title: "群扩展事件"
source_url: "https://open.dingtalk.com/document/development/croud-expansion-event"
namespace: "development"
slug: "croud-expansion-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 群扩展事件"
doc_id: "Y73ft007RG"
updated_at: "2025-10-16 15:06:43"
---

> Source: https://open.dingtalk.com/document/development/croud-expansion-event
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 群扩展事件
> Updated: 2025-10-16 15:06:43

# 群扩展事件

本文介绍了群扩展事件回调的RDS和SyncHTTP推送的数据格式。

## 数据表

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 158 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=158的数据格式解释。 | 158 | 群内安装群扩展事件。 |
| 159 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=159的数据格式解释。 | 159 | 群内卸载群扩展事件。 |

## biz\_type=158

当biz\_type=158时，数据为群内安装群扩展相关数据。

该数据为群内安装群扩展的数据推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值158，表示群内安装群扩展的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "syncAction": "im_cool_app_install",
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
| OpenConversationCorpId | String | 群会话企业corpId。 |
| OperateTime | String | 操作时间。 |
| OpenConversationId | String | 群加密会话ID。 |
| CoolAppCode | String | 群扩展code。 |
| RobotCode | String | 机器人code。 |

## biz\_type=159

当biz\_type=159时，数据为群内卸载群扩展相关数据。

该数据为群内卸载群扩展的数据推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值159，表示群内卸载群扩展的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "syncAction": "im_cool_app_uninstall",
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
| OpenConversationCorpId | String | 群会话企业corpId。 |
| OperateTime | String | 操作时间。 |
| OpenConversationId | String | 群加密会话ID。 |
| CoolAppCode | String | 群扩展code。 |
| RobotCode | String | 机器人code。 |
