---
title: "群内卸载酷应用事件"
source_url: "https://open.dingtalk.com/document/development/intra-cluster-offload-cluster-extension-event-stream"
namespace: "development"
slug: "intra-cluster-offload-cluster-extension-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 群聊酷应用事件 > 群内卸载酷应用事件"
doc_id: "4zi9K1a9Xq"
updated_at: "2025-10-16 14:32:45"
---

> Source: https://open.dingtalk.com/document/development/intra-cluster-offload-cluster-extension-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 群聊酷应用事件 > 群内卸载酷应用事件
> Updated: 2025-10-16 14:32:45

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 字段说明

- `operateTime`（string）：操作时间。
- `coolAppCode`（string）：群扩展code。
- `openConversationCorpId`（string）：群会话企业corpId。
- `robotCode`（string）：机器人code。
- `openConversationId`（string）：群加密会话ID。
- `operator`（string）：操作人userId。

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
