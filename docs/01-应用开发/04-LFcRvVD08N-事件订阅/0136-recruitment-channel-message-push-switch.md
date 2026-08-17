---
title: "招聘渠道消息推送开关"
source_url: "https://open.dingtalk.com/document/development/recruitment-channel-message-push-switch"
namespace: "development"
slug: "recruitment-channel-message-push-switch"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能招聘 > 招聘渠道消息推送开关"
doc_id: "d45RKGOO1b"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/recruitment-channel-message-push-switch
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能招聘 > 招聘渠道消息推送开关
> Updated: 2022-01-19 19:29:22

# 招聘渠道消息推送开关

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 招聘渠道消息推送开关 |
| 英文名称 | rcm\_channel\_message\_push |

## 功能描述

该事件用于通知与钉钉智能招聘打通的招聘渠道平台，用户在智能招聘侧设置渠道候选人投递简历的通知消息是否通过IM进行推送。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "rcm_channel_message_push",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpId": "ding2c015874d8dasv",
    "pluginCode": "af235g2",
    "outId": "rcmsdag123722",
    "pushAction": "openMessagePush",
    "channelAccountId": "rcmsdag123722",
    "userId": "dsfa2335glk234235"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=244)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 244,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpId": "ding2c015874d8dasv",
    "syncAction": "rcm_channel_message_push",
    "pluginCode": "af235g2",
    "outId": "rcmsdag123722",
    "pushAction": "openMessagePush",
    "channelAccountId": "rcmsdag123722",
    "userId": "dsfa2335glk234235"
  }
}
```
