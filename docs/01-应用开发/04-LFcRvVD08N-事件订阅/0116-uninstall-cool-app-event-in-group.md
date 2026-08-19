---
title: "群内卸载酷应用事件"
source_url: "https://open.dingtalk.com/document/development/uninstall-cool-app-event-in-group"
namespace: "development"
slug: "uninstall-cool-app-event-in-group"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "即时通讯 > 酷应用 > 群内卸载酷应用事件"
doc_id: "VAiNgLlr5r"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/uninstall-cool-app-event-in-group
> Path: 应用开发 / 事件订阅 / 即时通讯 > 酷应用 > 群内卸载酷应用事件
> Updated: 2022-01-19 19:29:22

# 群内卸载酷应用事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 群内卸载酷应用事件 |
| 英文名称 | im\_cool\_app\_uninstall |

## 功能描述

群内卸载群酷应用事件推送数据说明。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "im_cool_app_uninstall",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "coolAppCode": "COOLAPP-1-1018xxxxxxxxxxxxxxxx",
    "operateTime": "1641866135051",
    "openConversationCorpId": "ding9bd1bfb59xxxxxxxxxxxxxxxxxxx",
    "robotCode": "rBLBXuiaA2rn3xxxxxxxxxxxxxx",
    "openConversationId": "cidT461wC7yvGJxxxxxxxxxxxxxx",
    "operator": "0213454xxxx1745"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "im_cool_app_uninstall",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "coolAppCode": "COOLAPP-1-1018xxxxxxxxxxxxxxxx",
  "operateTime": "1641866135051",
  "openConversationCorpId": "ding9bd1bfb59xxxxxxxxxxxxxxxxxxx",
  "robotCode": "rBLBXuiaA2rn3xxxxxxxxxxxxxx",
  "openConversationId": "cidT461wC7yvGJxxxxxxxxxxxxxx",
  "operator": "0213454xxxx1745"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=159)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 159,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "im_cool_app_uninstall",
    "coolAppCode": "COOLAPP-1-1018xxxxxxxxxxxxxxxx",
    "operateTime": "1641866135051",
    "openConversationCorpId": "ding9bd1bfb59xxxxxxxxxxxxxxxxxxx",
    "robotCode": "rBLBXuiaA2rn3xxxxxxxxxxxxxx",
    "openConversationId": "cidT461wC7yvGJxxxxxxxxxxxxxx",
    "operator": "0213454xxxx1745"
  }
}
```
