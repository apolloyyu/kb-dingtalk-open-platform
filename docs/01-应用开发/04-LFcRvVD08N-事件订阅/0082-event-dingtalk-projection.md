---
title: "钉钉投屏事件"
source_url: "https://open.dingtalk.com/document/development/event-dingtalk-projection"
namespace: "development"
slug: "event-dingtalk-projection"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 钉钉投屏事件"
doc_id: "HSQbPlFtw6"
updated_at: "2025-08-27 16:11:17"
---

> Source: https://open.dingtalk.com/document/development/event-dingtalk-projection
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 钉钉投屏事件
> Updated: 2025-08-27 16:11:17

# 钉钉投屏事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 钉钉投屏事件 |
| 英文名称 | dingtalk\_projection |

## 功能描述

钉钉投屏端发起投屏时，产生的钉钉投屏事件数据。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.unionId`（string）：投屏发送端用户的unionId。
- `data.projectionConferenceId`（string）：公网投屏会议id。  
  - 本地投屏无该字段。
- `data.projectionCode`（string）：投屏码。
- `data.projectionBizType`（string）：投屏类型：  
  \* 1 : 桌面投屏  
  \* 2 : 应用窗口投屏  
  \* 3 : 拓展屏  
  \* 4 : 会议室多方投屏  
  \* 5 : 联系人多方投屏
- `data.projectionType`（string）：投屏模式：  
  \* p2p：公网投屏p2p模式  
  \* conf：公网投屏会议模式  
  \* local：本地投屏  
    
  注：当projectEventType为projection\_process\_start\_all有值。
- `data.sessionId`（string）：投屏会话，唯一标识一次投屏全流程。
- `data.timestamp`（string）：投屏端事件发生时间戳。
- `data.projectionEventType`（string）：投屏发送端子事件类型：  
  \* projection\_process\_start\_all： 发送端发起投屏事件  
  \* projection\_process\_rooms\_dev：发送端往Rooms发起投屏  
  \* projection\_process\_success：投屏成功事件  
  \* projection\_process\_failed：投屏失败事件  
  \* projection\_process\_lose\_connection：投屏掉线事件  
  \* projection\_process\_stop\_all：结束投屏事件

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "dingtalk_projection",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "unionId": "KiiX59w8ZI***jJZjl3giEiE",
    "projectionConferenceId": "2d2sfsdfeee***291",
    "projectionCode": "511759",
    "projectionBizType": "1",
    "projectionType": "local",
    "sessionId": "mac_5B38DC67-C9****BA-01C9E55AB04F",
    "timestamp": "1677662878594",
    "projectionEventType": "projection_process_start_all"
  }
}
```

HTTP推送

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `unionId`（string）：投屏发送端用户的unionId。
- `projectionConferenceId`（string）：公网投屏会议id。  
  - 本地投屏无该字段。
- `projectionCode`（string）：投屏码。
- `projectionBizType`（string）：投屏类型：  
  \* 1 : 桌面投屏  
  \* 2 : 应用窗口投屏  
  \* 3 : 拓展屏  
  \* 4 : 会议室多方投屏  
  \* 5 : 联系人多方投屏
- `projectionType`（string）：投屏模式：  
  \* p2p：公网投屏p2p模式  
  \* conf：公网投屏会议模式  
  \* local：本地投屏  
    
  注：当projectEventType为projection\_process\_start\_all有值。
- `sessionId`（string）：投屏会话，唯一标识一次投屏全流程。
- `timestamp`（string）：投屏端事件发生时间戳。
- `projectionEventType`（string）：投屏发送端子事件类型：  
  \* projection\_process\_start\_all： 发送端发起投屏事件  
  \* projection\_process\_rooms\_dev：发送端往Rooms发起投屏  
  \* projection\_process\_success：投屏成功事件  
  \* projection\_process\_failed：投屏失败事件  
  \* projection\_process\_lose\_connection：投屏掉线事件  
  \* projection\_process\_stop\_all：结束投屏事件

### **事件体示例**

```
{
  "EventType": "dingtalk_projection",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "unionId": "KiiX59w8ZI***jJZjl3giEiE",
  "projectionConferenceId": "2d2sfsdfeee***291",
  "projectionCode": "511759",
  "projectionBizType": "1",
  "projectionType": "local",
  "sessionId": "mac_5B38DC67-C9****BA-01C9E55AB04F",
  "timestamp": "1677662878594",
  "projectionEventType": "projection_process_start_all"
}
```
