---
title: "批量支付消息通知"
source_url: "https://open.dingtalk.com/document/development/event-open-batch-trade-callback"
namespace: "development"
slug: "event-open-batch-trade-callback"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > 钉工牌 > 批量支付消息通知"
doc_id: "19NQ9Gnm9t"
updated_at: "2026-07-22 16:25:31"
---

> Source: https://open.dingtalk.com/document/development/event-open-batch-trade-callback
> Path: 应用开发 / 事件订阅 / 办公 > 钉工牌 > 批量支付消息通知
> Updated: 2026-07-22 16:25:31

# 批量支付消息通知

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 批量支付消息通知 |
| 英文名称 | open\_batch\_trade\_callback |

## 功能描述

批量支付完成事件回调，创建批量付款单并支付后，当支付处理完成时，给对应归属的ISV应用定向推送回调。

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
- `data.failCount`（integer）：失败笔数。
- `data.successAmount`（float）：成功金额（元）。
- `data.paymentAmount`（float）：付款方需要支付的金额（元）。
- `data.totalAmount`（float）：批次的总金额（元）。
- `data.outBatchNo`（string）：外部商户批次号。
- `data.successCount`（integer）：成功笔数。
- `data.failAmount`（float）：明细处理失败的支付汇总金额。
- `data.alipayTransId`（string）：支付宝批次订单号。
- `data.status`（string）：状态:  
  \* SUCCESS 成功  
  \* FAIL 失败  
  \* PART\_SUCESS 部分成功  
  \* SYSTEM\_TERMINATE 系统原因中断  
  \* MANUAL\_TERMINATE 人工中断
- `data.gmtFinish`（string）：批次完成交易时间。
- `data.gmtSubmit`（string）：批次受理交易时间。
- `data.failReason`（string）：失败原因。
- `data.paymentCurrency`（string）：支付币种。
- `data.payerStaffId`（string）：付款人userId。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "open_batch_trade_callback",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "failCount": 1,
    "gmtFinish": "2023-07-21 14:00:00",
    "successAmount": 19.5,
    "paymentAmount": 21.0,
    "totalAmount": 21.0,
    "outBatchNo": "2023XXXXXXX06",
    "successCount": 5,
    "alipayTransId": "2002XXXXXXX92",
    "gmtSubmit": "2023-07-21 13:58:57",
    "failAmount": 1.5,
    "failReason": "账号异常",
    "payerStaffId": "332XXXX011",
    "paymentCurrency": "CNY",
    "status": "SUCCESS"
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
- `biz_data.failCount`（integer）：失败笔数。
- `biz_data.successAmount`（float）：成功金额（元）。
- `biz_data.paymentAmount`（float）：付款方需要支付的金额（元）。
- `biz_data.totalAmount`（float）：批次的总金额（元）。
- `biz_data.outBatchNo`（string）：外部商户批次号。
- `biz_data.successCount`（integer）：成功笔数。
- `biz_data.failAmount`（float）：明细处理失败的支付汇总金额。
- `biz_data.alipayTransId`（string）：支付宝批次订单号。
- `biz_data.status`（string）：状态:  
  \* SUCCESS 成功  
  \* FAIL 失败  
  \* PART\_SUCESS 部分成功  
  \* SYSTEM\_TERMINATE 系统原因中断  
  \* MANUAL\_TERMINATE 人工中断
- `biz_data.gmtFinish`（string）：批次完成交易时间。
- `biz_data.gmtSubmit`（string）：批次受理交易时间。
- `biz_data.failReason`（string）：失败原因。
- `biz_data.paymentCurrency`（string）：支付币种。
- `biz_data.payerStaffId`（string）：付款人userId。

### **biz\_data数据示例(biz\_type=134)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 134,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "open_batch_trade_callback",
    "failCount": 1,
    "gmtFinish": "2023-07-21 14:00:00",
    "successAmount": 19.5,
    "paymentAmount": 21.0,
    "totalAmount": 21.0,
    "outBatchNo": "2023XXXXXXX06",
    "successCount": 5,
    "alipayTransId": "2002XXXXXXX92",
    "gmtSubmit": "2023-07-21 13:58:57",
    "failAmount": 1.5,
    "failReason": "账号异常",
    "payerStaffId": "332XXXX011",
    "paymentCurrency": "CNY",
    "status": "SUCCESS"
  }
}
```
