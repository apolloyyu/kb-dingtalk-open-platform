---
title: "群内卸载酷应用事件"
source_url: "https://open.dingtalk.com/document/development/intra-cluster-offload-cluster-extension-event-stream"
namespace: "development"
slug: "intra-cluster-offload-cluster-extension-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 群聊酷应用事件 > 群内卸载酷应用事件"
doc_id: "4zi9K1a9Xq"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/intra-cluster-offload-cluster-extension-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 群聊酷应用事件 > 群内卸载酷应用事件
> Updated: 2022-01-19 19:29:22

# 群内卸载酷应用事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 群内卸载酷应用事件 |
| 英文名称 | im\_cool\_app\_uninstall |

## 功能描述

eventType为im\_cool\_app\_uninstall时，表示群内卸载群酷应用事件数据。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### data部分(事件业务信息)

### **事件体数据示例如下:**

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
