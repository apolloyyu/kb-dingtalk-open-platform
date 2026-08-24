---
title: "企业金融用户协议回调事件"
source_url: "https://open.dingtalk.com/document/development/event-open-user-agreement-callback"
namespace: "development"
slug: "event-open-user-agreement-callback"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > 钉工牌 > 企业金融用户协议回调事件"
doc_id: "ho3nJr91Zu"
updated_at: "2026-07-22 16:25:31"
---

> Source: https://open.dingtalk.com/document/development/event-open-user-agreement-callback
> Path: 应用开发 / 事件订阅 / 办公 > 钉工牌 > 企业金融用户协议回调事件
> Updated: 2026-07-22 16:25:31

# 企业金融用户协议回调事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业金融用户协议回调事件 |
| 英文名称 | open\_user\_agreement\_callback |

## 功能描述

用户代扣签解约事件回调。首先调用该接口获取签约页面员工签约或解约代扣协议时，给对应归属的ISV应用定向推送回调。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.gmtExpire`（string）：过期时间  
    
  格式：yyyy-MM-dd HH:mm:ss
- `data.gmtSign`（string）：签约时间  
    
  格式：yyyy-MM-dd HH:mm:ss
- `data.payChannelAccountName`（string）：支付渠道账号名称
- `data.payChannelAccountNo`（string）：支付渠道账号
- `data.gmtValid`（string）：生效时间  
    
  格式：yyyy-MM-dd HH:mm:ss
- `data.messageType`（string）：消息类型  
    
  \* sign 签约消息  
  \* unsign 解约消息
- `data.agreementNo`（string）：协议编号
- `data.subInstId`（string）：外部商户Id

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "open_user_agreement_callback",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "gmtValid": "2022-03-26 12:49:41",
    "gmtExpire": "2023-07-21 15:47:55",
    "messageType": "sign",
    "agreementNo": "141XXXXX15_2023XXXXXX07",
    "gmtSign": "2022-03-26 12:49:41",
    "payChannelAccountName": "*宝源",
    "payChannelAccountNo": "159***07",
    "subInstId": "944XXXXXXXXXX0250"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.gmtExpire`（string）：过期时间  
    
  格式：yyyy-MM-dd HH:mm:ss
- `biz_data.gmtSign`（string）：签约时间  
    
  格式：yyyy-MM-dd HH:mm:ss
- `biz_data.payChannelAccountName`（string）：支付渠道账号名称
- `biz_data.payChannelAccountNo`（string）：支付渠道账号
- `biz_data.gmtValid`（string）：生效时间  
    
  格式：yyyy-MM-dd HH:mm:ss
- `biz_data.messageType`（string）：消息类型  
    
  \* sign 签约消息  
  \* unsign 解约消息
- `biz_data.agreementNo`（string）：协议编号
- `biz_data.subInstId`（string）：外部商户Id

### **biz\_data数据示例(biz\_type=157)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 157,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "gmtValid": "2022-03-26 12:49:41",
    "gmtExpire": "2023-07-21 15:47:55",
    "messageType": "sign",
    "syncAction": "open_user_agreement_callback",
    "agreementNo": "141XXXXX15_2023XXXXXX07",
    "gmtSign": "2022-03-26 12:49:41",
    "payChannelAccountName": "*宝源",
    "payChannelAccountNo": "159***07",
    "subInstId": "944XXXXXXXXXX0250"
  }
}
```
