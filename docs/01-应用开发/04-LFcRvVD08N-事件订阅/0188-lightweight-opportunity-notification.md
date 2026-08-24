---
title: "轻量级商机通知"
source_url: "https://open.dingtalk.com/document/development/lightweight-opportunity-notification"
namespace: "development"
slug: "lightweight-opportunity-notification"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 轻量级商机通知"
doc_id: "N6X2p5ONP3"
updated_at: "2025-08-28 19:47:21"
---

> Source: https://open.dingtalk.com/document/development/lightweight-opportunity-notification
> Path: 应用开发 / 事件订阅 / 应用市场 > 轻量级商机通知
> Updated: 2025-08-28 19:47:21

# 轻量级商机通知

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 轻量级商机通知 |
| 英文名称 | light\_opportunity\_notice |

## 功能描述

客户触发的进服务群、提交业务需求等轻量级商机触发事件

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
- `data.opportunityType`（string）：商机类型：  
  - 服务群  
  - 需求提交
- `data.source`（string）：商机来源：  
  - 工作台  
  - 市场
- `data.orgName`（string）：客户组织名称。
- `data.customerCorpId`（string）：客户组织ID。
- `data.userName`（string）：用户名。
- `data.demand`（string）：客户详细需求描述。
- `data.goodsCode`（string）：商品码。
- `data.goodsName`（string）：商品名称。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "light_opportunity_notice",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "opportunityType": "需求提交",
    "orgName": "杭州XXX有限责任公司",
    "customerCorpId": "dingf1de093e65722e314ac5d6980864d335",
    "source": "工作台",
    "goodsCode": "DT_GOODS_881594729797745",
    "userName": "XXX",
    "demand": "我是一个财务，想要高效解决企业报销等问题。。。",
    "goodsName": "智能财务"
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
- `biz_data.opportunityType`（string）：商机类型：  
  - 服务群  
  - 需求提交
- `biz_data.source`（string）：商机来源：  
  - 工作台  
  - 市场
- `biz_data.orgName`（string）：客户组织名称。
- `biz_data.customerCorpId`（string）：客户组织ID。
- `biz_data.userName`（string）：用户名。
- `biz_data.demand`（string）：客户详细需求描述。
- `biz_data.goodsCode`（string）：商品码。
- `biz_data.goodsName`（string）：商品名称。

### **biz\_data数据示例(biz\_type=367)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 367,
  "biz_data": {
    "opportunityType": "需求提交",
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "orgName": "杭州XXX有限责任公司",
    "syncAction": "light_opportunity_notice",
    "customerCorpId": "dingf1de093e65722e314ac5d6980864d335",
    "source": "工作台",
    "goodsCode": "DT_GOODS_881594729797745",
    "userName": "XXX",
    "demand": "我是一个财务，想要高效解决企业报销等问题。。。",
    "goodsName": "智能财务"
  }
}
```
